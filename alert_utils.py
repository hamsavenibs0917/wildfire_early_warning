def get_forest_alert(data: dict, risk: str):
    danger_points = 0

    if data["temperature"] >= 40:
        danger_points += 1
    if data["humidity"] <= 25:
        danger_points += 1
    if data["wind_speed"] >= 25:
        danger_points += 1
    if data["rainfall"] <= 2:
        danger_points += 1

    if risk == "HIGH" and danger_points >= 3:
        return "RED ALERT", "Deploy forest teams immediately, increase patrols, and prepare fire control resources."

    if risk == "MEDIUM":
        return "ORANGE ALERT", "Keep forest patrols active, watch hotspot areas, and prepare response teams."

    if danger_points >= 2:
        return "YELLOW ALERT", "Monitor forest areas closely and keep teams on standby for sudden changes."

    return "GREEN ALERT", "Normal monitoring is enough. Keep routine forest surveillance active."
