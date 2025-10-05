import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="ЛР2 — Дискретизация сигналов", page_icon="📈")

st.title("Лабораторная работа №2 — Дискретизация сигналов (результирующая гармоника)")
st.markdown("""
В данной лабораторной работе исследуется процесс **дискретизации непрерывных сигналов**
и определяется **результирующая гармоника** по спектру дискретного сигнала.
""")

# ============================================================
# --- параметры сигнала ---
# ============================================================

st.subheader("Параметры сигнала")

col1, col2, col3, col4 = st.columns(4)
with col1:
    func_type = st.selectbox("Форма сигнала",
        ["sin²", "cos²", "|sin|", "exp(-t)", "sin+cos", "пилообразный", "треугольный"])
with col2:
    A = st.number_input("Амплитуда A", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
with col3:
    f = st.slider("Частота f, Гц", 1.0, 20.0, 5.0)
with col4:
    fd = st.slider("Частота дискретизации fₑ, Гц", 20, 200, 50)

duration = st.slider("Длительность сигнала (с)", 0.1, 2.0, 1.0)

# ============================================================
# --- формирование сигнала ---
# ============================================================

t_cont = np.linspace(0, duration, 5000)

if func_type == "sin²":
    signal_cont = (A * np.sin(2*np.pi*f*t_cont))**2
elif func_type == "cos²":
    signal_cont = (A * np.cos(2*np.pi*f*t_cont))**2
elif func_type == "|sin|":
    signal_cont = A * np.abs(np.sin(2*np.pi*f*t_cont))
elif func_type == "exp(-t)":
    signal_cont = A * np.exp(-2*t_cont) * np.abs(np.sin(2*np.pi*f*t_cont))
elif func_type == "sin+cos":
    signal_cont = A * (np.sin(2*np.pi*f*t_cont) + np.cos(2*np.pi*f*t_cont)) / 2 + A
elif func_type == "пилообразный":
    signal_cont = A * (2*(t_cont*f - np.floor(0.5 + t_cont*f))) + A
elif func_type == "треугольный":
    signal_cont = A * (2*np.abs(2*(t_cont*f - np.floor(t_cont*f + 0.5))) - 1) + A
else:
    signal_cont = np.zeros_like(t_cont)

# все значения ≥ 0
signal_cont = np.clip(signal_cont, 0, None)

# --- дискретизация ---
t_disc = np.arange(0, duration, 1/fd)
signal_disc = np.interp(t_disc, t_cont, signal_cont)

# ============================================================
# --- восстановление (ряд Котельникова через sinc) ---
# ============================================================
def sinc_reconstruction(t, t_disc, samples, fd):
    reconstructed = np.zeros_like(t)
    for k in range(len(samples)):
        reconstructed += samples[k] * np.sinc(fd * (t - t_disc[k]))
    return reconstructed

signal_recon = sinc_reconstruction(t_cont, t_disc, signal_disc, fd)

# ============================================================
# --- спектральный анализ ---
# ============================================================
N = len(signal_disc)
freqs = np.fft.fftfreq(N, d=1/fd)
spectrum = np.abs(np.fft.fft(signal_disc)) / N
mask = freqs >= 0
freqs, spectrum = freqs[mask], spectrum[mask]
dominant_freq = freqs[np.argmax(spectrum)]
dominant_amp = np.max(spectrum)

# ============================================================
# --- вывод результатов ---
# ============================================================
st.markdown("---")
st.subheader("Результирующая гармоника")
st.write(f"**Частота:** {dominant_freq:.2f} Гц")
st.write(f"**Амплитуда:** {dominant_amp:.3f}")

# ============================================================
# --- графики ---
# ============================================================
tab1, tab2 = st.tabs(["📉 Сигналы", "📊 Спектр"])

with tab1:
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(t_cont, signal_cont, label="Исходный сигнал (непрерывный)")
    ax.stem(t_disc, signal_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label="Отсчёты (дискретизация)")
    ax.plot(t_cont, signal_recon, 'g--', label="Восстановленный сигнал (Котельников)")
    ax.set_xlabel("Время, с")
    ax.set_ylabel("Амплитуда")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

with tab2:
    fig2, ax2 = plt.subplots(figsize=(10,4))
    ax2.plot(freqs, spectrum, label="Амплитудный спектр")
    ax2.axvline(dominant_freq, color='red', linestyle='--', label=f"Результирующая гармоника ({dominant_freq:.2f} Гц)")
    ax2.set_xlabel("Частота, Гц")
    ax2.set_ylabel("Амплитуда")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)
