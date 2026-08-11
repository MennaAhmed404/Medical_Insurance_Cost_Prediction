from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def get_best_preprocessor():
 numeric_features = ["age", "bmi","children"]
 categorical_features = [
    "sex",
    "smoker",
    "region",
    "bmi_category",
    "age_category"
 ]

 preprocessor_4 = ColumnTransformer(
    transformers=[
        (
            "one_hot_encoding",
            OneHotEncoder(drop="first",handle_unknown="ignore"),
            categorical_features
        ),

        (
            "passthrough",
            "passthrough",
            numeric_features 
        )
    ]
 )
 return preprocessor_4 

#R² Score : 0.8780 
#           0.8782  After Adding age_category
#           0.8752  ِAfter adding bmi_smoker (i will remove it)
#           0.8770 After target Transformation (i will remove it)