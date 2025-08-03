import string 
import random
import getpass

def check_password_strength(password):
  issues = []
  if len(password) < 8:
    issues.append("Too short (minimum 8 characters)")
  if not any(c.islower() for c in password):
    issues.append("Missing lower case letter")
  if not any(c.isupper() for c in password):
    issues.append("Missing upper case letter")
  if not any(c.isdigit() for c in password):
    issues.append("Missing a number")
  if not any(c in string.punctuation for c in password):
    issues.append("Missing a special character")
  return issues

def generate_strong_password(length=12):
  chars = string.ascii_letters + string.digits + string.punctuation
  chars_lower = "abcdefghijklmnopqrstuvwxyz"
  chars_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  chars_number = "0123456789"
  chars_special = "`~!@#$%^&*()-_=+[];',./<>?:}|{"

  password1 = "".join(random.choice(chars_lower) for _ in range(3))
  
  password2 = "".join(random.choice(chars_upper) for _ in range(3))
  
  password3 = "".join(random.choice(chars_number) for _ in range(3))
  
  password4 = "".join(random.choice(chars_special) for _ in range(3))
  
  password = password1+password2+password3+password4

  return password

password = getpass.getpass("Enter a password: ")

issues = check_password_strength(password)

if not issues:
  print("Strong password! you are good to go...")
else: 
  print("You got weak password")
  for issue in issues:
    print(f"- {issue}")

  suggestion = generate_strong_password()
  print("\n suggesting you a strong password: ")
  print(suggestion)