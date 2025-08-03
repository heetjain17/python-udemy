import csv
import os

FILENAME = "contacts.csv"

# Initialize the file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Check if contact exists
    try:
        with open(FILENAME, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Name"].lower() == name.lower():
                    print("Contact name already exists")
                    return
    except FileNotFoundError:
        pass  # File will be created when we write to it
        
    with open(FILENAME, 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact added")

def view_contacts():
    try:
        with open(FILENAME, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            # Skip header and filter out empty rows
            rows = [row for row in reader if row and len(row) >= 3][1:]
            
            if not rows:
                print("\nNo contacts found\n")
                return
            
            print("\nYour contacts:\n")
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]}")
            print()
    except FileNotFoundError:
        print("\nNo contacts found (file doesn't exist yet)\n")

def search_contacts(): 
    term = input("Enter the name to search: ").strip().lower()
    found = False

    try:
        with open(FILENAME, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if term in row["Name"].lower():
                    print(f"{row['Name']} | {row['Phone']} | {row['Email']}")
                    found = True
    except FileNotFoundError:
        pass  # File doesn't exist yet
  
    if not found:
        print("No matching contact found")

def main():
    while True:
        print("--- Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option(1-4): ").strip()

        match choice:
            case "1":
                add_contact()
            case "2":
                view_contacts()
            case "3":
                search_contacts()
            case "4":
                break
            case _:
                print("Invalid choice") 

if __name__ == "__main__":
    main()