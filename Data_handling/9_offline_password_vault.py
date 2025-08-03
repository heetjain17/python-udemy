import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
  return base64.b64encode(text.encode()).decode()

def decode(text):
  return base64.b64decode(text.encode()).decode()

def password_strength(password):
  length = len(password)
  has_upper = any(c.isupper() for c in password)  
  has_digit = any(c.isdigit() for c in password)  
  has_special = any(c in "!@#$%^&*()_-=][;',/.|:>?<]" for c in password)  

  score = sum([length >= 8, has_upper, has_special, has_digit])
  return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credentials():
  website = input("Website: ").strip()
  username = input("Username: ").strip()
  password = input("Password: ").strip()

  strength = password_strength(password)

  line = f"{website} || {username} || {password}"
  encoded_line = encode(line)

  with open(VAULT_FILE, 'a', encoding='utf-8') as f:
    f.write(encoded_line + "\n") 

  print("✅ Credentials saved")

def view_credentials():
  if not os.path.exists(VAULT_FILE):
    print("File not found")
    return
  
  with open(VAULT_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      decoded = decode(line.strip())
      website, username, password = decoded.split("||") 
      hidden_password = '*' * len(password)
      print(f"{website} | {username} | {password}")

def main(): 
  while True:
    print("Credential manager")
    print("1. Add credential")
    print("2. View all credentials")
    print("3. Update password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:
      case "1":
        add_credentials()
      case "2":
        view_credentials()
      case "3":
        pass
      case "4":
        break
      case _:
        print("Enter a valid choice")

if __name__ == "__main__":
  main()