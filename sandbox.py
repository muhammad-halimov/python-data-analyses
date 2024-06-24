import matplotlib.pyplot as plt

# Генерируем случайные данные
data = [23, 34, 45, 67, 23, 56, 78, 89, 43, 65, 34, 56, 76]

# Построение гистограммы
plt.hist(data, bins=10, color='blue', alpha=0.7)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма данных')
plt.show()

# Построение диаграммы рассеяния
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [15, 25, 30, 40, 50, 60, 70, 80]

plt.scatter(x, y, color='red')
plt.xlabel('Переменная X')
plt.ylabel('Переменная Y')
plt.title('Диаграмма рассеяния')
plt.show()

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.show()

minutes, seconds = divmod(831, 60)
formatted_duration = f"{int(minutes)}:{int(seconds):02d}"

print(formatted_duration)
