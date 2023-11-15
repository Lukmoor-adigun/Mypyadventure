import sys
count = 0
while (count < 3):
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        count = count + 1
        print(count)
        tries_count = (count - 3) * -1
        print('You have ' + str(tries_count) + ' More tries left')
print('Sorry you have no tries left.')