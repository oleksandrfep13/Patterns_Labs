from dataclasses import dataclass
from typing import List

class CourseInfo:
    def __init__(self, course_name: str, instructor: str, students_list: List[str]):
        self.course_name = course_name
        self.instructor = instructor
        self.students_list = students_list
        self.grades = {}

    def get_students(self) -> List[str]:
        return self.students_list

    def assign_grade(self, student: str, grade: float):
        if student in self.students_list:
            self.grades[student] = grade
        else:
            print(f"Student {student} is not enrolled in this course.")

@dataclass
class PersonalInfo:
    name: str
    age: int
    address: str

class Student:
    def __init__(self, personal_info: PersonalInfo, course_details: CourseInfo):
        self.personal_info = personal_info
        self.course_details = course_details

    def give_details(self) -> dict:
        return {
            "personal_info": self.personal_info,
            "course_info": {
                "course_name": self.course_details.course_name,
                "instructor": self.course_details.instructor,
                "students_list": self.course_details.students_list,
                "grades": self.course_details.grades
            }
        }
