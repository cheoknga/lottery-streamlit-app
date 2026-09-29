# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:15:57 2026

@author: user
"""
import random
import streamlit as st


# ==============================
# 1. 網頁基本設定
# ==============================
st.set_page_config(
    page_title="樂透選號系統",
    page_icon="🎱",
    layout="centered"
)


# ==============================
# 2. 自訂 CSS 樣式
# ==============================
st.markdown(
    """
    <style>

    /* 主標題置中 */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* 說明文字 */
    .sub-title {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }

    /* 彩球容器 */
    .ball-container {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        justify-content: center;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    /* 一般彩球 */
    .ball {
        width: 58px;
        height: 58px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;

        background-color: #4CAF50;
        color: white;

        font-size: 22px;
        font-weight: bold;

        box-shadow: 0 4px 8px rgba(0,0,0,0.20);
    }

    /* 威力彩第二區特別球 */
    .special-ball {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;

        background-color: #E53935;
        color: white;

        font-size: 24px;
        font-weight: bold;

        box-shadow: 0 4px 8px rgba(0,0,0,0.25);
    }

    /* 區塊標題 */
    .section-title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# 3. 顯示一般彩球函數
# ==============================
def show_balls(numbers):

    balls_html = '<div class="ball-container">'

    for number in numbers:
        balls_html += f'<div class="ball">{number}</div>'

    balls_html += '</div>'

    st.markdown(
        balls_html,
        unsafe_allow_html=True
    )


# ==============================
# 4. 顯示特別球函數
# ==============================
def show_special_ball(number):

    special_html = f"""
    <div class="ball-container">
        <div class="special-ball">{number}</div>
    </div>
    """

    st.markdown(
        special_html,
        unsafe_allow_html=True
    )


# ==============================
# 5. 主標題
# ==============================
st.markdown(
    '<div class="main-title">🎱 樂透選號系統</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">請選擇要產生的彩券號碼</div>',
    unsafe_allow_html=True
)


# ==============================
# 6. 建立兩欄按鈕
# ==============================
col1, col2 = st.columns(2)


# ==============================
# 7. 大樂透按鈕
# ==============================
with col1:

    lotto_button = st.button(
        "大樂透",
        use_container_width=True
    )


# ==============================
# 8. 威力彩按鈕
# ==============================
with col2:

    power_button = st.button(
        "威力彩",
        use_container_width=True
    )


# ==============================
# 9. 大樂透抽號
# ==============================
if lotto_button:

    lotto_numbers = sorted(
        random.sample(range(1, 50), 6)
    )

    st.markdown(
        '<div class="section-title">大樂透號碼</div>',
        unsafe_allow_html=True
    )

    show_balls(lotto_numbers)


# ==============================
# 10. 威力彩抽號
# ==============================
if power_button:

    # 第一區：1~38 抽 6 個
    first_area = sorted(
        random.sample(range(1, 39), 6)
    )

    # 第二區：1~8 抽 1 個
    second_area = random.randint(1, 8)

    st.markdown(
        '<div class="section-title">威力彩第一區</div>',
        unsafe_allow_html=True
    )

    show_balls(first_area)

    st.markdown(
        '<div class="section-title">威力彩第二區</div>',
        unsafe_allow_html=True
    )

    show_special_ball(second_area)