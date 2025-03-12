import pandas as pd

data = {
    "CustomerID": [1, 2, 3, 4, 5],
    "LastPurchaseDate": ["2024-10-01", "2024-09-20", "2024-11-10", "2024-08-15", "2024-11-01"],
    "TotalPurchases": [5, 15, 3, 20, 10],
    "TotalRevenue": [250, 500, 75, 800, 400]
}

df = pd.DataFrame(data)

df["LastPurchaseDate"] = pd.to_datetime(df["LastPurchaseDate"])

today_date = pd.to_datetime("2024-11-25")

df["Recency"] = (today_date - df["LastPurchaseDate"]).dt.days
df["Frequency"] = df["TotalPurchases"]
df["Monetary"] = df["TotalRevenue"]

df["R_Score"] = pd.qcut(df["Recency"], q=5, labels=[5, 4, 3, 2, 1])
df["F_Score"] = pd.qcut(df["Frequency"], q=5, labels=[1, 2, 3, 4, 5])
df["M_Score"] = pd.qcut(df["Monetary"], q=5, labels=[1, 2, 3, 4, 5])
df["RFM_Score"] = df["R_Score"].astype(str) + df["F_Score"].astype(str) + df["M_Score"].astype(str)

print(df[["CustomerID", "Recency", "Frequency", "Monetary", "RFM_Score"]])
