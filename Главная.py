import streamlit as st

st.set_page_config(page_title="Лабораторные работы", page_icon="📘")

# Заголовок и описание
st.title("ИВТ-223 - Тимофеев М.Е.")
st.write("Это веб-приложение для выполнения лабораторных работ по дисциплине **Теория моделирования**")
st.subheader("Список работ:")

# Пользовательский CSS для стилизации карточек
st.markdown("""
    <style>
    /* Сброс стандартных стилей ссылок под Firefox */
    :where(a.card) {
        color: white !important;
        text-decoration: none !important;
    }
    .card {
        background-color: #141922;
        border: 2px solid #FF4B4B;
        border-radius: 12px;
        padding: 40px 20px;
        text-align: left;
        font-size: 16px;
        line-height: 1.7;
        font-weight: bold;
        text-decoration: none;
        color: white;
        transition: 0.3s;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        height: 100%;
        display: flex;
        align-items: flex-end;
        justify-content: flex-start;
        padding-left: 16px;
        padding-bottom: 16px;
    }
    .card:hover {
        background-color: #FF4B4B;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transform: translateY(-3px);
    }
    .card.disabled {
        background-color: #e0e0e0;
        border: none;
        color: gray;
        cursor: not-allowed;
        box-shadow: none;
        font-size: 16px;
        line-height: 1.7;
        font-weight: bold;
        text-decoration: none;
    }
    .card.disabled:hover {
        background-color: #e0e0e0;
        box-shadow: none;
        transform: none;
    }
    .card a {
        color: white !important;
        text-decoration: none !important;
    }
    .card a:hover, .card a:active, .card a:visited, .card a:focus {
        color: white !important;
        text-decoration: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Создаем сетку 2x3 с помощью st.columns
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# Список карточек
cards = [
    {"title": "ЛР1<br>Квантование", "link": "/Квантование_сигнала_по_уровням", "disabled": False},
    {"title": "ЛР2<br>Дискретизация", "link": "/Дискретизация_сигналов", "disabled": False},
    {"title": "ЛР3<br>Скоро 🔒", "link": None, "disabled": True},
    {"title": "ЛР4<br>Скоро 🔒", "link": None, "disabled": True},
    {"title": "ЛР5<br>Скоро 🔒", "link": None, "disabled": True},
    {"title": "РЕФЕРАТ<br>Скоро 🔒", "link": None, "disabled": True},
]

# Размещаем карточки в колонках
with col1:
    if cards[0]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[0]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[0]["link"]}" target="_self" class="card">{cards[0]["title"]}</a>', unsafe_allow_html=True)

with col2:
    if cards[1]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[1]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[1]["link"]}" target="_self" class="card">{cards[1]["title"]}</a>', unsafe_allow_html=True)

with col3:
    if cards[2]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[2]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[2]["link"]}" target="_self" class="card">{cards[2]["title"]}</a>', unsafe_allow_html=True)

with col4:
    if cards[3]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[3]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[3]["link"]}" target="_self" class="card">{cards[3]["title"]}</a>', unsafe_allow_html=True)

with col5:
    if cards[4]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[4]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[4]["link"]}" target="_self" class="card">{cards[4]["title"]}</a>', unsafe_allow_html=True)

with col6:
    if cards[5]["disabled"]:
        st.markdown(f'<div class="card disabled">{cards[5]["title"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<a href="{cards[5]["link"]}" target="_self" class="card">{cards[5]["title"]}</a>', unsafe_allow_html=True)