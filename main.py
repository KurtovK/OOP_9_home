from figure_tools.figures import Square, Ellipse, Circle, Rectangle
#Задание 1.
#Создайте базовый класс Shape для хранения плоских фигур.
#Определите производные классы:
#Square — квадрат, который характеризуется координатами левого
#верхнего угла и длиной стороны;
#Rectangle — прямоугольник с заданными координатами верхнего
#левого угла и размерами;
#Circle — окружность с заданными координатами цен-тра и радиусом;
#Ellipse — эллипс с заданными координатами верхнего угла описанного
#вокруг него прямоугольника со сторонами, параллельными осям координат,
#и размерами этого прямоугольника.
#Создайте список фигур. Определите класс, который сохраняет фигуры
#в файлы, загружает из файла и отобразите информацию о каждой из фигур.


def execute_application():
    print("Фигуры для записи в файлы: \n")

    square = Square(5, 3, 34)
    square.info()

    circle = Circle(0, 2, 42)
    circle.info()

    ellipse = Ellipse(7, 1, 12, 78.9)
    ellipse.info()

    rectangle = Rectangle(9, 9, 5.6, 23.5)
    rectangle.info()

    figure_list = [square, circle, ellipse, rectangle]

    for num, item in enumerate(figure_list):
        path = str(num) + "_" + item.__class__.__name__
        item.write_in_file(path)

    print("Фигуры считанные из файлов:\n")

    path_square = "square.txt"
    square_from_file = Square.read_from_file(path_square)
    square_from_file.info()

    path_circle = "circle.txt"
    circle_from_file = Circle.read_from_file(path_circle)
    circle_from_file.info()

    path_rectangle = "rectangle.txt"
    rectangle_from_file = Rectangle.read_from_file(path_rectangle)
    rectangle_from_file.info()

    path_ellipse = "ellipse.txt"
    ellipse_from_file = Ellipse.read_from_file(path_ellipse)
    ellipse_from_file.info()





if __name__=="__main__":
    execute_application()