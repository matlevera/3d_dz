from PIL import Image, ImageDraw

def line_clip(segment, polygon):
    # Получение координат начала и конца отрезка
    x1, y1, x2, y2 = segment

    # Итерация по ребрам многоугольника
    for i in range(len(polygon)):
        x_start, y_start = polygon[i]
        x_end, y_end = polygon[(i + 1) % len(polygon)]

        # Вычисление вектора нормали ребра
        normal = (y_end - y_start, x_start - x_end)

        # Вычисление вектора относительной позиции начала и конца отрезка
        start_point = (x1 - x_start, y1 - y_start)
        end_point = (x2 - x_start, y2 - y_start)

        # Вычисление скалярного произведения вектора нормали и векторов относительной позиции
        start_dot = normal[0] * start_point[0] + normal[1] * start_point[1]
        end_dot = normal[0] * end_point[0] + normal[1] * end_point[1]

        # Определение положения начала и конца отрезка относительно ребра
        if start_dot < 0 and end_dot < 0:
            # Отрезок полностью находится снаружи многоугольника
            return None
        elif start_dot >= 0 and end_dot >= 0:
            # Отрезок полностью находится внутри многоугольника
            break
        else:
            # Отрезок пересекает ребро многоугольника
            intersection = (start_dot - end_dot) / (start_dot - end_dot + 1e-6)
            if start_dot < 0:
                x1 = x_start + intersection * (x1 - x_start)
                y1 = y_start + intersection * (y1 - y_start)
            else:
                x2 = x_start + intersection * (x2 - x_start)
                y2 = y_start + intersection * (y2 - y_start)

    # Возвращение отсеченного отрезка
    return [int(x1), int(y1), int(x2), int(y2)]

# Создание изображения с белым фоном
width = 500
height = 500
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Задание координат многоугольника
polygon = [(100, 100), (150, 250), (300, 200), (200, 100)]

# Задание координат отрезка
segment = (50, 200, 250, 400)

# Отсечение отрезка многоугольником
clipped_segment = line_clip(segment, polygon)

# Рисование многоугольника
draw.polygon(polygon, outline="black")

# Рисование исходного и отсеченного отрезков
draw.line(segment, fill="blue", width=2)
if clipped_segment:
    draw.line(clipped_segment, fill="red", width=2)

# Сохранение изображения
image.save("clipped_segment.png")
