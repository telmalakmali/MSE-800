#Activity2: You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. Each row represents a student, and each column a subject. See below:
 #scores = np.array([
# [78, 85, 90],
#[88, 79, 92],
#[84, 76, 88],
#[90, 93, 94],
#[75, 80, 70]])
 
#Tasks:
#Calculate and print the average score for each student.
#Calculate and print the average score for each subject.
#Identify the student (row index) with the highest total score.
#Add 5 bonus points to the third subject for all students.
    
import numpy as np

scores = np.array([
[78, 85, 90],
[88, 79, 92],
[84, 76, 88],
[90, 93, 94],
[75, 80, 70]
])


#Calculate and print the average score for each student.
student1 = scores[0,:]
student2 = scores[1,:]
student3 = scores[2,:]
student4 = scores[3,:]
student5 = scores[4,:]
print("Student1 Average score is",np.mean(student1))
print("Student2 Average score is",np.mean(student2))
print("Student3 Average score is",np.mean(student3))
print("Student4 Average score is",np.mean(student4))
print("Student5 Average score is",np.mean(student5))

#Calculate and print the average score for each subject.
Subject1 = scores[:,0]
Subject2 = scores[:,1]
Subject3 = scores[:,2]
print("Avenarge of subject1",np.mean(Subject1))
print("Avenarge of subject2",np.mean(Subject2))
print("Avenarge of subject3",np.mean(Subject3))

#Identify the student (row index) with the highest total score.
Student1totoalscore = np.sum(student1)
Student2totoalscore = np.sum(student2)
Student3totoalscore = np.sum(student3)
Student4totoalscore = np.sum(student4)
Student5totoalscore = np.sum(student5)
TotalScore = np.array([Student1totoalscore, Student2totoalscore, Student3totoalscore, Student4totoalscore, Student5totoalscore])
Maxscore = np.max(TotalScore)
Maxindex =np.argmax(TotalScore)
print("Student row index of the highest score is",Maxindex,"And the score is",Maxscore)

#Add 5 bonus points to the third subject for all students.
Subject3Updated = np.add(Subject3,5)
print("Subject 3 new values are",Subject3Updated)

