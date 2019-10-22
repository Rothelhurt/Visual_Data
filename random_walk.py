from random import choice


class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        self.step = 0

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        def get_step():
            """Определяет расстояние и направление для каждого шага."""
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction * distance
            return step
        # Шаги генерируются до достижения нужной длинны.

        while len(self.x_values) < self.num_points:
            # Определение направление и длинны перемещения.
            x_step = get_step()
            y_step = get_step()
            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
