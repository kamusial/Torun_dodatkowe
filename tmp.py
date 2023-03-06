import datetime

nazwa = 'screen0.png'

if nazwa[6] == 0:
    nazwa = 'screen1.png'
print(nazwa[6])

teraz = datetime.datetime.now()
nazwa = teraz.strftime('Aktualny czas to .... %H_%M_%S .....')

print(nazwa)

