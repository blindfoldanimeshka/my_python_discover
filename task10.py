print("Calc")

x = float(input("Pervoe 4islo"))
y = float(input("Vtoroe 4islo"))

operation = input("Какая опера вас интересует?: (+, -, *, /)")

if operation =="+":
    print("Слага")
    result = x+y

elif operation =="-":
    print("Вычитание")
    result = x-y

elif operation =="/":
    print("Delenie")
    result = x/y

elif operation =="*":
    print("Умножение")
    result = x*y

else:
    print("Che eto?")
    result=None

if result is not None:
    print("Че получилось:", result)