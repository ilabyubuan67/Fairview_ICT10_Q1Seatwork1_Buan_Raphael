from pyscript import document, display


# 

a = "Student Name: Raphael Buan"
b = "Age: 15"
height1 = "Height: 165cm"
_Countries3 = "Countries I want to visit: Canada, South Korea, America"
student_type = "Are you a student?: True"
#Dict
_things3 = {"Shoe Brand: Nike", "Car Brand: Tesla", "Best Friend: Dustin"}
#Set
fruit5 = ({"Apple": "Grapes", "Oranges": "Banana", "Mangoes": "Pineapple"})
#tuple
_Sevendays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


display((a))
display((b))
display((height1))
display((student_type))
display(( _Countries3))
display(( _things3))
display((fruit5))
display((_Sevendays))

def Add(g):
    document.getElementById("result").innerHTML = ""
    a = int(document.getElementById("input1").value)
    b = int(document.getElementById("input2").value)
    result1 = a + b

    display(result1, target="result")

    def Subtraction(g):
    document.getElementById("result").innerHTML = ""
    c = int(document.getElementById("input3").value)
    d = int(document.getElementById("input4").value)
    result1 = c - d

    display(result1, target="result")

    def Multiply(g):
    document.getElementById("result").innerHTML = ""
    e = int(document.getElementById("input5").value)
    f = int(document.getElementById("input6").value)
    result1 = e * f

    display(result1, target="result")

    def Division(g):
    document.getElementById("result").innerHTML = ""
    a = int(document.getElementById("input7").value)
    b = int(document.getElementById("input8").value)
    result1 = a / b
    display(result1, target="result")



