try:
    num = int(input("Enter a number: "))  # 1
    result = 100 / num                     # 2
    print("Result is", result)             # 3
except ZeroDivisionError:                  # 4
    print("Error: You cannot divide by zero!")  # 5
except ValueError:                         # 6
    print("Error: Please enter a valid number!")  # 7
else:                                      # 8
    print("Division successful!")          # 9
finally:                                   # 10
    print("This will always run.")        # 11
