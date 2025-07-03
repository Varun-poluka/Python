try:
    score = float(input("Enter the score:")) #trying to convert entered string into float
except:
    print("entered is not a number:") #if entered is not a number 
#checking the scores and printing grade
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Error not a right score")