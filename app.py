"""
House Price Prediction - Gradio Web Application
Loads the trained pipeline (models/best_model.pkl) and serves an
interactive prediction UI.
"""

from pathlib import Path

import gradio as gr
import joblib
import pandas as pd

# --------------------------------------------------------------------------
# Configuration (no hardcoded magic numbers scattered through the code)
# --------------------------------------------------------------------------
MODEL_PATH = Path(__file__).parent / "models" / "best_model.pkl"

FEATURE_CONFIG = {
    "Avg. Area Income": {
        "label": "Average Area Income ($)",
        "info": "Average annual income of residents in the area",
        "minimum": 10_000,
        "maximum": 150_000,
        "step": 500,
        "value": 68_000,
    },
    "Avg. Area House Age": {
        "label": "Average Area House Age (years)",
        "info": "Average age of houses in the area",
        "minimum": 0,
        "maximum": 20,
        "step": 0.1,
        "value": 5.9,
    },
    "Avg. Area Number of Rooms": {
        "label": "Average Number of Rooms",
        "info": "Average number of rooms per house in the area",
        "minimum": 2,
        "maximum": 12,
        "step": 0.1,
        "value": 6.9,
    },
    "Avg. Area Number of Bedrooms": {
        "label": "Average Number of Bedrooms",
        "info": "Average number of bedrooms per house in the area",
        "minimum": 1,
        "maximum": 8,
        "step": 0.1,
        "value": 4.0,
    },
    "Area Population": {
        "label": "Area Population",
        "info": "Population of the area",
        "minimum": 1_000,
        "maximum": 70_000,
        "step": 100,
        "value": 36_000,
    },
}

EXAMPLES = [
    [79545.46, 5.68, 7.01, 4.09, 23086.80],
    [61287.07, 6.73, 6.73, 3.09, 40173.07],
    [50000.00, 3.50, 5.50, 2.50, 15000.00],
]


# --------------------------------------------------------------------------
# Load model
# --------------------------------------------------------------------------
def load_model(model_path: Path):
    if not model_path.exists():
        raise FileNotFoundError(
            f"Trained model not found at '{model_path}'. "
            "Run notebooks/2_training.ipynb first to generate models/best_model.pkl."
        )
    return joblib.load(model_path)


model_pipeline = load_model(MODEL_PATH)
FEATURE_ORDER = list(FEATURE_CONFIG.keys())


# --------------------------------------------------------------------------
# Prediction function
# --------------------------------------------------------------------------
def predict_price(income, house_age, num_rooms, num_bedrooms, population):
    input_df = pd.DataFrame(
        [[income, house_age, num_rooms, num_bedrooms, population]],
        columns=FEATURE_ORDER,
    )
    predicted_price = model_pipeline.predict(input_df)[0]
    return f"${predicted_price:,.2f}"


# --------------------------------------------------------------------------
# Gradio Interface
# --------------------------------------------------------------------------
def build_interface() -> gr.Interface:
    inputs = [
        gr.Slider(
            minimum=cfg["minimum"],
            maximum=cfg["maximum"],
            step=cfg["step"],
            value=cfg["value"],
            label=cfg["label"],
            info=cfg["info"],
        )
        for cfg in FEATURE_CONFIG.values()
    ]

    output = gr.Textbox(label="Predicted House Price")

    interface = gr.Interface(
        fn=predict_price,
        inputs=inputs,
        outputs=output,
        title="🏡 House Price Prediction",
        description=(
            "Estimate a house's market price from area-level statistics. "
            "Adjust the sliders below to match the target area's profile, "
            "then view the predicted price. Model trained on the USA Housing dataset."
        ),
        examples=EXAMPLES,
        theme=gr.themes.Soft(primary_hue="blue"),
        flagging_mode="never",
    )
    return interface


if __name__ == "__main__":
    demo = build_interface()
    demo.launch(share=True)