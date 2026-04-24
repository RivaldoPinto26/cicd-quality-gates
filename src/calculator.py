#simple calculator 

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
symbol = str(input("Operator: "))

if symbol == "+":
  sum = number1 + number2
  print(sum)
elif symbol == "-" :
  subt = number1 - number2
  print(subt)
elif symbol == "*" :
  mul= number1 * number2
  print(mul)
elif symbol == "/" and number2 != 0:
  div= number1 / number2
  print(div)
else:
  print("try again")