class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __radd__(self, number):
        if type(number) is not int:
            return NotImplemented
        return Coord(self.x + number, self.y + number)

    def get_xy(self):
        return self.x, self.y


def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Помилка! Введіть ціле число.")


def main():
    x = input_int("Введіть X (1-10): ")
    y = input_int("Введіть Y (1-10): ")

    while not (1 <= x <= 10 and 1 <= y <= 10):
        print("Координати мають бути від 1 до 10.")
        x = input_int("Введіть X (1-10): ")
        y = input_int("Введіть Y (1-10): ")

    point = Coord(x, y)

    while True:
        number = input_int("Введіть ціле число для додавання (0 – вихід): ")

        if number == 0:
            break

        result = number + point
        rx, ry = result.get_xy()

        if 1 <= rx <= 10 and 1 <= ry <= 10:
            point = result
            print(f"Нові координати: X = {rx}, Y = {ry}")
        else:
            print("Помилка! Картка вийде за межі поля.")

    print("Програму завершено.")


if __name__ == "__main__":
    main()
