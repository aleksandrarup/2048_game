import random


class Game:  # Основные методы игры
    def __init__(self):
        self.field = [[0 for _ in range(4)] for _ in range(4)]  # Инициализируем поле для игры.

    def clear_fild(self) -> None:  # Создаем новое поле.
        self.field = [[0 for _ in range(4)] for _ in range(4)]

    def check_add(self) -> bool:  # Проверяем наличие доступных для хода клеток.
        for line in self.field:
            if 0 in line:
                return True
        return False

    def check_win(self) -> bool:  # Проверям победил ли игрок.
        for line in self.field:
            if 32 in line:
                return True
        return False

    def add_two(self) -> None:  # Создаем список возможных клеток для добавления двойки и добавляем её.
        list_of_moves = []
        for index_line, line in enumerate(self.field):
            for index_value, value in enumerate(line):
                if value == 0:
                    list_of_moves.append([index_line, index_value])
        place_for_add = list_of_moves[random.randint(0, len(list_of_moves) - 1)]
        self.field[place_for_add[0]][place_for_add[1]] = 2

    def tern_left(self, x=1) -> None:  # Осуществляем поворот поля против часовой стрелки на 90 градусов x раз.
        for _ in range(x):
            new_field = [[], [], [], []]
            for line in self.field:
                for index_value, value in enumerate(line):
                    new_field[(len(self.field) - 1) - index_value].append(value)
            self.field = new_field

    def merge_left(self) -> None:  # Складываем все одинаковые значения не равные 0.
        self.sort_for_merge()
        for index_line in range(4):
            for index_elem in range(3):
                if self.field[index_line][index_elem] == 0:
                    break
                if self.field[index_line][index_elem] == self.field[index_line][index_elem + 1]:
                    self.field[index_line][index_elem] *= 2
                    self.field[index_line].pop(index_elem + 1)
                    self.field[index_line].append(0)

    def merge_right(self) -> None:  # Правое слияние через повороты поля и левое слияние.
        self.tern_left(2)
        self.merge_left()
        self.tern_left(2)

    def merge_up(self) -> None:  # Верхнее слияние через повороты поля и левое слияние.
        self.tern_left()
        self.merge_left()
        self.tern_left(3)

    def merge_down(self) -> None:  # Нижнее слияние через повороты поля и левое слияние.
        self.tern_left(3)
        self.merge_left()
        self.tern_left()

    def sort_for_merge(self) -> None:  # Создаем отсортированную копию поля.
        sorted_field = [[], [], [], []]
        for index_line, line in enumerate(self.field):
            count = 0
            for value in line:
                if value == 0:
                    sorted_field[index_line].append(0)
                else:
                    sorted_field[index_line].insert(count, value)
                    count += 1
        self.field = sorted_field

    def input_play(self, input_) -> None:  # Вызываем слияние в сторону, выбранную игроком.
        if input_ == 'w':
            self.merge_up()
        if input_ == 's':
            self.merge_down()
        if input_ == 'a':
            self.merge_left()
        if input_ == 'd':
            self.merge_right()

    def show_score(self) -> int:  # Возвращающем максимальное значение на игровом поле.
        max_value = 0
        for line in self.field:
            for value in line:
                if value > max_value:
                    max_value = value
        return max_value

    @staticmethod
    def start():
        x = Game()
        print("Игра начинается")
        while x.check_add():
            x.add_two()
            x.input_play(input())
            if x.check_win():
                print('Победа!')
                break


if __name__ == '__main__':
    Game.start()