import hashlib

class StudentCard:
    def __init__(self, student_name: str, student_id: str, major: str, gpa: float):
        self.student_name = student_name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self._identifier = self.encrypt(student_id)

    def encrypt(self, value: str) -> str:
        return hashlib.sha256(value.encode()).hexdigest()

    def give_details(self) -> dict:
        return {
            "student_name": self.student_name,
            "student_id": self.student_id,
            "major": self.major,
            "gpa": self.gpa,
            "identifier": self._identifier
        }
