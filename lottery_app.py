# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:15:57 2026

@author: user
"""
import random
import streamlit as st

# ==============================
# 網頁標題
# ==============================
st.title("樂透選號系統")

st.write("請按下按鈕產生號碼")

# ==============================
# 大樂透按鈕
# ==============================
if st.button("大樂透"):
    lotto_numbers = sorted(random.sample(range(1, 50), 6))
    st.markdown(f"## 大樂透號碼：{lotto_numbers}")

# ==============================
# 威力彩按鈕
# ==============================
if st.button("威力彩"):
    first_area = sorted(random.sample(range(1, 39), 6))
    second_area = random.randint(1, 8)

    st.markdown(f"## 威力彩第一區：{first_area}")
    st.markdown(f"## 威力彩第二區：{second_area}")