import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Лабораторная работа №1 — Квантование сигнала")

# --- квантование по 3 уровням (равномерное) ---
def quantize_three_levels(x, method='nearest'):
    """
    Равномерное квантование сигнала по 3 уровням
    method: 'floor', 'ceil', 'nearest'
    """
    x = np.asarray(x)
    Xmin, Xmax = x.min(), x.max()
    Δ = (Xmax - Xmin) / 3

    # пороги
    t1 = Xmin + Δ
    t2 = Xmin + 2 * Δ

    # уровни
    low = Xmin
    mid = Xmin + Δ
    high = Xmin + 2 * Δ
    top = Xmax  # верхняя граница

    q = np.zeros_like(x)

    if method == 'По нижнему уровню':  # всегда "вниз"
        q[x < t1] = low
        q[(x >= t1) & (x < t2)] = mid
        q[x >= t2] = high

    elif method == 'По верхнему уровню':  # всегда "вверх"
        q[x < t1] = mid
        q[(x >= t1) & (x < t2)] = high
        q[x >= t2] = top

    elif method == 'По ближайшему уровню':  # к ближайшему
        q[x < t1] = np.where(abs(x[x < t1] - low) < abs(x[x < t1] - mid), low, mid)
        mask = (x >= t1) & (x < t2)
        q[mask] = np.where(abs(x[mask] - mid) < abs(x[mask] - high), mid, high)
        q[x >= t2] = np.where(abs(x[x >= t2] - high) < abs(x[x >= t2] - top), high, top)

    return q


# --- UI ---
st.title("Квантование сигнала (ЛР №1)")

# выбор функции
func = st.selectbox("Выберите функцию:",
                    ["sin", "cos", "sin+cos", "пила", "треугольник"])

amp = st.number_input("Амплитуда", 0.1, 10.0, 1.0)
freq = st.number_input("Частота", 1.0, 50.0, 5.0)
N = st.slider("Число точек", 100, 2000, 500)

t = np.linspace(0, 1, N, endpoint=False)

# генерация сигнала
if func == "sin":
    signal = amp * np.sin(2 * np.pi * freq * t)
elif func == "cos":
    signal = amp * np.cos(2 * np.pi * freq * t)
elif func == "sin+cos":
    signal = amp * (np.sin(2 * np.pi * freq * t) + np.cos(2 * np.pi * freq * 2 * t))
elif func == "пила":
    signal = amp * (2 * (t * freq - np.floor(0.5 + t * freq)))  # sawtooth
elif func == "треугольник":
    signal = amp * (2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1)
else:
    signal = np.zeros_like(t)

# выбор метода
method = st.radio("Метод квантования:", ["По ближайшему уровню", "По нижнему уровню", "По верхнему уровню"])

# квантование
quantized = quantize_three_levels(signal, method=method)
mse = np.mean((signal - quantized) ** 2)

# график
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, signal, label="Оригинальный")
ax.step(t, quantized, where='mid', label=f"Квантованный ({method})")
ax.set_title(f"Квантование по 3 уровням — {method}, MSE={mse:.5f}")
ax.set_xlabel("Время")
ax.set_ylabel("Амплитуда")

# заштриховать разницу
ax.fill_between(t, signal, quantized, color="orange", alpha=0.3)

ax.legend()
ax.grid(True)

st.pyplot(fig)
