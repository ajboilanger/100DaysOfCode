try:
    file = open(
        "c:\\Users\\AJ\\Documents\\GitHub\\100DaysOfCode\\Mosh\\6Exceptions\\4CleaningUp.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
