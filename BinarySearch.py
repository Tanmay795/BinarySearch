import sys

def search(list, target):
  min = 0
  max = len(list)-1
  avg = (min+max)/2
  while (min < max):
    if (list[avg] == target):
      return avg
    elif (list[avg] < target):
      return search(list[avg+1:], target)
    else:
      return search(list[:avg-1], target)

  print ("The location of the number in the array is", avg)


def main():

  number = int(input("Please enter a number you want to search in the array !"))
  index = int(number)
  list = [24,26,28,30,32,34,36,40,42,44]
  print ("The list to search from", list)

  print(search(list, index))

if __name__ == '__main__':
  main()
