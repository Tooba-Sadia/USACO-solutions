#Link -> https://dmoj.ca/problem/ac20p1
#Acute Triangle ->  a^2 + b^2 > c^2
#Obtuse Triangle -> a^2 + b^2 < c^2
#Right Triangle -> a^2 + b^2 = c^2
T = int(input())
for i in range(T):
  triangle = list(map(int,input().split()))
  triangle.sort() # sorting so l3 is always the largest
  l1,l2,l3 = triangle
  if l1**2 + l2**2 > l3**2:
    print("A")
  elif l1**2 + l2**2 < l3**2:
    print("O")
  elif l1**2 + l2**2 == l3**2:
    print("R")