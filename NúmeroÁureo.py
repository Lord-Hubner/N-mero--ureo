import csv
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import math

# def GoldenNumberByNFractions(n: int) -> Decimal:
#     getcontext().prec = 39
#     number = Decimal(1)
   
#     number += Decimal(1) / GetNextDivision(n, 1)

#     return number

# def GetNextDivision(n: int, k: int) -> Decimal:
#     if k < n:
#         return Decimal(1) + (Decimal(1) / GetNextDivision(n, k + 1))
    
#     return Decimal(1)

# results = {}
# goldenNumber = Decimal('1.6180339887498948482045868343656381177')

# with open('ResultadosFractions.csv', 'w', newline='') as resultados:
#     writer = csv.writer(resultados, delimiter=',')
#     correctDecimals = 0
#     relevantNumberIndex = 1

#     #Pula até a primeira casa decimal
#     relevantNumberResult = '6'
#     relevantNumberGolden = '6'

#     for it in range(3,900):
#         result = GoldenNumberByNFractions(it)

#         relevantNumberResult = format(result, '.37f').replace('.','')[relevantNumberIndex]
        
#         if relevantNumberResult == relevantNumberGolden:
#             results[correctDecimals] = it
#             correctDecimals = correctDecimals + 1
#             writer.writerow([correctDecimals, it])

#             relevantNumberIndex = relevantNumberIndex + 1
#             if relevantNumberIndex > 37:
#                 break
#             relevantNumberGolden = format(goldenNumber, '.37f').replace('.','')[relevantNumberIndex]


# keys = [a for a in results.keys()]
# values = [a for a in results.values()]
# fig, ax = plt.subplots(1,1)

#fig.set_size_inches(10, 10)

# ax.plot(results.keys(), results.values(), marker='o')
# ax.set_xticks(keys)
# ax.set_yticks(values)
# plt.show()


# def GoldenNumberByNRoots(n : int) -> Decimal:
#     getcontext().prec = 39
#     number = Decimal(1)

#     return (number + GetNextRoot(n, 1))**Decimal(1/2)


# def GetNextRoot(n : int, k : int) -> Decimal:
#     if k < n:
#         return (Decimal(1) + GetNextRoot(n, k+1))**Decimal(1/2)

#     return Decimal(1)


# teste = GoldenNumberByNRoots(2)
# bah = 2


# with open('ResultadosRoots.csv', 'w', newline='') as resultados:
#     writer = csv.writer(resultados, delimiter=',')
#     correctDecimals = 0
#     relevantNumberIndex = 1

#     #Pula até a primeira casa decimal
#     relevantNumberResult = '6'
#     relevantNumberGolden = '6'

#     results = {}
#     goldenNumber = Decimal('1.6180339887498948482045868343656381177')

#     for it in range(4,900):
#         result = GoldenNumberByNRoots(it)

#         relevantNumberResult = format(result, '.37f').replace('.','')[relevantNumberIndex]
        
#         if relevantNumberResult == relevantNumberGolden:
#             results[correctDecimals] = it
#             correctDecimals = correctDecimals + 1
#             writer.writerow([correctDecimals, it])

#             relevantNumberIndex = relevantNumberIndex + 1
#             if relevantNumberIndex > 37:
#                 break
#             relevantNumberGolden = format(goldenNumber, '.37f').replace('.','')[relevantNumberIndex]

# keys = [a for a in results.keys()]
# values = [a for a in results.values()]
# fig, ax = plt.subplots(1,1)

# fig.set_size_inches(10, 10)

# ax.plot(results.keys(), results.values(), marker='o')
# ax.set_xticks(keys)
# ax.set_yticks(values)
# plt.show()


#Fibonnaci em que todo enésimo número está na casa n-1
#Limitação: números negativos de g retornam 1 (por que vc faria isso?)
def ZangõesFibonnaci(g : int) -> int:
    return GetNext(g, 1, 1)

def GetNext(g, a, b) -> int:
    if g <= 1:
        return b
    return GetNext(g-1, b, a+b)

getcontext().prec = 39

results = {}
goldenNumber = Decimal('1.6180339887498948482045868343656381177')

correctDecimals = 1
relevantNumberGolden = '6'
relevantNumberIndex = 1

fibonacci = list()
fibonacci.append(ZangõesFibonnaci(0))

lastFibo = ZangõesFibonnaci(0)

for it in range(1,100):
    currentFibo = ZangõesFibonnaci(it)
    division = Decimal(currentFibo) / Decimal(lastFibo)
    fibonacci.append(currentFibo)

    relevantNumberResult = format(division, '.37f').replace('.','')[relevantNumberIndex]
    
    if relevantNumberResult == relevantNumberGolden:
        results[correctDecimals] = it
        correctDecimals = correctDecimals + 1

        relevantNumberIndex = relevantNumberIndex + 1
        if relevantNumberIndex > 37:
            break
        relevantNumberGolden = format(goldenNumber, '.37f').replace('.','')[relevantNumberIndex]
    
    lastFibo = currentFibo

# for it in range(1,100):
#     fibonacci.append(ZangõesFibonnaci(it))
#     resultados[it] = Decimal(fibonacci[it]) / Decimal(fibonacci[it-1])



x = [a for a in results.keys()]
y = [a for a in results.values()]

#Gráfico fibonacci[n]/fibonacci[n-1]
plt.plot(x, y, marker='o', color='#d9fa1e')
plt.xticks(x)
plt.yticks(y)
plt.title('Casas decimais corretas da divisão de elementos sequenciais da sequência de Fibonacci em relação ao número áureo')
plt.xlabel('Enésima casa decimal')
plt.ylabel('Número de iterações')

plt.gcf().set_size_inches(15, 10)
plt.gcf().subplots_adjust(bottom=0.1)
plt.gcf().text(0.1, 0.04, 'Obs: a sequência de Fibonacci aqui tem os elementos', color='red')
plt.gcf().text(0.15, 0.025, 'movidos uma casa para trás', color='red')
plt.show()

#Gráfico x=número na sequência y=valor

plt.plot([a for a in range(len(fibonacci))], fibonacci, marker='o', color='#77e610')
plt.title('Número por posição na sequência de Fibonacci')
plt.xlabel('Enésima casa decimal')
plt.ylabel('Número')
plt.show()



