import numpy as np

from funcs import tochka_peresecheniya as tochka
from funcs import bezier_curve as bezier


# Хорда
B = 30  # мм
# Угол в относительном движении в сечении перед рабочей лопаткой
beta_1 = 38  # градусов
# Угол в относительном движении в сечении за рабочей лопаткой
beta_2 = 34  # градусов
# Установочный угол
beta_y = 180  # - (beta_1 + beta_2)/2
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


class Blade:
    """ docsting """

    def __init__(
            self,
            B,
            beta_1,
            beta_2,
            beta_y,
            gamma_1,
            gamma_2,
            w_1,
            w_2,
            radius_1,
            radius_2
    ):
        self.B = B
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.beta_y = beta_y
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2
        self.w_1 = w_1
        self.w_2 = w_2
        self.radius_1 = radius_1
        self.radius_2 = radius_2

        self.x, self.y = None, None
        self.center_of_mass = None

        pass

    def calc(self):
        # Координаты начала построений
        x_0, y_0 = 0, 0

        # Перевод в радианы
        beta_1 = np.radians(self.beta_1)
        beta_2 = np.radians(self.beta_2)
        beta_y = np.radians(self.beta_y)
        gamma_1 = np.radians(self.gamma_1)
        gamma_2 = np.radians(self.gamma_2)

        # Координаты точки рабочего колеса на входе
        x_1 = x_0
        y_1 = y_0
        # Координаты н и угла наклона потижней точки рабочего колеса на входе с учетом скоростиока
        x_1w = x_1 + self.w_1 * np.cos(beta_1)
        y_1w = y_1 + self.w_1 * np.sin(beta_1)

        x_1radius = x_1 + self.radius_1 * np.cos(beta_1)
        y_1radius = y_1 + self.radius_1 * np.sin(beta_1)

        # Это точка l
        x_1_spinka = x_1 - self.radius_1 * np.sin(beta_1 - gamma_1 / 2)
        y_1_spinka = y_1 + self.radius_1 * np.cos(beta_1 - gamma_1 / 2)
        x_1w_spinka = x_1_spinka + self.w_1 * np.cos(beta_1 - gamma_1 / 2)
        y_1w_spinka = y_1_spinka + self.w_1 * np.sin(beta_1 - gamma_1 / 2)

        # Это точка g
        x_1_korytse = x_1 + self.radius_1 * np.sin(beta_1 + gamma_1 / 2)
        y_1_korytse = y_1 - self.radius_1 * np.cos(beta_1 + gamma_1 / 2)
        x_1w_korytse = x_1_korytse + self.w_1 * np.cos(beta_1 + gamma_1 / 2)
        y_1w_korytse = y_1_korytse + self.w_1 * np.sin(beta_1 + gamma_1 / 2)

        x_2 = x_1 - self.B * np.cos(beta_y)
        y_2 = y_1 - self.B * np.sin(beta_y)

        x_2w = x_2 + self.w_2 * np.cos(beta_2)
        y_2w = y_2 - self.w_2 * np.sin(beta_2)

        x_2radius = x_2 + self.radius_2 * np.cos(beta_2)
        y_2radius = y_2 - self.radius_2 * np.sin(beta_2)

        x_2_spinka = x_2 - self.radius_2 * np.sin(beta_2 - gamma_2 / 2)
        y_2_spinka = y_2 - self.radius_2 * np.cos(beta_2 - gamma_2 / 2)

        x_2w_spinka = x_2_spinka + self.w_2 * np.cos(beta_2 - gamma_2 / 2)
        y_2w_spinka = y_2_spinka - self.w_2 * np.sin(beta_2 - gamma_2 / 2)

        x_2_korytse = x_2 + self.radius_2 * np.sin(beta_2 + gamma_2 / 2)
        y_2_korytse = y_2 + self.radius_2 * np.cos(beta_2 + gamma_2 / 2)

        x_2w_korytse = x_2_korytse + self.w_2 * np.cos(beta_2 + gamma_2 / 2)
        y_2w_korytse = y_2_korytse - self.w_2 * np.sin(beta_2 + gamma_2 / 2)

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
            [x_1_spinka, y_1_spinka, 0],
            [x_tochka_spinka, y_tochka_spinka, 0],
            [x_2_spinka, y_2_spinka, 0],
        ]
        spinka = bezier(points_for_spinka, 50)

        points_for_korytse = [
            [x_1_korytse, y_1_korytse, 0],
            [x_tochka_korytse, y_tochka_korytse, 0],
            [x_2_korytse, y_2_korytse, 0],
        ]
        korytse = bezier(points_for_korytse, 50)

        x_1p1_spinka = x_1_spinka + self.radius_1 * np.cos(beta_1 - gamma_1 / 2)
        y_1p1_spinka = y_1_spinka + self.radius_1 * np.sin(beta_1 - gamma_1 / 2)
        x_1p3 = x_1 + 1.5 * self.radius_1 * np.cos(beta_1)
        y_1p3 = y_1 + 1.5 * self.radius_1 * np.sin(beta_1)
        x_1p2_korytse = x_1_korytse + self.radius_1 * np.cos(beta_1 + gamma_1 / 2)
        y_1p2_korytse = y_1_korytse + self.radius_1 * np.sin(beta_1 + gamma_1 / 2)
        points_for_radius1 = [
            [x_1_spinka, y_1_spinka, 0],
            [x_1p1_spinka, y_1p1_spinka, 0],
            [x_1p3, y_1p3, 0],
            [x_1p2_korytse, y_1p2_korytse, 0],
            [x_1_korytse, y_1_korytse, 0],
        ]
        radius1 = bezier(points_for_radius1, 20)

        x_2p1_spinka = x_2_spinka + self.radius_2 * np.cos(beta_2 - gamma_2 / 2)
        y_2p1_spinka = y_2_spinka - self.radius_2 * np.sin(beta_2 - gamma_2 / 2)
        x_2p3 = x_2 + 1.5 * self.radius_2 * np.cos(beta_2)
        y_2p3 = y_2 - 1.5 * self.radius_2 * np.sin(beta_2)
        x_2p2_korytse = x_2_korytse + self.radius_2 * np.cos(beta_2 + gamma_2 / 2)
        y_2p2_korytse = y_2_korytse - self.radius_2 * np.sin(beta_2 + gamma_2 / 2)
        points_for_radius2 = [
            [x_2_spinka, y_2_spinka, 0],
            [x_2p1_spinka, y_2p1_spinka, 0],
            [x_2p3, y_2p3, 0],
            [x_2p2_korytse, y_2p2_korytse, 0],
            [x_2_korytse, y_2_korytse, 0],
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
            [x_1radius, y_1radius, 0],
            [x_tochka_srednaya, y_tochka_srednaya, 0],
            [x_2radius, y_2radius, 0],
        ]
        srednaya = bezier(points_for_srednaya, 50)

        # Основные координаты
        x, y = spinka
        x, y = np.append(x, np.flip(radius1[0])), np.append(y, np.flip(radius1[1]))
        x, y = np.append(x, np.flip(korytse[0])), np.append(y, np.flip(korytse[1]))
        x, y = np.append(x, radius2[0]), np.append(y, radius2[1])
        self.x, self.y = x, y

        center_of_mass = [
            np.sum(x * np.ones(len(x))) / np.sum(np.ones(len(x))),
            np.sum(y * np.ones(len(y))) / np.sum(np.ones(len(y)))
        ]
        self.center_of_mass = center_of_mass
        x_array, y_array = x - center_of_mass[0], y - center_of_mass[1]

        self.x, self.y = x_array, y_array

        # sr_1x = srednaya[0] + self.B / 2 - center_of_mass[0]
        # sr_2x = srednaya[0] - self.B / 2 - center_of_mass[0]
        # sr_1y = srednaya[1] - center_of_mass[1]
        # sr_2y = srednaya[1] - center_of_mass[1]

        pass

    def return_coords(self):
        return [self.x, self.y]

    def return_point(self):
        # TODO
        pass


# lopatka = Blade(
#     B,
#     beta_1,
#     beta_2,
#     beta_y,
#     gamma_1,
#     gamma_2,
#     w_1,
#     w_2,
#     radius_1,
#     radius_2
# )
# lopatka.calc()

# print(lopatka.return_coords())


