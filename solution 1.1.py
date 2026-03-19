"""
На ферме содержатся шесть разных видов животных, и каждый раз, когда фермер заходит в сарай,
он видит одно случайное животное. За день фермер заходит в сарай 6 раз.
Каково математическое ожидание количества разных видов животных, которые фермер увидит за день?
Ответ округлить до сотых, например: 4,12
"""
def given(n_animals=6, n_visits=6):
    # Вероятность не увидеть конкретный вид за одно посещение: 1 - 1/n
    # За n посещений: ((n-1)/n)^n
    not_seen = ((n_animals - 1) / n_animals) ** n_visits
    # Вероятность увидеть вид хотя бы раз:
    seen = 1 - not_seen
    # Матожидание числа видов = сумма вероятностей для всех видов:
    expected = n_animals * seen
    return expected

def simulation(n_animals=6, n_visits=6, n_simulations=1000000):
    """
    Моделирование методом Монте-Карло для проверки аналитического результата.
    """
    import random
    total = 0
    for _ in range(n_simulations):
        # Генерируем n_visits случайных чисел от 0 до n_animals-1 (виды)
        visits = [random.randint(0, n_animals-1) for _ in range(n_visits)]
        # Количество уникальных видов
        unique_count = len(set(visits))
        total += unique_count
    return total / n_simulations

if __name__ == "__main__":
    # Аналитическое решение
    exact = given()
    # Округление до сотых с заменой точки на запятую для соответствия примеру
    formatted = f"{exact:.2f}".replace('.', ',')
    print(f"Аналитическое математическое ожидание: {formatted}")
