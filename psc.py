import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv('csvs/BankChurners.csv')

# 1
customers = data.groupby(by="Attrition_Flag")["Attrition_Flag"].count()
ax = customers.plot.bar(rot=0, color=["powderblue", "cadetblue"])
plt.ylabel('count')
plt.show()

# 2
married = data[["Marital_Status", "Gender"]][data.Marital_Status == "Married"].groupby(by="Gender").count()
single = data[["Marital_Status", "Gender"]][data.Marital_Status == "Single"].groupby(by="Gender").count()
unknown = data[["Marital_Status", "Gender"]][data.Marital_Status == "Unknown"].groupby(by="Gender").count()
divorced = data[["Marital_Status", "Gender"]][data.Marital_Status == "Divorced"].groupby(by="Gender").count()

fig, axs = plt.subplots(1, 4, figsize=(9, 3), sharey=True)
axs[0].bar(married.index, list(married["Marital_Status"]))
axs[1].bar(single.index, list(single["Marital_Status"]))
axs[2].bar(unknown.index, list(unknown["Marital_Status"]))
axs[3].bar(divorced.index, list(divorced["Marital_Status"]))
fig.suptitle('Marital Status')
plt.xlabel('Gender')
plt.show()

# 3
education = data.groupby(by="Education_Level")["Education_Level"].count()
ax = education.plot.bar(rot=20, color=["powderblue", "cadetblue"])
plt.ylabel('count')
plt.show()

# 4
income1 = data[["Attrition_Flag", "Income_Category"]][data.Attrition_Flag == "Existing Customer"].\
    groupby(by="Income_Category").count()
income2 = data[["Attrition_Flag", "Income_Category"]][data.Attrition_Flag == "Attrited Customer"].\
    groupby(by="Income_Category").count()

mergeprop = income1.merge(income2, on="Income_Category")
mergeprop = mergeprop.rename(columns={"Attrition_Flag_x": "Existing Customer", "Attrition_Flag_y": "Attrited Customer"})
mergeprop.plot.bar(rot=10, color=["powderblue", "cadetblue"])
plt.ylabel('count')
plt.show()

# 5
cards = data.groupby(by="Card_Category")["Card_Category"].count()
cards.plot.bar(rot=0, color=["powderblue", "cadetblue"])
plt.show()

# 6
months = data["Months_on_book"]
sns.histplot(months, kde=True, stat="density", linewidth=1, edgecolor="white", color="cadetblue")
plt.ylabel('count')
plt.show()

# 7
relatives = data.groupby(by="Dependent_count")["Dependent_count"].count()
relatives.plot.bar(rot=0, color=["powderblue", "cadetblue"])
plt.show()

# 8
relationships1 = data[["Attrition_Flag", "Total_Relationship_Count"]][data.Attrition_Flag == "Existing Customer"].\
    groupby(by="Total_Relationship_Count").count()
relationships2 = data[["Attrition_Flag", "Total_Relationship_Count"]][data.Attrition_Flag == "Attrited Customer"].\
    groupby(by="Total_Relationship_Count").count()
mergeprop = relationships1.merge(relationships2, on="Total_Relationship_Count")
mergeprop = mergeprop.rename(columns={"Attrition_Flag_x": "Existing Customer", "Attrition_Flag_y": "Attrited Customer"})
mergeprop.plot.bar(rot=10, color=["powderblue", "cadetblue"])
plt.ylabel('count')
plt.show()

# 9
temp = data["Credit_Limit"]
sns.histplot(temp, kde=True, stat="density", linewidth=1, edgecolor="white", color="cadetblue")
plt.show()

# 10
temp = data[["Total_Trans_Amt", "Total_Trans_Ct"]]
ax1 = temp.plot.scatter(x='Total_Trans_Amt',
                        y='Total_Trans_Ct',
                        c='cadetblue')
plt.show()

# 11
temp = data["Avg_Utilization_Ratio"]
sns.histplot(temp, kde=True, stat="density", linewidth=1, edgecolor="white", color="cadetblue")
plt.show()
