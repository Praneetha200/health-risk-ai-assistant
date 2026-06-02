import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JtvuRZbgbfEzcajKHT2EDlzXIzVvtZrRM6tdIbCeytaw")

model = genai.GenerativeModel("gemini-2.5-flash")



def generate_remark(glucose, haemoglobin, cholesterol, risk_level):

    prompt = f"""
    Patient Health Report

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Calculated Risk Level: {risk_level}

    IMPORTANT:
    The risk level has already been calculated by a machine learning system.
    DO NOT change it.
    DO NOT contradict it.
    DO NOT use words like critical, severe, emergency, dangerous unless risk level is High Risk.

    Generate:
    1. Short explanation of the risk level.
    2. Lifestyle recommendation.
    3. Keep response under 3 sentences.
    """

    response = model.generate_content(prompt)

    return response.text