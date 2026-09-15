from pyscript import document, display

a = "Student Name: Raphael Buan"
b = "Age: 15"
height1 = "Height: 165cm"
_Countries3 = "Countries I want to visit: Canada, South Korea, America"
student_type = "Are you a student?: True"

_things3 = {"Shoe Brand: Nike", "Car Brand: Tesla", "Best Friend: Dustin"}
fruit5 = {"Apple": "Grapes", "Oranges": "Banana", "Mangoes": "Pineapple"}
_Sevendays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

display(a)
display(b)
display(height1)
display(student_type)
display(_Countries3)
display(_things3)
display(fruit5)
display(_Sevendays)


def Add(g):
    document.getElementById("result").innerHTML = ""
    num1 = int(document.getElementById("input1").value)
    num2 = int(document.getElementById("input2").value)

    display(num1 + num2, target="result")


def Subtraction(g):
    document.getElementById("result").innerHTML = ""
    num1 = int(document.getElementById("input3").value)
    num2 = int(document.getElementById("input4").value)

    display(num1 - num2, target="result")


def Multiply(g):
    document.getElementById("result").innerHTML = ""
    num1 = int(document.getElementById("input5").value)
    num2 = int(document.getElementById("input6").value)

    display(num1 * num2, target="result")


def Division(g):
    document.getElementById("result").innerHTML = ""
    num1 = int(document.getElementById("input7").value)
    num2 = int(document.getElementById("input8").value)

    if num2 == 0:
        display("Cannot divide by zero.", target="result")
    else:
        display(num1 / num2, target="result")



