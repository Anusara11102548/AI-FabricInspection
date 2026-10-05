import streamlit as st 
import pandas as pd 
import plotly.express as px 
import random 
from pathlib import Path 
 
# ========================= 
# ตั้งค่าหน้าเว็บ 
# ========================= 
st.set_page_config( 
    page_title="AI Fabric Inspection", 
    page_icon="🧵", 
    layout="wide" 
) 
 
# ========================= 
# สร้างข้อมูลทดสอบ 
# ========================= 
def create_test_data(): 
 
    random.seed(42) 
 
    defect_types = [ 
        "Hole", 
        "Stain", 
        "Broken Yarn", 
        "Uneven Color", 
        "Weaving Defect", 
        "No Defect" 
    ] 
 
    rows = [] 
 
    # สร้าง 904 Correct + 96 Wrong 
    results = ["Correct"] * 904 + ["Wrong"] * 96 
 
    random.shuffle(results) 
 
    for i in range(1000): 
 
        defect = random.choice(defect_types) 
 
        confidence = round( 
            random.uniform(75, 99), 2 
        ) 
 
        detection_time = round( 
            random.uniform(0.5, 3.5), 2 
        ) 
 
        rows.append({ 
            "Image_ID": f"IMG_{i+1:04d}", 
            "Defect_Type": defect, 
            "Actual_Result": defect, 
            "AI_Result": defect, 
            "Confidence": confidence, 
            "Detection_Time_sec": detection_time, 
            "Result": results[i] 
        }) 
 
    return pd.DataFrame(rows) 
 
 
# ========================= 
# โหลดข้อมูล 
# ========================= 
@st.cache_data 
def load_data(): 
 
    folder = Path(__file__).parent 
 
    excel_file = folder / "AI_Fabric_Inspection_1000_rows.xlsx" 
 
    # ถ้ามี Excel ให้ใช้ Excel 
    if excel_file.exists(): 
 
        try: 
 
            df = pd.read_excel(excel_file) 
 
            return df 
 
        except Exception: 
 
            pass 
 
    # ถ้าไม่มี Excel ให้สร้างข้อมูลทดสอบ 
    return create_test_data() 
 
 
df = load_data() 
 
 
# ========================= 
# คำนวณ KPI 
# ========================= 
total = len(df) 
 
correct = ( 
    df["Result"] == "Correct" 
).sum() 
 
wrong = ( 
    df["Result"] == "Wrong" 
).sum() 
 
accuracy = ( 
    correct / total 
) * 100 
 
avg_confidence = ( 
    df["Confidence"].mean() 
) 
 
avg_time = ( 
    df["Detection_Time_sec"].mean() 
) 
 
 
# ========================= 
# HEADER 
# ========================= 
st.title("🧵 AI Fabric Inspection") 
 
st.subheader( 
    "ระบบ AI สำหรับตรวจสอบคุณภาพและตำหนิของผ้า" 
) 
 
st.write( 
    "Dashboard นี้นำเสนอข้อมูลการตรวจสอบคุณภาพผ้า " 
    "เพื่อวิเคราะห์ประเภทตำหนิ ประสิทธิภาพการตรวจจับ " 
    "และสนับสนุนการตัดสินใจในกระบวนการผลิต" 
) 
 
st.divider() 
 
 
# ========================= 
# KPI 
# ========================= 
col1, col2, col3, col4 = st.columns(4) 
 
col1.metric( 
    "🔍 Total Inspections", 
    f"{total:,}" 
) 
 
col2.metric( 
    "✅ Correct", 
    f"{correct:,}" 
) 
 
col3.metric( 
    "❌ Wrong", 
    f"{wrong:,}" 
) 
 
col4.metric( 
    "🎯 Accuracy", 
    f"{accuracy:.1f}%" 
) 
 
 
st.divider() 
 
 
# ========================= 
# วิเคราะห์ประเภทตำหนิ 
# ========================= 
st.header("📊 วิเคราะห์ประเภทตำหนิ") 
 
defect_count = ( 
    df["Defect_Type"] 
    .value_counts() 
    .reset_index() 
) 
 
defect_count.columns = [ 
    "Defect_Type", 
    "Count" 
] 
 
fig_defect = px.bar( 
    defect_count, 
    x="Defect_Type", 
    y="Count", 
    text="Count", 
    title="จำนวนการตรวจสอบแยกตามประเภทตำหนิ" 
) 
 
fig_defect.update_layout( 
    xaxis_title="ประเภทตำหนิ", 
    yaxis_title="จำนวน" 
) 
 
st.plotly_chart( 
    fig_defect, 
    use_container_width=True 
) 
 
 
# ========================= 
# ผลการตรวจสอบ + Confidence 
# ========================= 
col1, col2 = st.columns(2) 
 
with col1: 
 
    result_count = ( 
        df["Result"] 
        .value_counts() 
        .reset_index() 
    ) 
 
    result_count.columns = [ 
        "Result", 
        "Count" 
    ] 
 
    fig_result = px.pie( 
        result_count, 
        names="Result", 
        values="Count", 
        title="ผลการตรวจสอบ AI" 
    ) 
 
    st.plotly_chart( 
        fig_result, 
        use_container_width=True 
    ) 
 
 
with col2: 
 
    fig_confidence = px.histogram( 
        df, 
        x="Confidence", 
        nbins=20, 
        title="การกระจายของค่า Confidence" 
    ) 
 
    fig_confidence.update_layout( 
        xaxis_title="Confidence (%)", 
        yaxis_title="จำนวนภาพ" 
    ) 
 
    st.plotly_chart( 
        fig_confidence, 
        use_container_width=True 
    ) 
 
 
# ========================= 
# ประสิทธิภาพ 
# ========================= 
st.header("⚙️ ประสิทธิภาพการตรวจสอบ") 
 
col1, col2 = st.columns(2) 
 
with col1: 
 
    st.metric( 
        "Average Confidence", 
        f"{avg_confidence:.1f}%" 
    ) 
 
with col2: 
 
    st.metric( 
        "Average Detection Time", 
        f"{avg_time:.2f} sec" 
    ) 
 
 
st.divider() 
 
 
# ========================= 
# ตารางข้อมูล 
# ========================= 
st.header("📋 ข้อมูลการตรวจสอบ") 
 
st.dataframe( 
    df, 
    use_container_width=True, 
    height=400 
) 
 
 
# ========================= 
# Business Insight 
# ========================= 
st.header("💡 Business Insight") 
 
st.write( 
    f""" 
จากข้อมูลการตรวจสอบทั้งหมด **{total:,} รายการ** 
 
ระบบสามารถตรวจสอบได้ถูกต้อง **{correct:,} รายการ** 
คิดเป็น Accuracy ประมาณ **{accuracy:.1f}%** 
 
ข้อมูลประเภทตำหนิช่วยให้โรงงานสามารถวิเคราะห์ได้ว่า 
ตำหนิประเภทใดเกิดขึ้นบ่อย และสามารถนำข้อมูลไปใช้ 
ปรับปรุงกระบวนการผลิต ลดของเสีย 
และเพิ่มประสิทธิภาพการตรวจสอบคุณภาพผ้า 
""" 
) 
 
 
# ========================= 
# หมายเหตุ 
# ========================= 
st.caption( 
    "หมายเหตุ: Dataset นี้เป็น Simulated/Test Dataset " 
    "สำหรับการทดลองและสร้าง Dashboard" 
) 