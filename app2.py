import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")
st.title("AI校园节能系统 · 原型演示")
# 模拟数据
hours = np.arange(0, 24)
normal = np.random.uniform(10, 20, 24)
ai_control = normal * np.random.uniform(0.80, 0.88, 24)
df = pd.DataFrame({
    "Hour": hours,
    "传统模式": normal,
    "AI调控": ai_control
})
# 布局
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 教学楼24小时用电模拟")
    st.line_chart(df, x="Hour", y=["传统模式", "AI调控"])

with col2:
    st.subheader("🔍 教室占用与调控建议（模拟）")

    table = pd.DataFrame({
        "教室": ["101", "102", "201", "202", "301"],
        "状态": ["无人", "上课中", "无人", "活动中", "无人"],
        "当前用电(kWh)": [0.2, 2.5, 0.1, 1.8, 0.15],
        "系统建议": ["关闭空调", "保持", "关闭照明", "保持", "关闭照明"]
    })

    st.table(table)

st.markdown("---")
st.subheader("⚙️ 节能策略模拟（演示版）")

st.markdown("""
- 自动调节空调温度（夏季26℃、冬季20℃）
- 无人时自动关灯
- 上课前10分钟智能预冷/预热
- 根据课表智能判断占用状态
""")
