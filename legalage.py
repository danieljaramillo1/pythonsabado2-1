age = int(input("dame tu edad"))

if age<0:
    print(f'que me estas contando? ingresas edad real')
elif age>=0 and age <=14:
    print(f'eres un niño')
elif age>14 and age <=28:
    print(f'eres un joven')
elif age>28 and age <=60:
    print(f'eres un adulto')
elif age>60 and age <=120:
    print(f'eres un anciano')
else:
    print(f'que me estas contando?')

