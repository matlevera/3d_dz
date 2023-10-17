from PIL import Image

def fill_polygon(image, polygon, color):
    width, height = image.size
    pixels = image.load()

    # Получение границ многоугольника
    min_x = min(polygon, key=lambda point: point[0])[0]
    max_x = max(polygon, key=lambda point: point[0])[0]
    min_y = min(polygon, key=lambda point: point[1])[1]
    max_y = max(polygon, key=lambda point: point[1])[1]

    # Создание массива для хранения пересечений ребер с горизонтальными линиями
    intersections = [[] for _ in range(height)]

    # Перебор всех ребер многоугольника
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        # Игнорирование горизонтальных ребер
        if y1 == y2:
            continue

        # Вычисление координаты x пересечения ребра с горизонтальной линией
        if y1 < y2:
            y_start, y_end = y1, y2
            x_start, x_end = x1, x2
        else:
            y_start, y_end = y2, y1
            x_start, x_end = x2, x1

        for y in range(y_start, y_end + 1):
            x = round((y - y_start) * (x_end - x_start) / (y_end - y_start) + x_start)
            intersections[y].append(x)

    # Закрашивание многоугольника
    for y in range(min_y, max_y + 1):
        intersections[y].sort()
        for i in range(0, len(intersections[y]), 2):
            x_start = max(min_x, intersections[y][i])
            x_end = min(max_x, intersections[y][i + 1])

            for x in range(x_start, x_end + 1):
                pixels[x, y] = color

# Создание изображения с белым фоном
width = 500
height = 500
image = Image.new("RGB", (width, height), "white")

# Задание координат многоугольника
polygon = [(100, 100), (200, 200), (300, 150)]

# Закрашивание многоугольника
fill_polygon(image, polygon, (0, 255, 0))

# Сохранение изображения
image.save("filled_polygon.png")
