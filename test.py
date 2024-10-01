import os

def get_size(path):
    """Возвращает размер файла или директории в байтах, с обработкой исключений."""
    total_size = 0
    if os.path.isfile(path):
        try:
            total_size = os.path.getsize(path)
        except FileNotFoundError:
            print(f"Файл не найден: {path}")
        except OSError as e:
            print(f"Ошибка при чтении файла {path}: {e}")
    elif os.path.isdir(path):
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.exists(fp):  # Проверка существования файла
                        try:
                            total_size += os.path.getsize(fp)
                        except FileNotFoundError:
                            print(f"Файл не найден: {fp}")
                        except OSError as e:
                            print(f"Ошибка при чтении файла {fp}: {e}")
        except OSError as e:
            print(f"Ошибка при доступе к директории {path}: {e}")
    return total_size

def analyze_sizes():
    """Анализирует размеры файлов и директорий в текущей директории."""
    items = os.listdir('.')
    sizes = []

    for item in items:
        if os.path.exists(item):
            size = get_size(item)
            sizes.append((size, item))

    # Сортировка по убыванию размера
    sizes.sort(reverse=True, key=lambda x: x[0])

    # Вывод результатов
    for size, item in sizes:
        print(f"{size} bytes - {item}")

if __name__ == "__main__":
    analyze_sizes()
