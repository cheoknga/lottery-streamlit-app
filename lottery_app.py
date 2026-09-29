
# -*- coding: utf-8 -*-

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
# 4. 顯示威力彩第二區特別球
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
# 5. 建立 Session State
# ==============================

# 大樂透結果
if "lotto_numbers" not in st.session_state:
    st.session_state.lotto_numbers = None

# 威力彩第一區
if "power_first" not in st.session_state:
    st.session_state.power_first = None

# 威力彩第二區
if "power_second" not in st.session_state:
    st.session_state.power_second = None


# ==============================
# 6. 主標題
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
# 7. 建立三欄按鈕
# ==============================
col1, col2, col3 = st.columns(3)


# ==============================
# 8. 大樂透按鈕
# ==============================
with col1:

    lotto_button = st.button(
        "大樂透",
        use_container_width=True
    )


# ==============================
# 9. 威力彩按鈕
# ==============================
with col2:

    power_button = st.button(
        "威力彩",
        use_container_width=True
    )


# ==============================
# 10. 清除按鈕
# ==============================
with col3:

    clear_button = st.button(
        "清除",
        use_container_width=True
    )


# ==============================
# 11. 大樂透抽號
# ==============================
if lotto_button:

    st.session_state.lotto_numbers = sorted(
        random.sample(range(1, 50), 6)
    )

    # 清除威力彩舊結果
    st.session_state.power_first = None
    st.session_state.power_second = None


# ==============================
# 12. 威力彩抽號
# ==============================
if power_button:

    # 第一區：1~38 抽 6 個
    st.session_state.power_first = sorted(
        random.sample(range(1, 39), 6)
    )

    # 第二區：1~8 抽 1 個
    st.session_state.power_second = random.randint(1, 8)

    # 清除大樂透舊結果
    st.session_state.lotto_numbers = None


# ==============================
# 13. 清除所有結果
# ==============================
if clear_button:

    st.session_state.lotto_numbers = None
    st.session_state.power_first = None
    st.session_state.power_second = None


# ==============================
# 14. 顯示大樂透結果
# ==============================
if st.session_state.lotto_numbers is not None:

    st.markdown(
        '<div class="section-title">大樂透號碼</div>',
        unsafe_allow_html=True
    )

    show_balls(
        st.session_state.lotto_numbers
    )


# ==============================
# 15. 顯示威力彩結果
# ==============================
if st.session_state.power_first is not None:

    st.markdown(
        '<div class="section-title">威力彩第一區</div>',
        unsafe_allow_html=True
    )

    show_balls(
        st.session_state.power_first
    )

    st.markdown(
        '<div class="section-title">威力彩第二區</div>',
        unsafe_allow_html=True
    )

    show_special_ball(
        st.session_state.power_second
    )

