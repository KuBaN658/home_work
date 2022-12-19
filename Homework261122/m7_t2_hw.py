"""
Задача №2
Написать функцию, которая находит все файлы заданного расширения и
перемещает их в подпапку backup относительно текущей директории.
Если папка backup есть, то мы ее используем, если нет, ее нужно создать.
"""
import os


def search_move_files(extension='py',
                      search_directory='.',
                      backup_directory='backup') -> None:
    """
    Находит все файлы заданного расширения в заданной директории и
    перемещает их в подпапку backup относительно заданной директории
    :param extension: расширение файлов
    :param search_directory: директория для поиска
    :param backup_directory: директория для перемещения файлов
    :return: None
    """
    if search_directory != '.' and search_directory != os.getcwd():
        os.chdir(search_directory)

    if not os.path.exists(backup_directory):
        os.mkdir(backup_directory)
    elif not os.path.isdir(backup_directory):
        print('Измените параметр "backup_directory", или удалите файл',
              os.path.join(os.getcwd(), backup_directory))
        return

    files = os.listdir(os.curdir)

    for i in files:
        if os.path.splitext(i)[1][1:] == extension and os.path.isfile(i):
            os.replace(i, os.path.join(backup_directory, i))


if __name__ == '__main__':
    search_move_files()
