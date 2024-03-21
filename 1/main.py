import tkinter as tk #импортируем tkinter и присваеваем ему псевдоним
import math
from tkinter import messagebox, filedialog
from tkinter import *
#filedialog предоставляет функции для работы с диалоговыми окнами выбора файла


def calculate():
    #получаем значения радиуса, высоты и плотности из текстовых полей с помощью get и преобразовываем в число с плавающей точкой
    #используем try для проверки на ошибки
    try:
        radius = float(radius_entry.get())
        height = float(height_entry.get())
        density = float(density_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод! Нужно вводить только положительные числа.")
        return

    #определяем выбранный вариант вычислений (объём, масса или площадь поверхности). Далее будет прописано, что по умолчанию всегда будет выбран объем
    selected_calculation = var.get()

    try:
        #config изменяет свойства виджета в библиотеке tkinter. Он вызывается для изменения текста, отображаемого в метке result_label
        if selected_calculation == 1:  #объём
            volume = math.pi * radius * radius * height / 3
            result_label.config(text=f"Объём конуса: {volume}")
        elif selected_calculation == 2:  #масса
            mass = (math.pi * radius**2 * height / 3) * density
            result_label.config(text=f"Масса конуса: {mass}")
        elif selected_calculation == 3:  #площадь поверхности
            surface_area = math.pi * radius * (radius + (radius ** 2 + height ** 2) ** 0.5)
            result_label.config(text=f"Площадь поверхности конуса: {surface_area}")
        else:
            #в ином случае не выбран вариант вычислений(в нашем случае он выбран всегда)
            messagebox.showwarning("Ошибка", "Выберите вариант вычислений!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при вычислениях: {str(e)}")

def save_results():
    #открываем диалог выбора файла для сохранения данных и результатов вычислений
    #первый аргумент передает разрешение файла по умолчанию, если пользователь не выбрал
    #второй - типы файлов, которые можно выбрать в диалоговом окне(в нашем случае это только текстовый формат)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:#открываем файл и записываем:
                file.write(f"Радиус основания: {radius_entry.get()}\n")
                file.write(f"Высота: {height_entry.get()}\n")
                file.write(f"Плотность: {density_entry.get()}\n")
                file.write("Результат:\n")
                file.write(result_label["text"])
                #выводим окно с сообщением, что все успешно сохранилось
            messagebox.showinfo("Сохранено", "Результаты успешно сохранены.")
        except Exception as e: #ошибка
            messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении: {str(e)}")



#функция выхода из приложения. Появляется еще одно окно с подтверждением выхода
def f_exit():
    answer = messagebox.askokcancel("Выход", "Вы точно хотите выйти?")
    if answer:
        root.quit()


#функция для того, чтобы показать результаты из меню
def show_results():
    results_window = tk.Toplevel(root)#создаем новое окно верхнего уровня
    results_window.title("Результаты вычислений")
    #создаем новый виджет метки label, он получает текст,который находится в result_label. А result_label_copy копия
    result_label_copy = tk.Label(results_window, text=result_label["text"])
    result_label_copy.pack()#размещаем метку



def show_task_description():
    #открываем окно с текстом задачи
    task_description_window = tk.Toplevel(root)#создаем новое окно верхнего уровня
    task_description_window.geometry("220x190")#указываем размер окна
    task_description_window.title("Условие задачи")
    #последний аргумент - это переход на следующую строку
    task_description_label = tk.Label(task_description_window, text="Приложение для расчёта параметров конуса. Главная форма содержит: элементы для ввода значений радиуса основания, высоты и плотности материала конуса; группу элементов для выбора вычислений объёма, массы и площади поверхности конуса.", wraplength=200)
    task_description_label.pack()#размещаем метку

#окно с информацией о программе
def show_about():
    messagebox.showinfo("О программе", "Приложение для расчёта параметров конуса.")


root = tk.Tk()#создаем экземпляр класса Tk
root.title("Гудимчик Настя 32 группа, 2 вариант")
root.geometry("300x300")  #размер главного окна

#создаем меню(файлб Результаты и Справка)
main_menu = Menu(root)#привязываем класс меню к root
file_menu = Menu(main_menu, tearoff=0)
#создаем команду сохранить, указываем ее функцию(что она делает) и горячую клавишу
file_menu.add_command(label="Сохранить", command=save_results, accelerator="Ctrl+S")
file_menu.add_separator()#линия для отделения двух логически разных функций
file_menu.add_command(label="Выход", command=f_exit, accelerator="Ctrl+Q")
#добавляем в меню Файл с вышеописанными командами
main_menu.add_cascade(label="Файл", menu=file_menu)

#далее повторяем все тоже самое с Результаты и Справка
result_menu = Menu(main_menu, tearoff=0)
result_menu.add_command(label="Показать", command=show_results, accelerator="Ctrl+R")
main_menu.add_cascade(label="Результаты", menu=result_menu)


about_menu = Menu(main_menu, tearoff=0)
about_menu.add_command(label="Условие задачи", command=show_task_description)
about_menu.add_command(label="О программе", command=show_about)
main_menu.add_cascade(label="Справка", menu=about_menu)

root.config(menu=main_menu)#к опции menu присваеваем экземплятор Menu через имя main_menu

var = tk.IntVar()
var.set(1)  #по умолчанию выбран первый вариант вычислений (объём)

#создаем два виджета:метку с надписью и текстовое поле для ввода
radius_label = tk.Label(root, text="Радиус основания:")#root означает что находится в основном окне
radius_label.pack()#располагаем метку в окне
radius_entry = tk.Entry(root)#создаем текстовое поле для ввода радиуса
radius_entry.pack()#располагаем метку в окне

#далее выполняем все тоже самое
height_label = tk.Label(root, text="Высота:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

density_label = tk.Label(root, text="Плотность:")
density_label.pack()
density_entry = tk.Entry(root)
density_entry.pack()

calculation_label = tk.Label(root, text="Выберите вариант вычислений:")
calculation_label.pack()

#здесь создаем радиокнопки для выбора варианта вычисления. Указываем что кнопка связана с переменной var.
#А значение 1 означает, что если этот переключатель выбран, то var=1. С остальными радиокнопками тоже самое
volume_radio = tk.Radiobutton(root, text="Объём", variable=var, value=1)
volume_radio.pack()
mass_radio = tk.Radiobutton(root, text="Масса", variable=var, value=2)
mass_radio.pack()
surface_area_radio = tk.Radiobutton(root, text="Площадь поверхности", variable=var, value=3)
surface_area_radio.pack()

#кнопка для подсчета
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

#виджет label для отображения результата
result_label = tk.Label(root, text="")
result_label.pack()

#привязываем сочетание горячих клавиш к функциям
root.bind("<Control-s>", lambda event: save_results())#сохранение
root.bind("<Control-r>", lambda event: show_results())#показать результат
root.bind("<Control-q>", lambda event: f_exit())#выход

root.mainloop()#запускаем цикл событий
