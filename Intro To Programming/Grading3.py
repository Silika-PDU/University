	
# Grading #3
# Write a program that will help you grade the students’ achievements. The maximum score available on the test is 100 points, and the student’s mark is

# excellent if he scored at least 80 points;
# good if he scored at least 70 points but did not reach 80 points;
# satisfactory if he scored at least 60 points but did not reach 70 points;
# pass it he scored at least 50 points but did not reach 60 points;
# fail if he did not reach 50 points.

student_marks = int(input("Enter your marks: "))

if student_marks >= 80:
    print("excellent")
elif student_marks >= 70:
    print("good")
elif student_marks >= 60:
    print("satisfactory")
elif student_marks >= 50:
    print("pass")
else:
    print("fail")