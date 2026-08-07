# ==============================================================================
# INTERMEDIATE PYTHON: Loop Control Statements (break and continue)
# ==============================================================================

# 1. Using 'break' to stop the loop when target number 5 is found
numbers = [1, 3, 5, 7, 9, 11]

for num in numbers:
    print("Checking number:", num)
    if num == 5:
        print("--> Target number 5 found! Stopping loop.")
        break

print("Loop exited successfully.")


# 2. Using 'continue' to skip even numbers and print odd numbers
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print("Odd Number:", num)


# 3. Using 'continue' to skip specific items ("Bad-Apple")
fruits = ["Apple", "Bad-Apple", "Mango"]

for fruit in fruits:
    if fruit == "Bad-Apple":
        continue
    print("Eating:", fruit)
