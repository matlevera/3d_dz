from PIL import Image, ImageDraw

def draw_line(image, start, end, color):
    # Получаем размеры изображения
    width, height = image.size
    
    # Создаем объект для рисования на изображении
    draw = ImageDraw.Draw(image)
    
    # Разбиваем координаты начала и конца на отдельные переменные
    x0, y0 = start
    x1, y1 = end
    
    # Вычисляем разницу между начальной и конечной координатами
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Определяем направление движения по оси x
    sx = 1 if x0 < x1 else -1
    
    # Определяем направление движения по оси y
    sy = 1 if y0 < y1 else -1
    
    err = dx - dy
    
    # Рисуем линию, пиксель за пикселем
    while True:
        # Устанавливаем пиксель на изображении
        draw.point((x0, y0), fill=color)
        
        # Если достигли конечной точки, выходим из цикла
        if x0 == x1 and y0 == y1:
            break
        
        # Вычисляем ошибку
        e2 = 2 * err
        
        # Перемещаемся по оси x
        if e2 > -dy:
            err -= dy
            x0 += sx
        
        # Перемещаемся по оси y
        if e2 < dx:
            err += dx
            y0 += sy
    
    # Возвращаем измененное изображение
    return image

# Создаем новое черное изображение размером 800x600
image = Image.new("RGB", (800, 600), "black")

# Задаем начальные и конечные координаты для линии
start = (100, 100)
end = (700, 500)

# Задаем цвет линии 
color = (255, 255, 255)

# Рисуем линию
image = draw_line(image, start, end, color)

# Сохраняем изображение
image.save("line.png")
