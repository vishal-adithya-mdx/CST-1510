"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

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

def check_record(value,limit):
    difference = limit - value
    percent = (value/limit) * 100
    return difference,percent   


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path_):
    """loads txt records for label,value,limit lines from a file and returns a list of dicts"""

    try:
        with open(path_,"r") as f:
            rec = []
            for l in f.readlines():
                    label,value,limit = l.split(",")
                    value = float(value)
                    limit = float(limit)
                    rec.append({"label": label,"value": value,"limit": limit})
            return rec
    except FileNotFoundError:
        print("Enter a valid file name")
        return []

records = load_records("records_sample.txt")

percents = [(record["value"]/record["limit"]) * 100 for record in records ]

status = [status_of(percent) for percent in percents]
labels = [record["label"] for record in records]

with open("results.txt","w") as f:

    for l,s in zip(labels,status):
        f.write(f"{l},{s}\n")    
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
ol_count = 0

for record in records:
    difference,percent = check_record(record["value"],record["limit"])
    
    status = status_of(percent)
    if status =="OVER LIMIT":
        ol_count+=1
     
    print_report(record["label"],record["value"],record["limit"],difference,percent,status)

print(f"OVER LIMIT COUNT: {ol_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
