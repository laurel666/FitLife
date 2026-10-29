# Проект FitLife - MVP версия 1.0

# 1. Знакомство
user_name = input('Как вас зовут? ').strip().title()
user_age = int(input('Сколько вам лет? ').strip())


# 2. Сбор данных
user_weight = float(
    input('Какой у вас вес? (в кг через точку, например: 61.3) ').strip())
user_height = float(
    input('Ваш рост? (в метрах, например: 1.73)').strip())


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
def calculate_bmi(weight, height):
    """Функция для расчета индекса массы тела (BMI)"""
    return weight / height ** 2


bmi = calculate_bmi(user_weight, user_height)

# Подсчет воды: вес * 30 мл
WATER_PER_KG = 30
water_needed = user_weight * WATER_PER_KG / 1000    # в литрах


# 4. Вывод красивого результата
print(f'\nОтчет для пользователя: {user_name}, {user_age} лет')
print(f'Ваш индекс массы тела: {round(bmi, 1)} кг/м²')
print(f'Рекомендуемая норма воды: {water_needed:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")
