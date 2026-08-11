import pandas as pd

def load_data():
    df=pd.read_csv("../data/insurance.csv")
    return df

# not exist missing values 
# //    //  outliers
# //    //  duplicates
# //    //  incorrect data


def preprocess():
    df=load_data()
    return df

import sys
print(sys.executable)

import pandas as pd
print(pd.__version__)