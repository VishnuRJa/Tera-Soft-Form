import streamlit as st
import csv
from datetime import datetime

st.title("Meter Reader Employee Detail Submission Form")

# Cascading dropdown data
circle_division_map = {
    "EDC-AURAIYA": ["EDD-AURAIYA", "EDD-DIBIAPUR"],
    "EDC-ETAWAH": ["EDD-1-ETAWAH", "EDD-II ETAWAH", "EDD-SAIFAI"],
    "EDC-FARRUKHABAD": ["EDD-FARRUKKHABAD", "EDD-KAYAMGANJ", "EUDD-FARRUKHABAD"],
    "EDC-KANNAUJ": ["EDD-CHHIBRAMAU", "EDD-KANNAUJ"]
}

division_sdo_map = {
    "EDD-AURAIYA": ["2230512-EDSD AJITMAL", "2230513-EDSD BHAGAUTIPUR", "2230514-EDSD I AURAIYA", "EDSD AURAIYA TOWN"],
    "EDD-DIBIAPUR": ["2230521-EDSD I DIBIYAPUR", "2230522-EDSD II BIDHUNA", "2230523-EDSD III ROOPPUR SAHAR", "2230524-EDSD IV ACHHALDA"],
    "EDD-1-ETAWAH": ["EDSD  I ETAWAH", "EDSD  II ETAWAH", "EDSD  III ETAWAH"],
    "EDD-II ETAWAH": ["2230332-EDSD III CHAKARNAGAR", "2230333-EDSD I BAKEWAR", "2230334-EDSD IV UDI", "EDSD II BHARTHANA"],
    "EDD-SAIFAI": ["2230321-EDSD I JASWANTNAGAR", "2230322-EDSD II SAIFAI", "EDSD III TAKHA"],
    "EDD-FARRUKKHABAD": ["(Temp SDO) 2229219", "2229211-EDSD I FATEHGARH", "2229212-EDSD II NEEBKARORI", "2229214-EDSD IV JAHANGANJ", "EDSD III RAJEPUR"],
    "EDD-KAYAMGANJ": ["2229222-EDSD NAWABGANJ", "EDSD KAYAMGANJ"],
    "EUDD-FARRUKHABAD": ["EUDSD I FATEHGARH TOWN", "EUDSD II FARRUKHABAD", "EUDSD III LAKULA"],
    "EDD-CHHIBRAMAU": ["2229423-EDSD III SAURIKH", "2229424-EDSD IV SIKANDARPUR", "2229425-EDSD V TALGRAM", "EDSD I CHHIBRAMAU", "EDSD II GURSAYGANJ"],
    "EDD-KANNAUJ": ["2229412-EDSD II TIRWA", "2229413-EDSD I KANNAUJ", "2229414-EDSD IV THATHIYA", "EDSD  III KANNAUJ TOWN"]
}

# Dropdowns
circle = st.selectbox("Select Circle", list(circle_division_map.keys()))
division = st.selectbox("Select Division", circle_division_map.get(circle, []))
sdo = st.selectbox("Select SDO", division_sdo_map.get(division, []))

st.subheader("Personal Information")
name = st.text_input("Name")
father_name = st.text_input("Father's Name")
dob = st.date_input("Date of Birth")
aadhar = st.text_input("Aadhar Number")
address = st.text_area("Address")
mobile = st.text_input("Mobile Number")
email = st.text_input("Email ID")
uan = st.text_input("UAN")
esi = st.text_input("ESI Number")
bank_account = st.text_input("Bank Account Number")
ifsc = st.text_input("IFSC Code")

st.subheader("Nominee Details")
nominee_name = st.text_input("Nominee Name")
relation_nominee = st.text_input("Relation With Nominee")

if st.button("Submit"):
    # Validate mandatory fields
    if not name or not mobile or not aadhar:
        st.error("Please fill in Name, Mobile Number, and Aadhar Number.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            timestamp, circle, division, sdo,
            name, father_name, dob.strftime("%Y-%m-%d"), aadhar, address,
            mobile, email, uan, esi, bank_account, ifsc,
            nominee_name, relation_nominee
        ]
        try:
            with open('meter_reader_data.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
            st.success("✅ Data saved successfully!")
        except Exception as e:
            st.error(f"Failed to save data: {e}")
