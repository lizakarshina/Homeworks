# main.py
import matplotlib.pyplot as plt
from data_module import generate_data

# Отримати дані з модуля
X, Y = generate_data()

# Побудова графіка
plt.plot(X, Y, label="sin(X)", color="blue")
plt.title("Графік функції sin(X)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

plt.show()
