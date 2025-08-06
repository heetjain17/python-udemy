import os
import shutil

def batch_rename(folder, base_name, extension):
  files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
  files.sort()

  if not files:
    print("No files found in dir")
    return
  
  for i, file in enumerate(files, start=1):
    new_name = f"{base_name}_{i}{extension}"
    print(f"{file} => {new_name}")

  confirm = input("Press (y) to confirm or (n) to reject: ").strip().lower()

  if confirm != 'y':
    print("Cancel")
    return
  
  for i, file in enumerate(files, start=1):
    src = os.path.join(folder, file)
    new_name = f"{base_name}_{i}{extension}"
    dest = os.path.join(folder, new_name)
    os.rename(src, dest)

  print(f"Renamed {len(files)} files sucessfully")

if __name__ == "__main__":
  folder = input("Enter folder path else leave blank: ").strip() or os.getcwd()
  
  if not os.path.isdir(folder):
    print("Invalid folder")
  else:
    base_name = input("Enter the base name for files: ").strip()
    extension = input("Enter extension name for files: ").strip()

    batch_rename(folder, base_name, extension)


