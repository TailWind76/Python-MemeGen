import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def generate_meme(top_text, bottom_text, image_path):
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        width, height = image.size

        # Загрузка шрифта (указать путь к шрифту на вашей системе)
        font = ImageFont.truetype("arial.ttf", size=min(width, height) // 10)

        # Подготовка текста
        top_text = top_text.upper()
        bottom_text = bottom_text.upper()

        # Расположение текста
        text_width, text_height = draw.textsize(top_text, font=font)
        x_top = (width - text_width) // 2
        x_bottom = (width - draw.textsize(bottom_text, font=font)[0]) // 2
        y = 10

        # Добавление текста на изображение
        draw.text((x_top, y), top_text, fill="white", font=font, stroke_width=2, stroke_fill="black")
        draw.text((x_bottom, height - text_height - 10), bottom_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

        # Сохранение мема
        output_path = os.path.splitext(image_path)[0] + "_meme.png"
        image.save(output_path)
        return output_path
    except Exception as e:
        print("Ошибка: ", e)
        return None

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path.set(file_path)

def generate_and_save_meme():
    top_text = top_text_entry.get()
    bottom_text = bottom_text_entry.get()
    image = image_path.get()

    if not top_text or not bottom_text or not image:
        result_label.config(text="Заполните все поля!", fg="red")
        return

    output_path = generate_meme(top_text, bottom_text, image)
    if output_path:
        result_label.config(text=f"Мем сохранен: {output_path}", fg="green")
    else:
        result_label.config(text="Что-то пошло не так...", fg="red")

# Создание окна
root = tk.Tk()
root.title("Генератор мемов")

# Поля ввода
top_text_label = tk.Label(root, text="Текст сверху:")
top_text_label.pack()
top_text_entry = tk.Entry(root)
top_text_entry.pack()

bottom_text_label = tk.Label(root, text="Текст снизу:")
bottom_text_label.pack()
bottom_text_entry = tk.Entry(root)
bottom_text_entry.pack()

# Выбор изображения
image_path = tk.StringVar()
browse_button = tk.Button(root, text="Выбрать изображение", command=open_image)
browse_button.pack()

# Кнопка для генерации и сохранения мема
generate_button = tk.Button(root, text="Создать мем", command=generate_and_save_meme)
generate_button.pack()

# Отображение результата
result_label = tk.Label(root, text="", fg="green")
result_label.pack()

root.mainloop()
