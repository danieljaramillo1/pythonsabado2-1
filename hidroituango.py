#ENTRADA DEL PROBLEMA

nivelAgua = int(input("dame el nivel"))

#PROCESO

if nivelAgua<20 and nivelAgua>=0:
    print(f'el nivel es muy bajo { nivelAgua}') 
elif(nivelAgua<400 and nivelAgua>=20):
    print(f'todo esta bien {nivelAgua}')
elif(nivelAgua>=400):
    print(f'nivel de agua es peligroso {nivelAgua}')
else:
    print(f'incluiste un valor negativo')

    