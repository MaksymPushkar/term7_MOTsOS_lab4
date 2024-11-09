import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція f(t) для n = 18 (f(t) = t^(2*n+1), тому t^37
def f(t):
    return t ** 37

# Обчислення k-го члена інтегралу Фур'є для n = 18
def fourier_transform(k, T, N):
    omega_k = 2 * np.pi * k / T
    re_F, _ = quad(lambda t: f(t) * np.cos(omega_k * t), -N, N)  # Дійсна частина
    im_F, _ = quad(lambda t: f(t) * np.sin(omega_k * t), -N, N)  # Уявна частина
    return re_F, im_F

# Спектр амплітуд
def amplitude_spectrum(re_F, im_F):
    return np.sqrt(re_F ** 2 + im_F ** 2)

# Побудова графіків
def plot_spectrum(T, N, k_max):
    re_F_list = []
    amp_F_list = []

    for k in range(k_max):
        re_F, im_F = fourier_transform(k, T, N)
        re_F_list.append(re_F)
        amp_F_list.append(amplitude_spectrum(re_F, im_F))

    k_values = np.arange(k_max)

    plt.figure(figsize=(10, 5))

    # Графік дійсної частини
    plt.subplot(1, 2, 1)
    plt.plot(k_values, re_F_list, label='Re F(ω_k)')
    plt.xlabel('k')
    plt.ylabel('Re F(ω_k)')
    plt.title(f'Re F(ω_k) for T={T}')
    plt.grid(True)

    # Графік амплітуди
    plt.subplot(1, 2, 2)
    plt.plot(k_values, amp_F_list, label='|F(ω_k)|', color='r')
    plt.xlabel('k')
    plt.ylabel('|F(ω_k)|')
    plt.title(f'|F(ω_k)| for T={T}')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Основна функція
def main():
    N = 100*18  # Вибираємо значення N
    T_values = [4, 8, 16, 32, 64, 128]  # Різні значення T
    k_max = 50  # Кількість гармонік

    for T in T_values:
        print(f"Побудова спектрів для T = {T}")
        plot_spectrum(T, N, k_max)  # Для f(t) = t^37


if __name__ == '__main__':
    main()
