month = input("dame el mes")
monthlow = month.lower

if monthlow == "january" or monthlow == "february" or monthlow == "march":
    print(f'{month} es temporada de winter')
elif monthlow == "april" or monthlow == "may" or monthlow == "june":
    print(f'{month} es temporada de spring')
elif monthlow == "july" or monthlow == "agust" or monthlow == "septeber":
    print(f'{month} es temporada de summer')
elif monthlow == "october" or monthlow == "november" or monthlow == "december":
    print(f'{month} es temporada de fall')
else:
    print(f'no es un mes valido')