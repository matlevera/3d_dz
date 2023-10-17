import pygame
from matplotlib import pyplot as plt

# Класс, представляющий многоугольник
class Polygon:
    def init(self, vertices):
        self.vertices = vertices

    def draw(self, screen):
        pygame.draw.polygon(screen, (0, 0, 255), self.vertices, 1)

    def clip_segment(self, start, end):
        t_min = 0
        t_max = 1
        
        dx = end[0] - start[0]
        dy = end[1] - start[1]

        for i in range(-1, len(self.vertices)-1):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[i+1]
            nx = y2 - y1
            ny = x1 - x2
            p = dx * nx + dy * ny
            q1 = (x1 - start[0]) * nx + (y1 - start[1]) * ny
            q2 = (x2 - start[0]) * nx + (y2 - start[1]) * ny

            if p == 0 and q1 < 0 and q2 < 0:
                return None, None
            if p == 0:
                continue

            t = q1 / p

            if p > 0:
                if t > t_max:
                    return None, None
                t_min = max(t_min, t)
            else:
                if t < t_min:
                    return None, None
                t_max = min(t_max, t)
        
        xA = start[0] + t_min * dx
        yA = start[1] + t_min * dy
        xB = start[0] + t_max * dx
        yB = start[1] + t_max * dy

        return (xA, yA), (xB, yB)

# Инициализация Pygame
pygame.init()

# Создание экрана Pygame
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clipping Algorithm')

# Создание объекта многоугольника
polygon_vertices = [(100, 100), (250, 50), (400, 100), (450, 250), (400, 400), (250, 450), (100, 400), (50, 250)]
polygon = Polygon(polygon_vertices)

# Отображение экрана с использованием Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
plt.show()

# Отслеживание координат отрезка
xA, yA, xB, yB = None, None, None, None

# Функция обработки событий мыши
def on_click(event):
    global xA, yA, xB, yB
    if event.button == 1:
        if xA is None and yA is None:
            xA, yA = event.xdata, event.ydata
        elif xB is None and yB is None:
            xB, yB = event.xdata, event.ydata
            # Отсекаем отрезок
            segment_start = (xA, yA)
            segment_end = (xB, yB)
            clipped_start, clipped_end = polygon.clip_segment(segment_start, segment_end)
            if clipped_start is not None and clipped_end is not None:
                pygame.draw.line(screen, (255, 0, 0), clipped_start, clipped_end, 2)
                pygame.display.flip()
            xA, yA, xB, yB = None, None, None, None

# Основной цикл
running = True
while running:
    screen.fill((255, 255, 255))
    polygon.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == plt.events.ButtonRelease:
            on_click(event)
