from sys import stdin,stdout

def gcdOfStrings(str1,str2):
    lista = []
    max_length = max(len(str1),len(str2))
    min_length = min(len(str1),len(str2))
    for i in range(1,max_length+1):
        if max_length % i == 0:
            lista.append(i)
    for i in lista:
        if min_length % i != 0:
            lista.remove(i)

def oned(lista,string):
    for i in range(len(string)):
        for k in lista:
            if 