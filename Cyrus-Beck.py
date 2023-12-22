from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from bresenham import bresenham

polygon_axes = []
dots_axes = []
# эта функция действительно поожа на функцию егора, остальное нет
def on_click(event):
    global polygon_axes, dots_axes

    if event.button == 1:
        polygon_axes.append((int(event.xdata), int(event.ydata)))
    elif event.button == 3:
        if len(dots_axes) < 2:
            dots_axes.append((int(event.xdata), int(event.ydata)))

            if len(dots_axes) == 2 and len(polygon_axes) > 2:
                process_cyrus_beck_algorithm()

def process_cyrus_beck_algorithm():
    global dots_axes, polygon_axes

    t_begin, t_end = 0, 1
    AB_vector = (dots_axes[1][0] - dots_axes[0][0], dots_axes[1][1] - dots_axes[0][1])

    for i in range(len(polygon_axes)):
        j = i - 1
        N_vector = (-(polygon_axes[i][1] - polygon_axes[j][1]), (polygon_axes[i][0] - polygon_axes[j][0]))
        Api_vector = (dots_axes[0][0] - polygon_axes[i][0], dots_axes[0][1] - polygon_axes[i][1])
        Pi = N_vector[0] * AB_vector[0] + N_vector[1] * AB_vector[1]
        Qi = N_vector[0] * Api_vector[0] + N_vector[1] * Api_vector[1]

        if Pi == 0:
            if Qi < 0:
                return "Отрезок вне многоугольника"
            continue

        t = -Qi / Pi

        if Pi > 0:
            t_begin = max(t_begin, t)
        else:
            t_end = min(t_end, t)

    if t_begin > t_end:
        return "Отрезок вне многоугольника"
    else:
        x_begin, y_begin = dots_axes[0] if t_begin == 0 else interpolate_coordinates(t_begin)
        x_end, y_end = dots_axes[1] if t_end == 1 else interpolate_coordinates(t_end)
        return x_begin, y_begin, x_end, y_end

def interpolate_coordinates(t):
    x = int(dots_axes[1][0] * t + (1 - t) * dots_axes[0][0])
    y = int(dots_axes[1][1] * t + (1 - t) * dots_axes[0][1])
    return x, y

with Image.new('RGB', (50, 50)) as image:
    image = ImageOps.flip(image)

    for x in range(0, image.width, 2):
        for y in range(0, image.height, 2):
            image.putpixel((x, y), (54, 54, 54))

    plt.imshow(image)
    plt.connect("button_press_event", on_click)
    plt.show()

    # Остальной код отображения прямой и многоугольника опущен для улучшения производительности и читаемости
