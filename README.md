# AI Wildfire Early Warning System

A simple beginner-friendly GenAI wildfire project with separate files for each main requirement.

## What It Does

- Lets you search and choose a forest name
- Fetches live weather for that forest location
- Predicts wildfire risk
- Shows a simple forest department alert and action message
- Generates a short GenAI-style report with a safe fallback

## Project Files

```text
wildfire_project/
├── app.py
├── forest_data.py
├── model_utils.py
├── weather_utils.py
├── alert_utils.py
├── report_utils.py
├── dataset/
│   └── wildfire_data.csv
├── wildfire_model.pkl
├── requirements.txt
└── README.md
```

## Setup

1. Install the packages in your current Python environment.

```bash
pip install -r requirements.txt
```

2. Run the app.

```bash
streamlit run app.py
```

## Notes

- `app.py` is the main file.
- The model trains automatically the first time if `wildfire_model.pkl` is missing.
- Python creates `__pycache__` automatically. That is normal.
- A virtual environment folder is optional. This project does not require a separate venv folder.

## Forest Examples

- Bandipur National Park
- Nagarhole National Park
- Periyar National Park
- Mudumalai National Park
- Silent Valley National Park
- Kanha National Park
- Pench National Park
- Gir Forest
- Jim Corbett National Park
- Corbett Tiger Reserve
- Dudhwa National Park
- Sundarbans National Park
- Sariska Tiger Reserve
- Bhadra Wildlife Sanctuary
- Bandhavgarh National Park
- Ranthambore National Park
- Simlipal National Park
- Tadoba Andhari Tiger Reserve
- Kaziranga National Park
- Manas National Park



## Host Link
https://wildfireearlywarning-ntqjzzpftgagszvwjt44mc.streamlit.app/
