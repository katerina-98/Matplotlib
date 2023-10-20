import matplotlib.pyplot as plt

# Задаем данные
categories = ['ССЗ', 'Онкология', 'СД', 'ХЗЛ']
values = [17, 6, 2, 1]

# Создаем столбчатую диаграмму
plt.bar(categories, values)

# Настройка осей и заголовка
plt.xlabel('Заболевания')
plt.ylabel('Количество смертей в млн')
plt.title('Причина смерти')

# Отображаем диаграмму
plt.show()