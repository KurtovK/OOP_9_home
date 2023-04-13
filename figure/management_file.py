class FigureManagementFile:
    FIGURE_SET = {"Square", "Circle", "Rectange", "Ellipse"}
    def write_in_file(self, path: str) -> None:
        """
        Записывает данные в .txt файл
        :param path (str): Путь до файла и название с расширением
        """
        with open(path, "w", encoding="UTF-8") as file:
            file.write(self.__class__.__name__ + "\n")
            for value in self.__dict__.values():
                file.write(str(value) + "\n")

    @classmethod
    def read_from_file(cls, path: str):
        """
        Определяет, каким методом воспользоваться для чтения файла.
        :param path (str): Путь до файла и название с расширением
        :return:
                Объект фигура, считанная из файла
        """
        with open(path, "r", encoding="UTF-8") as file:
            class_name = file.readline().strip()
        if class_name == "Square":
            return cls.__read_square_from_file(path)
        elif class_name == "Circle":
            return cls.__read_circle_from_file(path)
        elif class_name == "Rectangle":
            return cls.__read_rectangle_from_file(path)
        elif class_name == "Ellipse":
            return cls.__read_ellipse_from_file(path)
        else:
            raise Exception("В файл записаны данные неизвестной фигуры")