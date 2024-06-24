import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('match.csv')

# Вычисление средней продолжительности
average_duration = data['duration'].mean()

# Разделение на минуты и секунды
minutes, seconds = divmod(average_duration, 60)
formatted_duration = f"{int(minutes)}:{int(seconds):02d}"

# Гистограмма продолжительности матча
plt.hist(data['duration'], bins=15, color='red', alpha=1)
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.title(f'Data Histogram\nAverage Duration {formatted_duration}')
plt.axvline(average_duration, color='blue', linestyle='solid', linewidth=2, label='Average Duration')
plt.legend()
plt.show()

# Вычисление средней продолжительности
average_duration = data['first_blood_time'].mean()

# Разделение на минуты и секунды
minutes, seconds = divmod(average_duration, 60)
formatted_duration = f"{int(minutes)}:{int(seconds):02d}"

# Гистограмма первого ФБ
plt.hist(data['first_blood_time'], bins=15, color='red', alpha=1)
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.title(f'Data Histogram\nAverage FB Time {formatted_duration}')
plt.axvline(average_duration, color='blue', linestyle='solid', linewidth=2, label='Average FB Time')
plt.legend()
plt.show()

# Гистограмма-пирог статистики выигрышей

# Подсчет относительной частоты
radiant_wins = data['radiant_win'].value_counts(normalize=True) * 100

# Пирог статистики выигрышей
labels = ['Radiant', 'Dire']
colors = ['skyblue', 'lightcoral']

fig, ax = plt.subplots()
ax.pie(radiant_wins, labels=labels, colors=colors, autopct='%1.1f%%')
ax.set_aspect('equal')
plt.title('Win Statistics')
plt.show()
