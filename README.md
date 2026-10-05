# AI-FabricInspection
# 🧵 AI Fabric Inspection

## Business Idea Creation

AI Fabric Inspection เป็นแนวคิดระบบ AI สำหรับช่วยตรวจสอบ
คุณภาพและตำหนิของผ้าในกระบวนการผลิต

ระบบช่วยวิเคราะห์ประเภทตำหนิ ประสิทธิภาพการตรวจจับ
และแสดงผลผ่าน Dashboard เพื่อสนับสนุนการตัดสินใจของธุรกิจ

---

## 🎯 Business Problem

การตรวจสอบคุณภาพผ้าด้วยมนุษย์อาจใช้เวลา
และมีโอกาสเกิดความผิดพลาด

ตัวอย่างตำหนิที่พบ ได้แก่

- Hole
- Stain
- Broken Yarn
- Uneven Color
- Weaving Defect

---

## 💡 Business Solution

พัฒนา AI Fabric Inspection System
เพื่อช่วยตรวจสอบคุณภาพผ้าและวิเคราะห์ตำหนิ

ระบบสามารถแสดงข้อมูลผ่าน Dashboard
เพื่อช่วยให้โรงงานสามารถติดตามประสิทธิภาพ
และนำข้อมูลไปใช้ปรับปรุงกระบวนการผลิต

---

## 📊 Dataset

Dataset มีจำนวน 1,000 รายการ

ประกอบด้วยข้อมูล

- Image_ID
- Defect_Type
- Actual_Result
- AI_Result
- Confidence
- Detection_Time_sec
- Result

> หมายเหตุ: Dataset นี้เป็น Simulated/Test Dataset
> ที่สร้างขึ้นเพื่อใช้ในการทดลองและสร้าง Dashboard
> ไม่ใช่ข้อมูลจากโรงงานจริง

---

## 📈 Dashboard

Dashboard แสดงข้อมูลสำคัญ ได้แก่

- Total Inspections
- Correct Detection
- Wrong Detection
- AI Accuracy
- Defect Type Analysis
- Inspection Result
- AI Confidence
- Average Detection Time
- Inspection Records
- Business Insight

---

## 📌 Key Result

จาก Dataset จำนวน 1,000 รายการ

- Total Inspections: 1,000
- Correct: 904
- Wrong: 96
- Accuracy: 90.4%

---

## 💼 Business Value

AI Fabric Inspection สามารถช่วยธุรกิจในด้าน

1. ลดเวลาในการตรวจสอบคุณภาพ
2. ลดความผิดพลาดในการตรวจสอบ
3. วิเคราะห์ประเภทตำหนิที่เกิดขึ้นบ่อย
4. ลดของเสียจากกระบวนการผลิต
5. สนับสนุนการตัดสินใจของฝ่ายผลิต

---

## 🛠️ Technology

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

---
## ชื่อผู้ทำ

ชื่อสกุล : นางสาวอนุสรา กล่ำสวัสดิ์

รหัสนิสิต: 67160381

Sec: 1 

## ▶️ How to Run

ติดตั้ง Library

```bash
pip install -r requirements.txt
