day = input("what day of the week is it?")

if day == 'saturday' or day == 'sunday':
        print("c'est le weekend!")

else:
    print("ugh, its workday")

year = input("what year were you born in?")

if not year.isnumeric():
      year = input("that isn't a number. try again plz! What year were you born in?")
year = int(year)
print(f"you were born {2025-year} years ago")