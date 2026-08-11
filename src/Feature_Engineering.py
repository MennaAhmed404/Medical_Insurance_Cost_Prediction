import pandas as pd
def feature_Engineering(df):
    #bmi
    bins = [0, 18.5, 25, 30, 35, 40, float("inf")]
    labels = [
    "Underweight",
    "Normal",
    "Overweight",
    "Obesity I",
    "Obesity II",
    "Obesity III"]  

    df["bmi_category"] = pd.cut(
    df["bmi"],
    bins=bins,
    labels=labels,
    right=False)

   # Age Categories
    age_bins = [18, 30, 45, 60, float("inf")]
    age_labels = [
        "Young Adult",
        "Middle Aged",
        "Senior Adult",
        "Elderly"
    ]

    df["age_category"] = pd.cut(
        df["age"],
        bins=age_bins,
        labels=age_labels,
        right=False
    )

    # # BMI × Smoker
    # df["bmi_smoker"] = (
    # df["bmi"] * (df["smoker"] == "yes").astype(int)
    # )

    return df
