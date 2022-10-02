size = int(input("Please enter any number"))

for row in range(0, size):
  for col in range(0,size):
    if (row + col == size-1):
      print("1 ", end=" ")
    else:
      print("0 ", end=" ")
  print()