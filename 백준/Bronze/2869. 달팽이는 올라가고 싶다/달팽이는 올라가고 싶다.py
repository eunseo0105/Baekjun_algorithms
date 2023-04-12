import  math

A, B, V = input().split()
A= int(A)
B= int(B)
V= int(V)

x= (V-B)/(A-B)

print(math.ceil(x))