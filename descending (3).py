class Student:

  def _init_(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sorted_students(student_list):
  sorted_students = sorted(students_list, key=lambda student:
student.cgpa,
                           reverse=True)
  return sorted_students

students =[
        Student("John doe","A101",3.8),
        Student("John doe","B202",3.9),
        Student("Jim smith","C303",3.7),
        Student("jill Johnson","D404",4.0),
        ]

sorted_students = sorted_students(students)

for student in sorted_students:
                           print("Name: {}, Roll Number: {}, CGPA: {}" .format(student.name,student.rollnumber,student.cgpa))