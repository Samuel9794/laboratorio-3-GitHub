def criba_eratostenes(max_num):
    primos = [True] * (max_num + 1)
    primos[0], primos[1] = False, False 
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, max_num + 1, i):
                primos[j] = False
    return primos

def contar_primos(a, b, primos):
    return sum(primos[a:b+1])
max_limit = 10**7

primos = criba_eratostenes(max_limit)
num_casos = int(input())
for _ in range(num_casos):
    a, b = map(int, input().split())
    print(contar_primos(a, b, primos))
