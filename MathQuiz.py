import random 

def display_title():
    print('''
******************
A Simple Math Quiz
******************  
    ''')

def display_option():
    list_options=["1.Addition", "2.Subtraction", "3.Multiplication", "4.Division", "5.Exit"]
    for option in list_options:
        print(option)
    print("__________________")

#Get user input for the choice of mathematical operations to be performed
def getUserInput():
    choice=int(input("Enter your choice:"))
    while choice>5 or choice<1:
        print("Invalid menu option, try again!!")
        choice=int(input("Enter your choice:"))
    return choice

def getUserSolution(problem):
    print("Enter your answer")
    print(problem,end="")
    result=int(input("="))
    return result

def getProblem(operation):
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    if operation==1:
        problem=(f"{num1}+{num2}")
        solution=num1+num2
    
    elif operation==2:
        problem=(f"{num1}-{num2}")
        solution=num1-num2

    elif operation==3:
        problem=(f"{num1}*{num2}")
        solution=num1*num2
    
    elif operation==4:
        problem=(f"{num1}/{num2}")
        solution=num1/num2

    return problem,solution

def main():
    display_title()
    display_option()
    option=getUserInput()
    correctAnswer=0
    totalQuestion=0

    while option!=5:
        prob,solution=getProblem(option)
        userAnswer=getUserSolution(prob)
        if userAnswer==solution:
            print("Correct!!")
            correctAnswer=correctAnswer+1
            totalQuestion=totalQuestion+1
        else:
            print("Incorrect!!")
            totalQuestion=totalQuestion+1
        option=getUserInput()
    
    print("Total questions asked answered:",totalQuestion)
    print("Correctly answered:",correctAnswer)
    print("Percentage correctly answered",round((correctAnswer*100)/totalQuestion,2))
    
main()
