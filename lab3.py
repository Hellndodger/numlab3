import numpy as np
import matplotlib.pyplot as plt
import math

# Функція, яка просто повертає sin(x)
def f(x):
    return np.sin(x)

# Рекурсивно обчислюємо факторіал, як я колись дізнався
def fact(k):
    if k == 0 or k == 1:
        return 1
    return k * fact(k - 1)

# Обчислює біноміальні коефіцієнти
def Cnk(n, k):
    return fact(n) / (fact(k) * fact(n - k))

# Перевіряє, чи число парне чи непарне (для знаків)
def step(n):
    return -1 if n % 2 else 1

# Обчислює дельта-синуси, чесно кажучи, до кінця не розумію як
def deltaf(y_vals, n):
    res = 0
    for k in range(n + 1):
        res += y_vals[k] * step(n - k) * Cnk(n, k)
    return res

# Обчислює якусь множину для аппроксимації
def factmn(t, k):
    result = 1
    for i in range(k):
        result *= (t - i)
    return result

# Основна функція аппроксимації
def fappr(y_vals, n, t):
    result = 0
    for k in range(n + 1):
        result += deltaf(y_vals, k) * factmn(t, k) / fact(k)
    return result

# Функція для оцінки помилки аппроксимації
def Eps(appr, true_val):
    return abs(appr - true_val)

# Основна функція програми, де все відбувається
def main():
    start = 0
    end = 1
    num_steps = 20
    h = (end - start) / num_steps
    x_values = np.linspace(start, end, num_steps + 1)
    y_values = np.sin(x_values)

    # Записуємо значення синусів в файл і друкуємо на екран
    with open('in.txt', 'w') as file1:
        for x, y in zip(x_values, y_values):
            file1.write(f"{x:e}\t{y:e}\n")
            print(f"{x:e}\t{y:e}")

    # Проводимо аппроксимацію
    t_vals = np.linspace(0, num_steps, 20 * num_steps + 1)
    fappr_vals = [fappr(y_values, num_steps, t) for t in t_vals]
    error_vals = [Eps(f(start + h * t), fappr(y_values, num_steps, t)) for t in t_vals]

    # Записуємо результати в два різних файли
    with open('fappr.txt', 'w') as file2, open('R.txt', 'w') as file3:
        for t, fappr_val, error_val in zip(t_vals, fappr_vals, error_vals):
            file2.write(f"{t:e}\t{fappr_val:e}\n")
            file3.write(f"{t:e}\t{error_val:e}\n")

    # Виводимо графік синусів і аппроксимації, синьо-жовті кольори для графіку
    plt.plot(x_values, y_values, label='sin(x)', color='blue')
    plt.plot(t_vals * h + start, fappr_vals, label='Approximation', color='yellow', linestyle='--')
    plt.xlabel('x', color='blue')
    plt.ylabel('f(x)', color='blue')
    plt.title('sin(x) і аппроксимація', color='blue')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

