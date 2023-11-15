# program that handles error using try and except.
# This way the program continues after an error before completing the program.
def divideBy(num):
    try:
        return 24/num
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(divideBy(2))
print(divideBy(6))
print(divideBy(0))
print(divideBy(2))
print(divideBy(8))