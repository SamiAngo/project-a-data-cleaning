import pandas as pd

def inspect_data(df):
    print("==== Data Inspection ====")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data Types:")
    print(df.dtypes)

passengers = pd.read_csv("data/passengers_messy.csv")
fares = pd.read_csv("data/fares_messy.csv")


inspect_data(passengers)
print()
inspect_data(fares)