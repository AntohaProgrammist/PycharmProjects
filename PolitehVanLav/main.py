import numpy as np

import matplotlib.pyplot as plt

from funcs import tochka_peresecheniya as tochka
from funcs import bezier_curve as bezier

# Хорда
B = 30  # мм

# Угол в относительном движении в сечении перед рабочей лопаткой
beta_1 = 38  # градусов
# Угол в относительном движении в сечении за рабочей лопаткой
beta_2 = 34  # градусов
# Установочный угол
beta_y = 180 - (beta_1 + beta_2)

# Угол раскрытия лопатки
gamma_1 = 30  # градусов
# Угол закртия лопатки
gamma_2 = 4  # градусов

# Скорости в относительном движении перед и за рабочим колесом турбины
w_1 = 314 / 100  # м/с
w_2 = 371 / 100  # м/с

# Радиусы скргуления входной и выходной кромок
radius_1 = 0.04 * B
radius_2 = 0.01 * B

# Координаты начала построений
X, Y = 0, 0

# Перевод в радианы
beta_1 = np.radians(beta_1)
beta_2 = np.radians(beta_2)
beta_y = np.radians(beta_y)
gamma_1 = np.radians(gamma_1)
gamma_2 = np.radians(gamma_2)

# Координаты точки рабочего колеса на входе
x_1 = X
y_1 = Y
# Координаты н и угла наклона потижней точки рабочего колеса на входе с учетом скоростиока
x_1w = x_1 + w_1 * np.cos(beta_1)
y_1w = y_1 + w_1 * np.sin(beta_1)

x_1radius = x_1 + radius_1 * np.cos(beta_1)
y_1radius = y_1 + radius_1 * np.sin(beta_1)

# Это точка l
x_1_spinka = x_1 - radius_1 * np.sin(beta_1 - gamma_1 / 2)
y_1_spinka = y_1 + radius_1 * np.cos(beta_1 - gamma_1 / 2)
x_1w_spinka = x_1_spinka + w_1 * np.cos(beta_1 - gamma_1 / 2)
y_1w_spinka = y_1_spinka + w_1 * np.sin(beta_1 - gamma_1 / 2)

# Это точка g
x_1_korytse = x_1 + radius_1 * np.sin(beta_1 + gamma_1 / 2)
y_1_korytse = y_1 - radius_1 * np.cos(beta_1 + gamma_1 / 2)
x_1w_korytse = x_1_korytse + w_1 * np.cos(beta_1 + gamma_1 / 2)
y_1w_korytse = y_1_korytse + w_1 * np.sin(beta_1 + gamma_1 / 2)

x_2 = x_1 - B * np.cos(beta_y)
y_2 = y_1 - B * np.sin(beta_y)

x_2w = x_2 + w_2 * np.cos(beta_2)
y_2w = y_2 - w_2 * np.sin(beta_2)

x_2radius = x_2 + radius_2 * np.cos(beta_2)
y_2radius = y_2 - radius_2 * np.sin(beta_2)

x_2_spinka = x_2 - radius_2 * np.sin(beta_2 - gamma_2 / 2)
y_2_spinka = y_2 - radius_2 * np.cos(beta_2 - gamma_2 / 2)

x_2w_spinka = x_2_spinka + w_2 * np.cos(beta_2 - gamma_2 / 2)
y_2w_spinka = y_2_spinka - w_2 * np.sin(beta_2 - gamma_2 / 2)

x_2_korytse = x_2 + radius_2 * np.sin(beta_2 + gamma_2 / 2)
y_2_korytse = y_2 + radius_2 * np.cos(beta_2 + gamma_2 / 2)

x_2w_korytse = x_2_korytse + w_2 * np.cos(beta_2 + gamma_2 / 2)
y_2w_korytse = y_2_korytse - w_2 * np.sin(beta_2 + gamma_2 / 2)

x_tochka_spinka, y_tochka_spinka = tochka(
    [x_1_spinka, x_1w_spinka],
    [y_1_spinka, y_1w_spinka],
    [x_2_spinka, x_2w_spinka],
    [y_2_spinka, y_2w_spinka]
)

x_tochka_korytse, y_tochka_korytse = tochka(
    [x_1_korytse, x_1w_korytse],
    [y_1_korytse, y_1w_korytse],
    [x_2_korytse, x_2w_korytse],
    [y_2_korytse, y_2w_korytse]
)

points_for_spinka = [
    [x_1_spinka, y_1_spinka],
    [x_tochka_spinka, y_tochka_spinka],
    [x_2_spinka, y_2_spinka],
]
spinka = bezier(points_for_spinka, 50)

points_for_korytse = [
    [x_1_korytse, y_1_korytse],
    [x_tochka_korytse, y_tochka_korytse],
    [x_2_korytse, y_2_korytse],
]
korytse = bezier(points_for_korytse, 50)

x_1p1_spinka = x_1_spinka + radius_1 * np.cos(beta_1 - gamma_1 / 2)
y_1p1_spinka = y_1_spinka + radius_1 * np.sin(beta_1 - gamma_1 / 2)
x_1p3 = x_1 + 1.5*radius_1 * np.cos(beta_1)
y_1p3 = y_1 + 1.5*radius_1 * np.sin(beta_1)
x_1p2_korytse = x_1_korytse + radius_1 * np.cos(beta_1 + gamma_1 / 2)
y_1p2_korytse = y_1_korytse + radius_1 * np.sin(beta_1 + gamma_1 / 2)
points_for_radius1 = [
    [x_1_spinka, y_1_spinka],
    [x_1p1_spinka, y_1p1_spinka],
    [x_1p3, y_1p3],
    [x_1p2_korytse, y_1p2_korytse],
    [x_1_korytse, y_1_korytse],
]
radius1 = bezier(points_for_radius1, 20)

x_2p1_spinka = x_2_spinka + radius_2 * np.cos(beta_2 - gamma_2 / 2)
y_2p1_spinka = y_2_spinka - radius_2 * np.sin(beta_2 - gamma_2 / 2)
x_2p3 = x_2 + 1.5*radius_2 * np.cos(beta_2)
y_2p3 = y_2 - 1.5*radius_2 * np.sin(beta_2)
x_2p2_korytse = x_2_korytse + radius_2 * np.cos(beta_2 + gamma_2 / 2)
y_2p2_korytse = y_2_korytse - radius_2 * np.sin(beta_2 + gamma_2 / 2)
points_for_radius2 = [
    [x_2_spinka, y_2_spinka],
    [x_2p1_spinka, y_2p1_spinka],
    [x_2p3, y_2p3],
    [x_2p2_korytse, y_2p2_korytse],
    [x_2_korytse, y_2_korytse],
]
radius2 = bezier(points_for_radius2, 20)

# Расчёт средней линии
x_tochka_srednaya, y_tochka_srednaya = tochka(
    [x_1w, x_1],
    [y_1w, y_1],
    [x_2w, x_2],
    [y_2w, y_2]
)
points_for_srednaya = [
    [x_1radius, y_1radius],
    [x_tochka_srednaya, y_tochka_srednaya],
    [x_2radius, y_2radius],
]
srednaya = bezier(points_for_srednaya, 50)

x, y = spinka
x, y = np.append(x, np.flip(radius1[0])), np.append(y, np.flip(radius1[1]))
x, y = np.append(x, np.flip(korytse[0])), np.append(y, np.flip(korytse[1]))
x, y = np.append(x, radius2[0]), np.append(y, radius2[1])

center_of_mass = [
    np.sum(x * np.ones(len(x))) / np.sum(np.ones(len(x))),
    np.sum(y * np.ones(len(y))) / np.sum(np.ones(len(y)))
]

x_array, y_array = x-center_of_mass[0], y-center_of_mass[1]

file = open('coordinates.asc', 'w')

print('x_array = [', ', '.join(
    str(x) for x in x_array
), ']')
print('y_array = [', ', '.join(
    str(y) for y in y_array
), ']')

sr_1x = srednaya[0] + B / 2-center_of_mass[0]
sr_2x = srednaya[0] - B / 2-center_of_mass[0]
sr_1y = srednaya[1]-center_of_mass[1]
sr_2y = srednaya[1]-center_of_mass[1]

print('sr_1x = [', ', '.join(
    str(x) for x in sr_1x
), ']')
print('sr_1y = [', ', '.join(
    str(y) for y in sr_1y
), ']')

print('sr_2x = [', ', '.join(
    str(x) for x in sr_2x
), ']')
print('sr_2y = [', ', '.join(
    str(y) for y in sr_2y
), ']')

plt.plot(x, y)

plt.plot(srednaya[0], srednaya[1])
plt.plot(sr_1x, sr_1y)
plt.plot(sr_2x, sr_2y)

for x, y in zip(x_array, y_array):
    # print(x, y)
    file.write(str(x) + '\t' + str(y) + '\t' + str(0) + '\n')

file.close()

plt.plot(x, y, 'k')
plt.title('Название')
plt.xlabel('Ось ИКС')
plt.ylabel('Ось Y')
plt.grid()
plt.axis('equal')
# plt.legend()
plt.show()

b = 1
