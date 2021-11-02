import math

def pitagoras(a, b):
    return math.sqrt(a*a+b*b)

def distMin(a):
    if not a:
        return -1
    else:
        distancias = []
        for i in range(0, len(a)):
            for k in range(i+1, len(a)):
                n1 = float(a[i][0] - a[k][0])
                n2 = float(a[i][1] - a[k][1])
                distancias.append(pitagoras(n1, n2))
        return min(distancias)

a = [[0.1, 4.3], [29.5, -3.2], [6.3, -2.4], [-45.2, 8.1], [3.1, 17.7]]
print(distMin(a))