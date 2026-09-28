# Course Management System

A Python mini-project demonstrating core Object-Oriented Programming (OOP) concepts.

## Overview

This project implements a simple Course Management System featuring users, students, mentors, courses, and enrollments. It is designed specifically to showcase the fundamental principles of Object-Oriented Programming in Python.

## OOP Concepts Demonstrated

This project implements the following OOP concepts:

1. **Classes and Objects**
   - Implemented multiple classes: `User`, `Student`, `Mentor`, `Course`, and `Enrollment` to model real-world entities.
   
2. **Inheritance**
   - Both `Student` and `Mentor` classes inherit from the base `User` class, reusing its attributes and methods while defining their own specific behaviors.

3. **Encapsulation**
   - **Protected Attributes**: Used `_name` and `_email` in the `User` class.
   - **Private Attributes**: Used `__student_id` in the `Student` class and `__employee_id` in the `Mentor` class to prevent direct external access.
   - **Property Decorators**: Utilized `@property` and `@name.setter` to safely manage getting and setting variable data (e.g., adding validation to ensure the name isn't empty).

4. **Abstraction**
   - The `User` class inherits from `ABC` (Abstract Base Class).
   - Utilized the `@abstractmethod` decorator for the `get_role_details()` method, ensuring that any subclass of `User` must implement this method.

5. **Polymorphism**
   - The `get_details()` method in the base `User` class calls `get_role_details()`. Because `Student` and `Mentor` provide their own unique implementations of `get_role_details()`, the `get_details()` method behaves differently depending on which object calls it.

6. **Instance Methods**
   - Utilized standard methods that operate on specific instances, such as `assign_course(self, course)` in the `Mentor` class and `_process_enrollment(self)` in the `Enrollment` class.

7. **Class Methods (`@classmethod`)**
   - The `get_total_users(cls)` method in the `User` class demonstrates interacting with class-level state (`_total_users`), rather than instance-level state.

8. **Static Methods (`@staticmethod`)**
   - The `is_valid_course_code(code)` method in the `Course` class demonstrates a utility function that logically belongs to the class but doesn't require access to `self` or `cls`.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `course_management.py` file.
3. Open your terminal or command prompt.
4. Run the script:
   ```bash
   python course_management.py
   ```
5. You should see output demonstrating the successful creation of users, courses, an enrollment, and the polymorphic output of their details.
