n = int(input())

array = []

for _ in range(n):
  inputData = input().split()
  array.append((int(inputData[0]), inputData[1]))

array = sorted(array, key=lambda x: x[0])

for i in array:
  print(i[0], i[1])