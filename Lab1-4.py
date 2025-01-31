# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:10:52 2025

@author: Proshin Pavel
"""
import math
# вводим исходные данные
def input_par():
    print("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)")
    d1 = float(input())
    print("Введите кратчайшее расстояние от утопающего до берега, d2 (футы)")
    d2 = float(input())    
    print("Введите боковое смещение между спасателем и утопающим, h (ярды)")
    h = float(input())   
    print("Введите скорость движения спасателя по песку, v_sand (мили в час)")
    v = float(input())   
    print("Введите коэффициент замедления спасателя при движении в воде, n")
    n = float(input())   
    return d1, d2, h, v, n 

# переводим все значения к футам
def to_foot(d1, h, v):
    d1 = d1 * 3
    h = h * 3
    v = (v * 5280) / (60 * 60)  # перевод миль в час в футы в секунду
    return d1, h, v  

# рассчитываем необходимое время
def calculation(d1, q, h, d2, v, n):
    h1 = d1 * q
    l1 = math.sqrt((d1 ** 2) + (h1 ** 2))
    h2 = h - h1
    l2 = math.sqrt((d2 ** 2) + (h2 ** 2))
    t1 = l1 / v
    t2 = l2 / (v / n)
    t = round(t1 + t2, 1)
    return t 

# находим угол при котором t минимальный
def find_angle(d1, h, d2, v, n):
    time = float('inf')
    best_Q = 0
    for q in range(0, 91):  # Проверяем углы от 0 до 90 градусов
        Q = math.tan(q * math.pi / 180)
        t = calculation(d1, Q, h, d2, v, n)
        if t < time:
            time = t
            best_Q = q
    return best_Q, time 

def main():
    d1, d2, h, v, n = input_par()  # Получаем значения
    d1, h, v = to_foot(d1, h, v)  # Преобразуем значения
    best_Q, time = find_angle(d1, h, d2, v, n)  # Находим оптимальный угол
    print(f"Оптимальный угол Q: {best_Q} градусов, время: {time} секунд")

# Вызов функции main для запуска программы
main()
