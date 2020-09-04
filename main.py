temp = float (input('Enter temperature: '))
unit = str (input('Enter unit in F/f or C/c: '))
newtemp = float
unitdet = 0
if unit == "F":
  unitdet = 1
elif unit == "f":
  unitdet = 1
elif unit == "C":
  unitdet = 2
elif unit == "c":
  unitdet = 2
if unitdet == 0:
  print('Invalid unit(%s).'% unit)
if unitdet == 2:
  newtemp = ((temp*(9/5)+32))
  print(str(temp)+"\N{DEGREE SIGN}",'in Celsius is equivalent to',str(newtemp)+"\N{DEGREE SIGN}",'Fahrenheit.')

elif unitdet == 1:
  newtemp = ((temp-32)/1.8)
  print(str(temp)+"\N{DEGREE SIGN}",'in Fahrenheit is equivalent to',str(newtemp)+"\N{DEGREE SIGN}",'Celsius.')

