from PIL import Image

def sobel_filter(image):
    # Преобразование изображения в оттенки серого
    grayscale = image.convert('L')

    # Получение размеров изображения
    width, height = grayscale.size

    # Создание массивов для хранения градиентов по горизонтали и вертикали
    gradient_x = [[0 for _ in range(height)] for _ in range(width)]
    gradient_y = [[0 for _ in range(height)] for _ in range(width)]

    # Определение матриц для фильтра Собеля
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Вычисление градиентов по горизонтали и вертикали
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            # Вычисление градиента по горизонтали
            pixel_values = [
                grayscale.getpixel((x-1, y-1)),
                grayscale.getpixel((x-1, y)),
                grayscale.getpixel((x-1, y+1)),
                grayscale.getpixel((x+1, y-1)),
                grayscale.getpixel((x+1, y)),
                grayscale.getpixel((x+1, y+1))
            ]
            gradient_x[x][y] = sum([sobel_x[i][j] * pixel_values[i] for i in range(3) for j in range(3)])

            # Вычисление градиента по вертикали
            gradient_y[x][y] = sum([sobel_y[i][j] * pixel_values[i] for i in range(3) for j in range(3)])

    # Создание изображения с нулевыми значениями пикселей
    filtered_image = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    filtered_pixels = filtered_image.load()

    # Вычисление суммарного градиента и обновление пикселей
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            gradient = int((gradient_x[x][y]**2 + gradient_y[x][y]**2)**0.5)
            filtered_pixels[x, y] = (gradient, gradient, gradient, 255)

    # Возвращение результирующего изображения
    return filtered_image

# Загрузка изображения
image = Image.open('image.jpg')

# Применение фильтра Собеля
filtered_image = sobel_filter(image)

# Сохранение результирующего изображения
filtered_image.save('sobel_filtered_image.png')
