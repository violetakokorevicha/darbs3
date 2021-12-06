def count_discount(summa):
  rez = ''
  if summa < 100:
    rez = 'Atlaidi nav pieskirsta, janomaksa vel' + str(summa)
  elif summa >= 100 and summa < 200:
    rez = 'Atlaide 5%, janomaksa vel' + str(summa * 0.95)
  else:
    rez = 'Atlaide 10%, janomaksa vel'+ str(summa * 0.9)
  return rez

summa = float(input('Ievadi summu:'))
print(count_discount(summa))

