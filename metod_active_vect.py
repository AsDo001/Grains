import cv2 
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, io, img_as_float
from skimage.segmentation import active_contour
from skimage.filters import gaussian

# Загрузка и подготовка изображения
image = io.imread('CORN_WHITE.jpg')
resized_img = cv2.resize(image, (800, 800))

# Конвертация в grayscale и сглаживание
image_gray = color.rgb2gray(resized_img)  
image_smooth = gaussian(image_gray, sigma=3)  

# Инициализация начального контура
h, w = image_gray.shape
center = (w // 2, h // 2)
radius = min(h, w) // 3
theta = np.linspace(0, 2 * np.pi, 800)
init = np.array([center[0] + radius * np.cos(theta), 
                 center[1] + radius * np.sin(theta)]).T

# Применение метода активных контуров
snake = active_contour(
    image_smooth,
    init,
    alpha=0.015,     
    beta=10.0,       
    gamma=0.001,     
    max_num_iter=500  
)

# Визуализация результатов
fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(resized_img)
ax.plot(init[:, 0], init[:, 1], '--r', lw=2, label="Начальный контур")
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=2, label="Активный контур")
ax.set_title('Результат работы активного контура')
ax.legend()
plt.show()