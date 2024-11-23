from student_card import StudentCard
from course_info import Student

class HonorStudentCard:
    def __init__(self, student_card: StudentCard):
        self._student_card = student_card

    def give_details(self):
        details = self._student_card.give_details()
        details["honors"] = True
        details["benefits"] = "Priority in course registration, scholarship eligibility"
        return details

class TopStudent:
    def __init__(self, student: Student):
        self._student = student

    def give_details(self):
        details = self._student.give_details()
        details["recognition"] = "Top performer"
        details["benefits"] = "Exclusive mentorship program and awards"
        return details
