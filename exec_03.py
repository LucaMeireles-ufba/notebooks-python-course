class Grades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

def main():
    student_grades = Grades()

    for i in range(3):
        try:
            grade_input = input(f"Enter grade {i + 1} (or 'done' to finish): ")
            if grade_input.lower() == 'done':
                break
            grade = float(grade_input)
            student_grades.add_grade(grade)
        except ValueError:
            raise ValueError("Invalid input for grade. Please enter a number between 0 and 10. Dumbass.");
    avg = student_grades.average()
    if avg < 7:
        print(f"The average grade is: {avg:.2f}, you've failed the class, dumb!")
    else:
        print(f"Congrats, smartass, you've passed the class with {avg:.2f}")
if __name__ == "__main__":
    main()