import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dosya yolları
excel_path = r"C:\Users\Serhat\Desktop\Project\customer_data.xlsx"
output_path = r"C:\Users\Serhat\Desktop\Project\rfm_results.xlsx"

# Veri yükleme
df = pd.read_excel(excel_path)

# Bugünün tarihi
today_date = pd.to_datetime("2024-11-25")

# Recency hesaplama
df["Recency"] = (today_date - df["Recency"]).dt.days

# RFM Skorları hesaplama
df["R_Score"] = pd.qcut(df["Recency"], q=5, labels=[5, 4, 3, 2, 1])
df["F_Score"] = pd.qcut(df["Frequency"], q=5, labels=[1, 2, 3, 4, 5])
df["M_Score"] = pd.qcut(df["Monetary"], q=5, labels=[1, 2, 3, 4, 5])

# RFM Skorlarını birleştirme
df["RFM_Score"] = df["R_Score"].astype(str) + df["F_Score"].astype(str) + df["M_Score"].astype(str)

# Sonuçları kaydetme
df.to_excel(output_path, index=False)
print(f"RFM analizi tamamlandı. Sonuçlar: {output_path}")

# RFM Skor Dağılımı grafiği
plt.figure(figsize=(10, 6))
sns.countplot(x="RFM_Score", data=df, hue="RFM_Score", palette="viridis", legend=False)
plt.title("RFM Skor Dağılımı")
plt.xlabel("RFM Skoru")
plt.ylabel("Müşteri Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()

# R, F, M Skor Dağılımı alt grafikler
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Recency Skoru Dağılımı
sns.countplot(x="R_Score", data=df, hue="R_Score", palette="Blues", ax=axes[0], legend=False)
axes[0].set_title("Recency Skoru Dağılımı")
axes[0].set_xlabel("Recency Skoru")
axes[0].set_ylabel("Müşteri Sayısı")

# Frequency Skoru Dağılımı
sns.countplot(x="F_Score", data=df, hue="F_Score", palette="Oranges", ax=axes[1], legend=False)
axes[1].set_title("Frequency Skoru Dağılımı")
axes[1].set_xlabel("Frequency Skoru")
axes[1].set_ylabel("Müşteri Sayısı")

# Monetary Skoru Dağılımı
sns.countplot(x="M_Score", data=df, hue="M_Score", palette="Greens", ax=axes[2], legend=False)
axes[2].set_title("Monetary Skoru Dağılımı")
axes[2].set_xlabel("Monetary Skoru")
axes[2].set_ylabel("Müşteri Sayısı")

# Grafiklerin düzenlenmesi
plt.tight_layout()
plt.show()
