"""
Задание 3:
Рассчитайте линейную корреляцию Пирсона, на основе данных.
Какой вывод можно сделать на основе полученного результата? 
Можно ли утверждать, что существует причинно-следственная связь между количеством чашек кофе, 
выпитых студентами в течение экзаменационного дня, и их итоговым баллом за экзамен?
"""

def correlation(x, y):
    n = len(x)
    if n != len(y) or n == 0:
        raise ValueError("Списки должны быть одинаковой ненулевой длины")
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    sum_xy = 0.0
    sum_x2 = 0.0
    sum_y2 = 0.0
    
    for xi, yi in zip(x, y):
        dx = xi - mean_x
        dy = yi - mean_y
        sum_xy += dx * dy
        sum_x2 += dx * dx
        sum_y2 += dy * dy
    
    if sum_x2 == 0 or sum_y2 == 0:
        return 0.0
    r = sum_xy / ((sum_x2 * sum_y2) ** 0.5)
    return r

def interpret_correlation(r):
    """Возвращает текстовую интерпретацию силы и направления корреляции."""
    abs_r = abs(r)
    direction = "положительная" if r > 0 else "отрицательная"
    
    if abs_r >= 0.9:
        strength = "очень сильная"
    elif abs_r >= 0.7:
        strength = "сильная"
    elif abs_r >= 0.5:
        strength = "средняя"
    elif abs_r >= 0.3:
        strength = "умеренная"
    elif abs_r >= 0.1:
        strength = "слабая"
    elif abs_r >= 0.01:
        strength = "незначительная"
    else:
        strength = "отсутствие"
        direction = ""  # при нуле направление не указываем
    
    if strength == "отсутствие":
        return "линейная связь отсутствует"
    else:
        return f"{strength} {direction} связь"

if __name__ == "__main__":
    coffee = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
    score = [85, 88, 79, 81, 84, 65, 67, 58, 76, 49]
    
    r = correlation(coffee, score)
    interpretation = interpret_correlation(r)
    
    # Формируем единый ответ с переносами строк
    result = (
        f"Коэффициент корреляции Пирсона: {r:.2f}\n"
        f"Интерпретация: {interpretation}\n\n"
        f"Вывод:\n"
        f"Полученное значение указывает на {interpretation.lower()}.\n"
        f"Однако наличие корреляции не доказывает причинно-следственную связь.\n"
        f"Возможно влияние третьих факторов (например, уровень подготовки, стресс, недосып).\n"
        f"Поэтому утверждать, что кофе напрямую влияет на результат экзамена, нельзя."
    )
    
    print(result)
