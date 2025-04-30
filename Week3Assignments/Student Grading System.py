#Activity 2: Deadline 2 May - Simple Student Grading System Using classes
#Task: Create students, record their grades, and show results.

class gradingSystem:
    record = []
    def Cstudent():
            student =input("Please enter student number : ")
            grade = input("Please enter the grade for the student : ")
            record = {
                 "Bstudent": student,
                 "Bgrade":grade
             }
            gradingSystem.record.append((student,grade))
            gradingSystem.add()
    
    def showResults():
        B= input ("Do you wish to view student grade? Y/N ? ")
        if B == "Y":
            print("Student grades are", gradingSystem.record)
        else:
            exit

    def add():
         A = input("Please type Y to add record or N to go back to the main menu : ")
         if A == "Y":
              gradingSystem.Cstudent()
         else:
              gradingSystem.process()


    def process():
        C = input ("Please type Y to add student records or N to view records? Y/N ? ")
        if C == "Y":
            gradingSystem.add()
        else:
            gradingSystem.showResults()
    
gradingSystem.process()




    

    
 
 