# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21,

import math

coord = ['X', 'Y']
coord_1 = []
coord_2 = []

for i in range(len(coord)):
    coord_1.append(int(input(f'Введите координату {coord[i]} первой точки: ')))
for i in range(len(coord)):
    coord_2.append(int(input(f'Введите координату {coord[i]} второй точки: ')))

result = math.sqrt((coord_2[0] - coord_1[0]) ** 2 + (coord_2[1] - coord_1[1]) ** 2)
print(f'Расстояние между точками равно: {round(result, 2)}')
