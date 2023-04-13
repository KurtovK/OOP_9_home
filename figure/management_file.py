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