import calendar


def cal_month():
  print("[*] Use 2 Digits to represent the Month\r\n[*] i.e 01 for January")
  yy = int(input("[*] Enter the Year for the Calendar: "))

  mm = int(input("[*] Month for the Calendar (number): "))
  print(calendar.month(yy, mm))


choice = int(input("[*] 1. If you would like to print a calendar for a certain month \n[*] 2. If you would like to "
                   "print another calendar\n Enter Choice: "))

if choice == 1:
  cal_month()
elif choice == 2:
  term = print("Not done yet")
else:
  ValueError
