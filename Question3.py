def studentStats(filename):
    '''
    Write a function that reads the data from the file into a dictionary.
    Then continue prompting the user for names of students.
    For each student, it should print the average of that student’s grades.
    Stop prompting when the user enters the name of a student not in the dictionary.
    '''
    # Open file and initialize dictionary
    student_grades = {}

    # Read lines from the file and process
    with open(filename, 'r') as file:
        for line in file:
            name, grade = line.strip().split()
            grade = int(grade)

        # Add the grade to the list of grades for this student
            if name in student_grades:
                student_grades[name].append(grade)
            else:
                student_grades[name] = [grade]

    return student_grades

def calculate_average(grades):
    return sum(grades) / len(grades)


if __name__ == "__main__":
    student_grades = studentStats('students.txt')

    while True:
        sname = input("Enter a student name or hit enter to quit: ").strip()

        if sname == "":
            print("Goodbye!")
            break

        if sname in student_grades:
            avg = calculate_average(student_grades[sname])
            print(f"{sname}'s average is {avg:.1f}")
        else:
            print("Goodbye!")
            break

