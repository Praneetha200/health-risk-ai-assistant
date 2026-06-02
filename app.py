print("APP.PY UPDATED VERSION LOADED")

from flask import Flask, render_template, request, redirect
print("STEP 2: Flask imported")

from datetime import datetime

from models import db, Patient
print("STEP 3: Models imported")

from prediction import predict_risk, calculate_health_score
print("STEP 4: Prediction imported")

from ai_service import generate_remark
print("STEP 5: AI Service imported")

from flask import send_file
from reportlab.pdfgen import canvas
import re

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

app = Flask(__name__)
print("STEP 6: Flask app created")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
print("STEP 7: Database initialized")

with app.app_context():
    db.create_all()
    print("STEP 8: Database tables created")


@app.route("/")
def dashboard():

    patients = Patient.query.all()

    low_count = Patient.query.filter_by(
        risk_level="Low Risk"
    ).count()

    medium_count = Patient.query.filter_by(
        risk_level="Medium Risk"
    ).count()

    high_count = Patient.query.filter_by(
        risk_level="High Risk"
    ).count()

    critical_patients = []

    for p in patients:

        if (
            p.risk_level == "High Risk"
            or p.health_score < 50
            or p.glucose > 250
            or p.cholesterol > 300
        ):

            critical_patients.append(p)

    return render_template(
        "dashboard.html",
        patients=patients,
        low_count=low_count,
        medium_count=medium_count,
        high_count=high_count,
        critical_patients=critical_patients
    )





@app.route("/add", methods=["GET", "POST"])
def add_patient():

    if request.method == "POST":

        full_name = request.form["full_name"]
        dob = request.form["dob"]
        email = request.form["email"]

        # Email Validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            return "Invalid Email Format"

        # DOB Validation
        print("DOB RECEIVED:", dob)

        selected_date = datetime.strptime(
            dob,
            "%Y-%m-%d"
        ).date()

        today = datetime.now().date()

        print("SELECTED DATE:", selected_date)
        print("TODAY:", today)

        if selected_date > today:

            print("FUTURE DATE DETECTED")

            return "Date of Birth cannot be in the future"

        glucose = float(request.form["glucose"])
        haemoglobin = float(request.form["haemoglobin"])
        cholesterol = float(request.form["cholesterol"])

        # Numeric Validation
        if glucose < 0:
            return "Invalid Glucose Value"

        if haemoglobin < 0:
            return "Invalid Haemoglobin Value"

        if cholesterol < 0:
            return "Invalid Cholesterol Value"

        risk_level = predict_risk(
            glucose,
            haemoglobin,
            cholesterol
        )

        health_score = calculate_health_score(
            glucose,
            haemoglobin,
            cholesterol
        )

        remarks = generate_remark(
            glucose,
            haemoglobin,
            cholesterol,
            risk_level
        )

        print("GEMINI RESPONSE:")
        print(remarks)

        patient = Patient(
            full_name=full_name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            risk_level=risk_level,
            health_score=health_score,
            remarks=remarks
        )

        db.session.add(patient)
        db.session.commit()

        return redirect("/")

    return render_template(
        "add_patient.html",
        today=datetime.now().strftime("%Y-%m-%d")
    )




@app.route("/delete/<int:id>")
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        patient.full_name = request.form["full_name"]

        dob = request.form["dob"]

        selected_date = datetime.strptime(
            dob,
            "%Y-%m-%d"
        ).date()

        if selected_date > datetime.now().date():

            return "Date of Birth cannot be in the future"

        patient.dob = dob

        patient.email = request.form["email"]

        patient.glucose = float(
            request.form["glucose"]
        )

        patient.haemoglobin = float(
            request.form["haemoglobin"]
        )

        patient.cholesterol = float(
            request.form["cholesterol"]
        )

        patient.risk_level = predict_risk(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        patient.health_score = calculate_health_score(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        patient.remarks = generate_remark(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol,
            patient.risk_level
        )

        db.session.commit()

        return redirect("/")

    return render_template(
        "edit_patient.html",
        patient=patient,
        today=datetime.now().strftime("%Y-%m-%d")
    )




@app.route("/patient/<int:id>")
def patient_details(id):

    patient = Patient.query.get_or_404(id)

    return render_template(
        "patient_details.html",
        patient=patient
    )

@app.route("/pdf/<int:id>")
def download_pdf(id):

    patient = Patient.query.get_or_404(id)

    filename = f"patient_{id}.pdf"

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "HealthRisk AI Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"<b>Patient Name:</b> {patient.full_name}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Email:</b> {patient.email}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Date of Birth:</b> {patient.dob}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            f"<b>Glucose:</b> {patient.glucose}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Haemoglobin:</b> {patient.haemoglobin}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Cholesterol:</b> {patient.cholesterol}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            f"<b>Risk Level:</b> {patient.risk_level}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Health Score:</b> {patient.health_score}/100",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "AI Health Analysis",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            patient.remarks,
            styles["BodyText"]
        )
    )

    pdf.build(elements)

    return send_file(
        filename,
        as_attachment=True
    )





if __name__ == "__main__":
    print("STEP 9: Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)