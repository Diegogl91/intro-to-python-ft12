# loops

# for in
# while

nombres = ["Luis", "Miguel", "Juan"]
for i in range(1, 11): # start, stop, step
    print(i)

for i in range(0, len(nombres)): # start, stop, step
    print(nombres[i])

for valor in nombres:
    print(valor)

i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 0
while i < len(nombres):
    print(nombres[i]) 
    i = i + 1