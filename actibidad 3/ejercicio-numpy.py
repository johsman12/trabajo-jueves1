import numpy as np

notas = np.array(
                [3.5,4.0, 2.2, 5.0],[4.4, 5.0, 3.0, 3.0],[5.0, 3.8, 4.6, 4.0])

print(notas.mean(axis=0)) 
print(notas.shape)
print(notas[0])
print(notas[:,1])