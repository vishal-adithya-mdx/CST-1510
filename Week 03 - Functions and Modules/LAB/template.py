"""
RECORD CHECK  -  my version
===========================

Name  : Vishal Adithya Ashok
Lane  : AI
Date  : 07/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    if percent>=100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def print_report(ds_name,rows_loaded,rows_expected,difference,percent,status):

    print("=" * 34)
    print(f"  DATASET NAME  -  {ds_name}")
    print("=" * 34)
    print(f"Rows Loaded     :  {rows_loaded:>10.2f}")
    print(f"Rows Expected   :  {rows_expected:>10.2f}")
    print(f"Difference      :  {difference:>10.2f}")
    print(f"Percent         :  {percent:>10.2f} %")
    print(f"Status          :  {status:>10}")
    print("=" * 34)


ol_count = 0
while True:
    label = input("Enter Dataset Name: ")  

    if label == "quit":
        break
    
    value = float(input("Rows Loaded: "))     
    limit = float(input("Rows Expected: "))       
    
    difference = limit - value
    percent = (value/limit) * 100    
    
    status = status_of(percent=percent)  
    if status == "OVER LIMIT":
        ol_count+=1
    
    print_report(ds_name = label,
                 rows_expected=limit,
                 rows_loaded=value,
                 difference=difference,
                 percent=percent,
                 status=status)
print(f"OVER LIMIT COUNT: {ol_count}")