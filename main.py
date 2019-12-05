import csv
from colorama import Fore, Back, Style
from colorama import init

init()

qnum = 1
ques = []
answ1 = []
answ2 = []
answ3 = []
correct_answers = []

coin = []
 
with open("vop.csv", newline='') as pythontext:
  reader = csv.reader(pythontext, delimiter = ';')
  for row in reader:
    ques.append(row[0])
    answ1.append(row[1])
    answ2.append(row[2])
    answ3.append(row[3])
    correct_answers.append(row[4])

while qnum < len(ques):
  print( Fore.CYAN )
  print(ques[qnum])
  print( Fore.WHITE )
  print(answ1[qnum])
  print(answ2[qnum])
  print(answ3[qnum])
  print( Fore.YELLOW )
  option = input("    Выберите вариант ответа>>> ")

  if option == 'a':
    if answ1[qnum] == correct_answers[qnum]:
      print( Fore.GREEN )
      print("\n                    Правильно!")
      coin.append(5)
    else:
      print( Fore.RED )
      print("\n                    Неправильно!!!")
  elif option == 'b':
    if answ2[qnum] == correct_answers[qnum]:
      print( Fore.GREEN )
      print("\n                    Правильно!")
      coin.append(5)
    else:
      print( Fore.RED )
      print("\n                    Неправильно!!!")
  elif option == 'c':
    if answ3[qnum] == correct_answers[qnum]:
      print( Fore.GREEN )
      print("\n                    Правильно!")
      coin.append(5)
    else:
      print( Fore.RED )
      print("\n                    Неправильно!!!")
  else:
    print( Fore.RED )
    print("         Вариант такого ответа нет!!!!!!")

  qnum += 1

totalscore = sum(coin)
print( Fore.WHITE )
print("Вы набрали " + str(totalscore) + " баллов)")


if totalscore == 100:
  print( Fore.GREEN )
  print("Ваша оценка 'A'")
elif totalscore == 95:
  print( Fore.BLUE )
  print("Ваша оценка '+B'")
elif totalscore == 90:
  print( Fore.BLUE )
  print("Ваша оценка 'B'")
elif totalscore == 85:
  print( Fore.BLUE )
  print("Ваша оценка '-B'")
elif totalscore == 80:
  print( Fore.BLUE )
  print("Ваша оценка '+C'")
elif totalscore == 75:
  print( Fore.YELLOW )
  print("Ваша оценка 'C'")
elif totalscore == 70:
  print( Fore.YELLOW )
  print("Ваша оценка '-C'")
elif totalscore == 65:
  print( Fore.MAGENTA )
  print("Ваша оценка 'D'")
elif totalscore == 60:
  print( Fore.MAGENTA )
  print("Ваша оценка '-D'")
else:
  print( Fore.RED )
  print("Ваша оценка 'F'\n поздравляю)")