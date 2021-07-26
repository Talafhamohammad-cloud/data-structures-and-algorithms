
array = []
n=int(input("enter the number of elements"))
for i in range(n):
    numbers=int(input("enter the number"))
    array.append(numbers)
else: print('you are done')
print(f'your array is {array}')
print(f'your reversed array is {array[::-1]} ')

