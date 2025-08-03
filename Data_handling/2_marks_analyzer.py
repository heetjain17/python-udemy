def collect_student_data():
  students = {}
  while True:
    name = input("Enter the student name or done to exit: \n").strip()
    if name.lower() == "done":
      break
    if name in students:
      print("Student already exists")
      continue

    try:
      marks = float(input(f"Enter marks for {name}: "))
      students[name] = marks
      
    except ValueError:
      print("Please enter a valid number for marks")

  return students
  
def display_reports(students):
  if not students:
    print("No student data")
    return
  
  marks = list(students.values())
  max_score = max(marks)
  min_score = min(marks)
  average_score  = sum(marks)/ len(marks)

  topper = [name for name, score in students.items() if score == max_score]
  dummy = [name for name, score in students.items() if score == min_score]

  print("\nStudents marks report")
  print(f"Total students: {len(students)}")
  print(f"Average marks for students: {average_score:.2f}")
  print(f"Highest marks: {max_score} by {', '.join(topper)}")
  print(f"Lowest marks: {min_score} by {', '.join(dummy)}")

  print("Detailed Marks")
  for name, score in students.items():
    print(f"- {name}: {score}")

students = collect_student_data()
display_reports(students)