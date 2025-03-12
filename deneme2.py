import pandas as pd

excel_path = r"C:\Users\Serhat\Desktop\Project\customer_data.xlsx"
df = pd.read_excel(excel_path)

print("Excel sütun adları:", df.columns)
today_date = pd.to_datetime("2024-11-25")

df["Recency"] = (today_date - df["Recency"]).dt.days

df["R_Score"] = pd.qcut(df["Recency"], q=5, labels=[5, 4, 3, 2, 1])
df["F_Score"] = pd.qcut(df["Frequency"], q=5, labels=[1, 2, 3, 4, 5])
df["M_Score"] = pd.qcut(df["Monetary"], q=5, labels=[1, 2, 3, 4, 5])
df["RFM_Score"] = df["R_Score"].astype(str) + df["F_Score"].astype(str) + df["M_Score"].astype(str)

output_path = r"C:\Users\Serhat\Desktop\Project\rfm_results.xlsx"
df.to_excel(output_path, index=False)
print(f"RFM analizi tamamlandı. Sonuçlar: {output_path}")
