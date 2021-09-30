def is_a_number(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Only numbers are allowed. Please, try again!")
        return False


print("#" * 15, "Beginning", "#" * 15)

result = 0
divisor = input("\nPlease, type an integer divisor: ")

while not is_a_number(divisor):
    divisor = input("Please, type an integer divisor: ")

divisor = int(divisor)

print("\n" + "#" * 7, "Middle", "#" * 7)

dividend = input("Please, type an integer dividend: ")

while not is_a_number(dividend):
    dividend = input("Type an integer dividend: ")

dividend = int(dividend)

print("\n" + "#" * 7, "Result", "#" * 7)
try:
    result = divisor / dividend
    print(f"The division result is {round(result, 2)}")
except ZeroDivisionError as zeroDivisionError:
    print("Cannot divide by 0 :(")

print("\n" + "#" * 15, "Ending", "#" * 15)
