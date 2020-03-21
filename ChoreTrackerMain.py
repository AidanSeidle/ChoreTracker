chores = []
valchores = []
children = ["Aidan", "Brynn", "Emery"]

aidantot = [0]
brynntot = [0]
emerytot = [0]
values = [aidantot, brynntot, emerytot]

run = 0
i = 0

while run != 1:

  action = input("Completed Chore = 1, Add Chore = 2, List Chores = 3, Check Balances = 4: ")

#completed chore
  if int(action) == 1:
    child = int(input("Aidan = 1, Brynn = 2, Emery = 3: "))
    for i in chores, valchores:
      print(i)
    selchore = chores.index(input("Name of Chore: "))
    if child == 1:
      aidantot[0] = int(aidantot[0]) + int(valchores[selchore])
    if child == 2:
      brynntot[0] = int(brynntot[0]) + int(valchores[selchore])
    if child == 3:
      emerytot[0] = int(emerytot[0]) + int(valchores[selchore])

#add chores
  elif int(action) == 2:
    chores.append(input("New Chore: "))
    valchores.append(input("Value: "))
    for i in chores, valchores:
      print(i)

#list chores
  elif int(action) == 3:
    for i in chores, valchores:
      print(i)

#check balances
  elif int(action) == 4:
    for i in children, values:
      print(i)
