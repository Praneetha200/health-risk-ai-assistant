from ai_service import generate_remark


remark = generate_remark(
    glucose=180,
    haemoglobin=11,
    cholesterol=250
)

print(remark)