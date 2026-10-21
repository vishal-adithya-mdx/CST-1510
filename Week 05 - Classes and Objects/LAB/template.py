"""
RECORD CHECK  -  my version
===========================

Name  : Vishal Adithya Ashok
Lane  :  AI 
Date  :21/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    over_limit_count = 0

    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit
        self.percent = (self.value/self.limit) * 100
    
    def status(self):
        """"Returns the status of the Record."""
        if self.percent>=100:
            Record.over_limit_count+=1
            return "OVER LIMIT"
        elif self.percent>=90:
            return "WARNING"
        else:
            return "OK"

def load_records(path_):
    record = []
    with open(path_,"r") as f:
        for line in f.readlines():
            l,v,li = line.split(",")
            record.append(Record(l,float(v),float(li)))
    return record

records = load_records("records_sample.txt")


for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print(f"Rows Loaded     :  {record.value:>10.2f}")
    print(f"Rows Expected   :  {record.limit:>10.2f}")
    print(f"Status          :  {record.status():>10}")
    print("=" * 34)

print(Record.over_limit_count)