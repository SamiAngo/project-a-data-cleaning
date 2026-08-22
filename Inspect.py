import pandas as pd

passengers = pd.read_csv("data/passengers_messy.csv")
fares = pd.read_csv("data/fares_messy.csv")

print("=====PASSENGERS=====")
print(passengers.head())
print(passengers.shape)
print(passengers.columns)
print(passengers.dtypes)

print("\n=====FARES=====")
print(fares.head())
print(fares.shape)
print(fares.columns)
print(fares.dtypes)

print("\n===== MISSING VALUES =====")
print("\nPassengers:")
print(passengers.isna().sum())

print("\nFares:")
print(fares.isna().sum())

print("\n===== DUPLICATES =====")
print("Passenger duplicate rows:", passengers.duplicated().sum())
print("Fare duplicate rows:", fares.duplicated().sum())

print("\n===== SEX VALUES =====")
print(passengers["Sex"].value_counts(dropna=False))

print("\n===== AGE VALUES =====")
print(passengers["Age"].value_counts(dropna=False).head(10))

print("\n===== FARE VALUES =====")
print(fares["Fare"].value_counts(dropna=False).head(10))

print("\n===== EMBARKED VALUES =====")
print(passengers["Embarked"].value_counts(dropna=False))

print("\n===== CABIN MISSINGNESS =====")
print(fares["Cabin"].isnull().sum())

cabin_missing_pct = fares["Cabin"].isnull().mean() * 100
print("Cabin missing:", cabin_missing_pct, "%")


passenger_ids = set(passengers["passenger_id"])
fare_ids = set(fares["passenger_id"])

passengers_without_fares = passenger_ids - fare_ids
fares_without_passengers = fare_ids - passenger_ids

print("\n===== ID CHECK =====")
print("Passengers without fare:", len(passengers_without_fares))
print("Fares without passenger:", len(fares_without_passengers))



























































































