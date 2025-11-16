import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI校园节能系统 - 成果展示", layout="wide")

st.title("AI校园节能系统｜成果展示（样例版）")
st.caption("数据为系统模拟生成，用于展示效果与成果呈现方式")

# -------------------------
# 1. 模拟节能前 vs 节能后的总能耗对比
# -------------------------

st.subheader("① 单栋教学楼能耗变化趋势）")

months = ["9月", "10月", "11月", "12月", "1月", "2月"]
before = np.array([12500, 13200, 11800, 11000, 9500, 8800])
after = before * 0.78  # 假设节能 22%

df = pd.DataFrame({"月份": months, "节能前(kWh)": before, "节能后(kWh)": after})

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(months, before, marker="o", label="节能前")
ax.plot(months, after, marker="o", label="节能后")
ax.set_ylabel("能耗 (kWh)")
ax.set_title("教学楼月度能耗对比")
ax.legend()

st.pyplot(fig)

st.info("从模拟对比可看到：节能后能耗平均降低 **≈22%**，与预期节能目标一致。")

# -------------------------
# 2. 单层楼节能策略（示例）
# -------------------------

st.subheader("② AI节能策略示例")

strategy_data = {
    "教室": [f"{i}0{i} 教室" for i in range(1, 7)],
    "AI 推荐策略": [
        "调整空调设定温度至 26℃，无人时自动关闭",
        "建议开启节能照明模式",
        "该时段占用率低，自动调节功率 40%",
        "自动关闭投影与插座排",
        "维持低功率照明，提升日光利用率",
        "无人时进入深度节能模式"
    ],
    "预计节能(%)": [18, 12, 22, 30, 15, 35]
}

strategy_df = pd.DataFrame(strategy_data)
st.table(strategy_df)

# -------------------------
# 3. 阶段性成果总结
# -------------------------

st.subheader("③ 阶段性成果总结")

st.success("""
- 完成单栋教学楼数据模拟。
- 生成 6 间教室的节能策略集，覆盖空调/照明/插座自动控制。
- 月均节能效果模拟值为 18–25% 区间，与高校节能改造参考值一致。

""")
