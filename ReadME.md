RFM-Analysis
What is RFM Analysis?
RFM (Recency, Frequency, Monetary) analysis is a powerful marketing technique used to identify and segment customers based on their purchasing behavior:
Recency (R): How recently a customer made a purchase.
Frequency (F): How often a customer makes a purchase.
Monetary (M): How much money a customer spends.

RFM segmentation helps businesses target their best customers, re-engage inactive ones, and create tailored marketing strategies.

Problem Statement
This project uses an online retail transactions dataset containing all purchases between 01/12/2010 and 09/12/2011 for a UK-based online store that mainly sells unique, all-occasion gifts. Many customers are wholesalers.

Goals:
Calculate RFM values for each customer using CustomerID.
Use December 2011 as the reference point for Recency calculations (Recency = months since last purchase).
Frequency represents the average number of purchases per month.
Monetary value is the total spend of the customer over the period.

Implementation

✅ Steps:
Compute RFM metrics for all customers.
Identify the top 10 customers based on Frequency and Monetary value (sorted by Frequency first, then Monetary).
Determine the optimal number of customer segments using dendrogram (hierarchical clustering) and elbow method (K-Means).
Assign customers to final segments and label them intuitively (e.g., "Loyal Customers", "At-Risk Customers", "New Customers").

✅ Visualizations:
Display Recency, Frequency, and Monetary score distributions using bar charts.
Plot dendrogram and elbow charts to justify clustering choice.
