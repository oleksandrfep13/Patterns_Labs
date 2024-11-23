from student_card import StudentCard
from course_info import CourseInfo, Student, PersonalInfo
from student_decorators import HonorStudentCard, TopStudent

student_card = StudentCard("Anna Senna", "ST1024", "Computer Science", 3.9)

course_info = CourseInfo("Data Structures", "Dr. Philip Davidson", ["Anna Senna", "John Doe"])

personal_info = PersonalInfo(name="Anna Senna", age=24, address="29, Rockford Street, New York, NY 10117")
student = Student(personal_info, course_info)

honor_card = HonorStudentCard(student_card)
print("Honor Student Card Details:", honor_card.give_details())

top_student = TopStudent(student)
print("Top Student Details:", top_student.give_details())
