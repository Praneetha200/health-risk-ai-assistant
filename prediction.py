def calculate_health_score(glucose, haemoglobin, cholesterol):

    score = 100

    if glucose > 140:
        score -= 20

    if cholesterol > 240:
        score -= 20

    if haemoglobin < 12:
        score -= 20

    return max(score, 0)


def predict_risk(glucose, haemoglobin, cholesterol):

    score = calculate_health_score(
        glucose,
        haemoglobin,
        cholesterol
    )

    if score >= 80:
        return "Low Risk"

    elif score >= 50:
        return "Medium Risk"

    else:
        return "High Risk"