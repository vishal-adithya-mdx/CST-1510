"""
RECORD CHECK  -  my version
===========================

Name  : Vishal Adithya Ashok
Lane  : AI
Date  : 01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

ol_count = 0
while True:
    ds_name = input("Dataset Name: ")
    if ds_name == "quit":
        break
    rows_loaded = float(input("Rows Loaded: "))
    rows_expected = float(input("Rows Expected: "))


    difference = rows_expected - rows_loaded
    percent = (rows_loaded / rows_expected) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        ol_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  DATASET NAME  -  {ds_name}")
    print("=" * 34)
    print(f"Rows Loaded     :  {rows_loaded:>10.2f}")
    print(f"Rows Expected   :  {rows_expected:>10.2f}")
    print(f"Difference      :  {difference:>10.2f}")
    print(f"Percent         :  {percent:>10.2f} %")
    print(f"Status          :  {status:>10}")
    print("=" * 34)

print()
print(f"Datasets OVER LIMIT: {ol_count}")