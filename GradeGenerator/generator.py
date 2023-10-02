from random import randrange

aNote = "A"          # 85 - 100
aMinusNote = "A-"    # 80 - 84
bPlusNote = "B+"     # 75 - 79
bNote = "B"          # 70 - 74
bMinusNote = "B-"    # 66 - 69
cPlusNote = "C+"     # 63 - 65
cNote = "C"          # 59 - 62
cMinusNote = "C-"    # 56 - 58
dPlusNote = "D+"     # 53 - 55
dNote = "D"          # 50 - 52
dMinusNote = "D-"    # 35 - 49
fNote = "F"          # 0 - 34
ngNote = "NG"        # Attendance Problem

differentclassNote = 0

midtermNote = int(input("Midterm Note: "))
finalNote = int(input("Final Note: "))
homeworkNote = int(input("Homework or More Note: "))

totalNote = midtermNote + finalNote + homeworkNote

if totalNote > 100:
  print("Do you get a higher score than 100 seriously? no one has the intelligence you have!")
elif 100 >= totalNote >= 85:
  print(aNote)
elif 84 >= totalNote >= 80:
  print(aMinusNote)
elif 79 >= totalNote >= 75:
  print(bPlusNote)
elif 74 >= totalNote >= 70:
  print(bNote)
elif 69 >= totalNote >= 66:
  print(bMinusNote)
elif 65 >= totalNote >= 63:
  print(cPlusNote)
elif 62 >= totalNote >= 59:
  print(cNote)
elif 58 >= totalNote >= 56:
  print(cMinusNote)
elif 55 >= totalNote >= 53:
  print(dPlusNote)
elif 52 >= totalNote >= 50:
  print(dNote)
elif 49 >= totalNote >= 35:
  print(dMinusNote)
elif 34 >= totalNote >= 0:
  print(fNote)
else:
  print("You will repeat the course due to absenteeism")


totalNote = round((differentclassNote + totalNote)/25)

print(totalNote)

if  4 >= totalNote > 3.5: 
  print("You are eligible to become a high honor student")
elif 3.5 > totalNote > 3: 
    print("You are entitled to be an honor student")
elif  3 > totalNote > 2: 
  print("Qualified to graduate")
elif  2 > totalNote > 1.8: 
  print("Passed but after to be tested")
elif  1.8 > totalNote > 1: 
  print("Department period repeat")
elif  1 > totalNote: 
  print("Compulsory department change")


