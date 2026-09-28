from abc import ABC, abstractmethod
from datetime import date
import re

class User(ABC):
    """Abstract base class representing a generic user."""
    
    # Class attribute to keep track of total users
    _total_users = 0

    def __init__(self, name: str, email: str):
        # Encapsulation: using protected/private attributes
        self._name = name
        self._email = email
        User._total_users += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def email(self):
        return self._email

    @abstractmethod
    def get_role_details(self) -> str:
        """Abstract method to enforce implementation in subclasses (Abstraction)."""
        pass

    def get_details(self) -> str:
        """Base method demonstrating Polymorphism when overridden or used with subclass specific details."""
        return f"Name: {self._name}, Email: {self._email}, Role: {self.get_role_details()}"

    @classmethod
    def get_total_users(cls) -> int:
        """Class method demonstrating state across all instances."""
        return cls._total_users

class Student(User):
    """Student class inheriting from User (Inheritance)."""
    
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.__student_id = student_id  # Strict encapsulation
        self.enrollments = []

    def get_role_details(self) -> str:
        """Implementation of abstract method (Polymorphism)."""
        return f"Student [ID: {self.__student_id}]"


class Mentor(User):
    """Mentor class inheriting from User (Inheritance)."""

    def __init__(self, name: str, email: str, employee_id: str):
        super().__init__(name, email)
        self.__employee_id = employee_id
        self.assigned_courses = []

    def get_role_details(self) -> str:
        """Implementation of abstract method (Polymorphism)."""
        return f"Mentor [EMP ID: {self.__employee_id}]"

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.mentor = self


class Course:
    """Class representing a course."""

    def __init__(self, course_code: str, course_name: str):
        if not self.is_valid_course_code(course_code):
            raise ValueError("Invalid course code format. Must be like 'CS101'.")
        self.course_code = course_code
        self.course_name = course_name
        self.mentor = None

    @staticmethod
    def is_valid_course_code(code: str) -> bool:
        """Static method as it doesn't require access to instance or class state."""
        return bool(re.match(r'^[A-Z]{2}\d{3}$', code))

    def __str__(self):
        mentor_name = self.mentor.name if self.mentor else "Not Assigned"
        return f"Course: {self.course_name} ({self.course_code}) - Mentor: {mentor_name}"

    
class Enrollment:
    """Class to manage enrollments connecting Students and Courses."""    
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        self.enrollment_date = date.today()
        # Instance method action
        self._process_enrollment()

    def _process_enrollment(self):
        """Private instance method for internal logic."""
        self.student.enrollments.append(self)
        print(f"Successfully enrolled {self.student.name} into {self.course.course_name} on {self.enrollment_date}")



# --- Demonstration ---
if __name__ == "__main__":
    print(f"Initial Total Users: {User.get_total_users()}")

    # 1. Create Users
    student1 = Student("Alice Smith", "alice@example.com", "S1001")
    mentor1 = Mentor("Bob Jones", "bob@example.com", "M500")

    # 2. Abstract Base Class prevents instantiation:
    # user = User("Invalid", "invalid@test.com") # This would raise TypeError

    # 3. Create Course and assign Mentor
    course1 = Course("CS101", "Introduction to Python")
    mentor1.assign_course(course1)

    # 4. Process Enrollment
    enrollment1 = Enrollment(student1, course1)

    print("\n--- Details ---")
    # Polymorphism in action via get_details() calling overridden get_role_details()
    users = [student1, mentor1]
    for u in users:
        print(u.get_details())

    print("\n--- Course Info ---")
    print(course1)

    print(f"\nFinal Total Users: {User.get_total_users()}")
