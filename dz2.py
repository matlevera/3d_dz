from PIL import Image, ImageDraw

def draw_circle(image, center, radius, color):
    # Получаем размеры изображения
    width, height = image.size
    
    # Создаем объект для рисования
    draw = ImageDraw.Draw(image)
    
    # Вычисляем координаты границ окружности
    x1 = center[0] - radius
    y1 = center[1] - radius
    x2 = center[0] + radius
    y2 = center[1] + radius
    
    # Рисуем окружность
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            # Вычисляем расстояние от текущей точки до центра окружности
            distance = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            if distance <= radius:
                draw.point((x, y), fill=color)
    
    del draw

# Создаем новое изображение
image = Image.new("RGB", (500, 500), "white")

# Задаем параметры окружности
center = (250, 250)
radius = 100
color = (255, 255, 255) 

# Рисуем окружность на изображении
draw_circle(image, center, radius, color)

# Сохраняем изображение
image.save("circle.png", "PNG")