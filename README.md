# 🖼️ Image Processing Toolkit

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-4.7.0-brightgreen?logo=opencv" alt="OpenCV">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</div>

<p align="center">
✨ Проект демонстрирует ключевые техники обработки изображений с помощью Python
</p>

## ✨ Особенности
- **Активные контуры** - Сегментация объектов методом "змейки"
- **Детектирование граней** - Алгоритм Кэнни для выделения граней
- **Изменение размера** - Единообразное масштабирование изображений
- **Визуализация** - Сравнение оригинальных и обработанных изображений

## 📦 Предварительные требования
```bash
pip install opencv-python numpy scikit-image matplotlib
```
## 🗂️  Структура проекта
```
├── main.py              # Активные контуры
├── canny.py             # Детектирование граней
├── resize.py            # Изменение размера
├── images/              # Папка с изображениями
│   ├── CORN_WHITE.jpg   # Пример изображения
│   └── results/         # Результаты обработки
├── README.md            # Документация
└── LICENSE              # MIT Лицензия
```

## 🚀 Быстрый старт
Клонируйте репозиторий:
```bash
git clone <https://github.com/AsDo001/Grains/blob/main/README.md>
cd image-processing-project
```
Запустите обработку:
```bash
# Активные контуры
python main.py --input images/CORN_WHITE.jpg

# Детектирование граней
python canny.py --input images/CORN_WHITE.jpg

# Изменение размера
python resize.py --input images/CORN_WHITE.jpg --output images/resized.jpg
```
## 🧠 Детали реализации:
## 🔵 Активные контуры (main.py)
```bash
# Параметры алгоритма
alpha = 0.015    # Эластичность контура
beta = 10.0       # Жёсткость контура
gamma = 0.001     # Шаг эволюции
max_iterations = 500
```
## 🔶 Детектирование граней (canny.py):
```bash
edges = cv2.Canny(
    image=blurred, 
    threshold1=100,  # Нижний порог
    threshold2=200   # Верхний порог
)
```
## 🔷 Изменение размера (resize.py):
```bash
resized = cv2.resize(
    src=image, 
    dsize=(500, 500), 
    interpolation=cv2.INTER_AREA
)
```
## ⚙️ Настройка параметров:
## ⚙️ Настройка параметров

| Параметр     | Рекомендуемые значения | Описание                |
|--------------|-----------------------|-------------------------|
| alpha        | 0.01 - 0.05           | Эластичность контура    |
| beta         | 5.0 - 20.0            | Жёсткость контура       |
| threshold1   | 50 - 150              | Нижний порог Кэнни      |
| threshold2   | 150 - 250             | Верхний порог Кэнни     |

## 📌 Важные заметки:
Для сложных изображений увеличьте max_iterations

Настройте пороги Кэнни под ваши изображения

Все результаты сохраняются в папке images/results/

Поддерживаются форматы JPG, PNG, BMP

## 📜 Лицензия:
Этот проект распространяется под MIT License

<div align="center"> <p>Сделано с ❤️ используя:</p> <img src="https://img.shields.io/badge/OpenCV-FF0000?logo=opencv&logoColor=white" height="30"> <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" height="30"> <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" height="30"> </div> 



