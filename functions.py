# ------------------------------------------------------------------------------------------ #
# Title: functions
# Desc: This file contains python classes that
# are imported to Assignment06.py
# Change Log: (Who, When, What)
#   James Copsey,11/20/2024,Created file
# ------------------------------------------------------------------------------------------ #

import json
from typing import TextIO

class FileProcessor:
    """
    JSON file processing functions

    ChangeLog:
    jcopsey,11/20/2024,Created class
    jcopsey,11/20/2024,Added function to read file or create if not found
    jcopsey,11/20/2024,Added function to write to file
    """
    @staticmethod
    def read_data_from_file(file_name:str,student_data:list):
        """
        Function to read data from JSON file
        Create file if not found

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: Data read from JSON file
        """
        file: TextIO = None
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            file = open(file_name, 'w')
            file.close()
            IO.output_error_messages(
                message=f"File not found. Creating {file_name}", error=e
            )
        except Exception as e:
            IO.output_error_messages(e.__str__())
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name:str,student_data:list):
        """
        Write data to JSON file

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: None
        """
        file: TextIO
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print(f"The following data was saved to {file_name}")
            for student in student_data:
                print((
                    f"Student {student['FirstName']} "
                    f"{student['LastName']} is enrolled in "
                    f"{student['CourseName']}"
                ))
        except Exception as e:
            if not file.closed:
                file.close()
            IO.output_error_messages(
                message=f"Error: Problem writing to {file_name}.\n" +
                "Please check that the file is not open by another program.\n",
                error=e
            )

class IO:
    """
    JSON file processing functions

    ChangeLog:
    jcopsey,11/20/2024,Created class
    jcopsey,11/20/2024,Added function to read file or create if not found
    jcopsey,11/20/2024,Added function to write to file
    """

    @staticmethod
    def output_error_messages(message:str, error: Exception = None):
        """
        Displays custom error message

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu:str):
        """
        Prints the options menu to the user

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: None
        """
        print(f"\n{menu}\n")

    @staticmethod
    def input_menu_choice():
        """
        Takes user choice from the user

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: The string the user entered
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ["1","2","3","4"]:
                raise Exception("Please only enter 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data:list):
        """
        Prints current list of students and registered courses

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: None
        """
        try:
            print()
            print("-" * 50)
            for student in student_data:
                print((
                    f"Student {student['FirstName']} "
                    f"{student['LastName']} is enrolled "
                    f"in {student['CourseName']}"
                ))
            print("-" * 50)
        except Exception as e:
            IO.output_error_messages(e.__str__())

    @staticmethod
    def input_student_data(student_data:list):
        """
        Gets first + last + course name from user and
        appends current list of students and registered courses

        ChangeLog:
        jcopsey,11/20/2024,Created function

        :return: Updated students list
        """
        students: list = student_data
        try:
            student_first_name : str = input(
                "Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name : str = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print((
                f"\nYou have registered {student_first_name} "
                f"{student_last_name} for {course_name}."
            ))
        except ValueError as e:
            IO.output_error_messages(message="Invalid value.", error=e)
        except Exception as e:
            IO.output_error_messages(e.__str__())
        finally:
            return students