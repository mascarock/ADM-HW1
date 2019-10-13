if __name__ == '__main__':
    # get the number of students
    studentsNumber = int(int(input()))
    # grade and students for each student
    gradeStudents = [[input(),float(input())] for i in range(0 , studentsNumber)]
    # list of grades
    grades = []
    for grade in gradeStudents: grades.append(grade[1])
    # Create a set of grades and find the min
    setGrades = set(grades)
    setGrades.remove(min(setGrades))   
    # Compute the second lowest grade
    minGrade = min(setGrades)
    # Get the students name 
    minStudents = [s[0] for s in gradeStudents if s[1] == minGrade]
    # sort the set
    sortedStudents = sorted(minStudents)
    # print the students
    for s in sortedStudents:
        print(s)
    