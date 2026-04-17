from deep_translator import GoogleTranslator

# 🌐 Translation function
def translate_text(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text


def analyze_health(symptoms, sleep, steps, stress):

    # 🌍 Translate symptoms to English
    symptoms = translate_text(symptoms)

    # 🧹 Clean inputs
    symptoms = symptoms.lower()

    try:
        sleep = int(sleep)
    except:
        sleep = 0

    try:
        steps = int(steps)
    except:
        steps = 0

    stress = stress.lower()

    # 📊 Initialize
    risk = "Low"
    prediction = []
    explanation = []
    suggestion = []

    # 🚨 Emergency detection
    if "chest pain" in symptoms or "shortness of breath" in symptoms:
        risk = "High"
        prediction.append("Possible cardiac or respiratory issue")
        suggestion.append("Seek immediate medical attention")

    # 🧠 Sleep analysis
    if sleep < 5:
        prediction.append("High fatigue and low immunity risk")
        explanation.append("Lack of sleep affects recovery and immune strength")
        suggestion.append("Increase sleep to at least 7 hours")

    elif sleep < 7:
        prediction.append("Moderate fatigue risk")
        suggestion.append("Maintain consistent sleep schedule")

    # 🏃 Activity check
    if steps < 3000:
        prediction.append("Low physical activity detected")
        explanation.append("Sedentary lifestyle may affect heart health")
        suggestion.append("Increase daily steps to 6000+")

    # 😓 Stress analysis
    if "high" in stress:
        prediction.append("High stress impact detected")
        explanation.append("Stress can impact both mental and physical health")
        suggestion.append("Practice relaxation techniques")

    # 📈 Final risk calculation
    if len(prediction) >= 3 and risk != "High":
        risk = "Medium"

    if len(prediction) >= 5:
        risk = "High"

    # 📦 Final output
    return {
        "risk": risk,
        "prediction": ", ".join(prediction) if prediction else "General health stable",
        "explanation": ", ".join(explanation) if explanation else f"Based on your input, your current health shows {risk} risk.",
        "suggestion": ", ".join(suggestion) if suggestion else "Maintain a healthy lifestyle"
    }