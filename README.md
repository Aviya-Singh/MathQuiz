# MathQuiz
This Python program is a simple math quiz game. It allows the user to choose from a menu of mathematical operations (addition, subtraction, multiplication, and division) and then presents random math problems based on the selected operation. The user must solve these problems, and the program will provide feedback on whether their answers are correct or not. The program keeps track of the number of correct answers, the total number of questions asked, and the percentage of questions answered correctly.

Here's a brief description of the program's main components:
display_title(): Displays the title of the math quiz.
display_option(): Displays a menu of mathematical operations for the user to choose from.
getUserInput(): Gets the user's choice for the mathematical operation. It ensures that the user enters a valid choice between 1 and 5.
getUserSolution(problem): Gets the user's answer to a math problem presented in the format of "num1 + num2 =".
getProblem(operation): Generates a random math problem based on the selected operation and returns the problem and its correct solution.
main(): The main function that orchestrates the quiz. It displays the title and options, gets the user's choice, and repeatedly presents math problems until the user selects the "Exit" option. It keeps track of correct answers and displays the total number of questions and the percentage of correctly answered questions.
