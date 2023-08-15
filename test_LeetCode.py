import sys
def addTwoNumbers(self,l1,l2):
    l1 = l1[::-1]
    l2 = l2[::-1]
    linea = ''
    lineb = ''
    for i in l1:
        linea += str(i)
    for i in l2:
        lineb += str(i)
    number = int(linea) + int(lineb)
    lista = list(reversed(list(str(number))))
    return lista

l1 = list(map(int,sys.stdin.readline().split(',')))
l2 = list(map(int,sys.stdin.readline().split(',')))
print(addTwoNumbers('self',l1,l2))

