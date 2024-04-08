# Which year do you want to check?
print("enter the year :")
year = int(input())

leap_year_4 = year%4
leap_year_100 = year%100
leap_year_400 = year%400
if leap_year_4 != 0:
  print("Not leap year")
elif leap_year_4 == 0:
  if leap_year_100 !=0:
    print("Leap year")
  elif leap_year_100 == 0:
    if leap_year_400 == 0:
      print("Leap year")
    else :
      print("Not leap year")