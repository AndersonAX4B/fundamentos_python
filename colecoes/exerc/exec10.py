"""
Média de valores usando as libs statistics e numpy e matemática

"""
import numpy
import statistics

notas = []

for nota in range(15):
    notas.append(nota)

# Matemática
media = sum(notas) / len(notas)
print(media)

# Usando Numpy
numpyMean = numpy.mean(notas)
print(numpyMean)

# Usando statistics
statisticsMean = statistics.mean(notas)
print(statisticsMean)
