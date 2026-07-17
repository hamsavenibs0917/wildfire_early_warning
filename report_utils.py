import os

try:
    import google.generativeai as genai
except ImportError:
    genai = None


def generate_report(data: dict, risk: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    prompt = (
        "Generate a short wildfire report for a forest department.\n\n"
        f"Temperature: {data['temperature']}\n"
        f"Humidity: {data['humidity']}\n"
        f"Wind Speed: {data['wind_speed']}\n"
        f"Rainfall: {data['rainfall']}\n"
        f"Predicted Risk: {risk}\n\n"
        "Explain the current alert and give simple forest department action advice."
    )

    if not api_key or genai is None:
        return (
            f"Risk level: {risk}. Dry air, high temperature, and strong wind increase wildfire danger. "
            "Forest staff should monitor hotspots, patrol high-risk zones, and stay ready for quick response."
        )

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
