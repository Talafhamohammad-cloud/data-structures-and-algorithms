v = 5
array = [1, 2, 6, 10]

def shiftarray(array, v):
  if not(type(array) == type([])):
    return 'error'
  newArr = []
  if len(array) % 2 == 0:
    n = int(len(array)/2)
  else:
    n = int(len(array)/2)+1
  newArr = array[0]+[v]
  newArr = newArr+array[len(array)]

  return newArr


print(shiftarray(array, v))
