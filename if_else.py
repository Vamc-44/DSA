# IF Else, ELif Else are conditional statements in Python
# IF statement is used to test a condition  
# If the condition is true, the code block inside the IF statement is executed
# If the condition is false, the code block inside the IF statement is skipped  

Marks = int(input("Enter the marks: "))

if Marks >= 90:
    print("Grade A")
    print("Excellent")
elif Marks >= 80 and Marks < 90:
    print("Grade B")
    print("Very Good")
elif Marks >= 70 and Marks < 80:
    print("Grade C")
    print("you can be better")
elif Marks >= 60 and Marks < 70:
    print("Grade D")
    print("You need to improve")
elif Marks <= 50 and Marks >= 35:   
    print("Grade E")
    print("You need to work hard")
else:
    print("Grade F")
    print("You failed")
