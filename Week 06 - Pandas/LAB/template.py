"""
RECORD CHECK  -  my version
===========================

Name  : Vishal Adithya Ashok
Lane  : AI 
Date  : 02/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "dataset": ["survey1", "survey2", "survey3", "survey4", "survey5"],
    "rows_loaded": [85, 92, 78, 110, 95],
    "rows_expected": [100, 100, 100, 100, 100]
})
df.to_csv("records.csv", index=False)
df = pd.read_csv("records.csv")
df.head()

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK")
df.head()


print(df[df["status"] != "OK"])

grouped_df = df.groupby("status")
print(grouped_df["status"].count())
df.to_csv("new_reports.csv",index = False)

grouped_df["status"].count().plot(kind='bar')
plt.title("Count Per Status")
plt.savefig('status_counts.png')
plt.show()
