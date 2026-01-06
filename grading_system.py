print("Enter marks abtained in 5 Subjects:")
markONE = int(input("Subject 1:"))
markTWO = int(input("Subject 2:"))
markTHREE = int(input("Subject 3:"))
markFOUR = int(input("Subject 4:"))
markFIVE  = int(input("Subject 5:"))

totalMarks = markONE + markTWO + markTHREE + markFOUR + markFIVE
avgMarks = totalMarks / 5

if avgMarks>=91 and avgMarks<=100:
    print("Your Grade is A1",avgMarks)
elif avgMarks>=81 and avgMarks<=90:
    print("Your Grade is A2", avgMarks)
elif avgMarks>=71 and avgMarks<=81:
    print("Your Grade is B1", avgMarks)
elif avgMarks>=61 and avgMarks<=71:
    print("Your Grade is B2", avgMarks)
elif avgMarks>=51 and avgMarks<=61:
    print("Your Grade is C1", avgMarks)
elif avgMarks>=41 and avgMarks<=51:
    print("Your Grade is C2", avgMarks)
else:
    print("Your Grade is F")