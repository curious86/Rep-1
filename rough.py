
import pandas as pd
import matplotlib.pyplot as plt

# Считываем данные из файла Excel
file_path = 'gender-height-weight.xlsx'
df = pd.read_excel(file_path)

# Переводим рост в сантиметры и вес в килограммы
df['height_cm'] = df['height'] * 2.54  # 1 дюйм = 2.54 см
df['weight_kg'] = df['weight'] * 0.453592  # 1 фунт = 0.453592 кг

# Разделяем данные на мужской и женский пол
male_data = df[df['gender'] == 1]
female_data = df[df['gender'] == 2]

# Строим графики scatter зависимости веса от роста
plt.figure(figsize=(12, 6))

# График для всего набора данных
plt.subplot(1, 3, 1)
plt.scatter(df['height_cm'], df['weight_kg'], alpha=0.7)
plt.title('Для всего набора данных')
plt.xlabel('Рост (см)')
plt.ylabel('Вес (кг)')

# График для мужского пола
plt.subplot(1, 3, 2)
plt.scatter(male_data['height_cm'], male_data['weight_kg'], alpha=0.7)
plt.title('Для мужского пола')
plt.xlabel('Рост (см)')
plt.ylabel('Вес (кг)')

# График для женского пола
plt.subplot(1, 3, 3)
plt.scatter(female_data['height_cm'], female_data['weight_kg'], alpha=0.7)
plt.title('Для женского пола')
plt.xlabel('Рост (см)')
plt.ylabel('Вес (кг)')

plt.tight_layout()

# Строим гистограммы распределения весов и ростов для мужского пола
plt.figure(figsize=(12, 6))

# Гистограмма для веса мужского пола
plt.subplot(2, 1, 1)
plt.hist(male_data['weight_kg'], bins=15, edgecolor='black')
plt.title('Распределение веса для мужского пола')
plt.xlabel('Вес (кг)')
plt.ylabel('Количество')

# Гистограмма для роста мужского пола
plt.subplot(2, 1, 2)
plt.hist(male_data['height_cm'], bins=15, edgecolor='black')
plt.title('Распределение роста для мужского пола')
plt.xlabel('Рост (см)')
plt.ylabel('Количество')

plt.tight_layout()

plt.show()
