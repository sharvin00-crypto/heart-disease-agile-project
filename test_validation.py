import pandas as pd

df = pd.read_csv("heart.csv")

def test_no_missing_values():
    assert df.isnull().sum().sum() == 0

def test_no_duplicates():
    assert df.duplicated().sum() == 0

def test_target_values():
    assert set(df["target"].unique()).issubset({0,1})

print("All tests passed!")
