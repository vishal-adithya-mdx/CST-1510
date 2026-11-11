"""
RECORD CHECK  -  my version
===========================

Name  : Vishal Adithya Ashok
Lane  :  AI 
Date  : 11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Parses any raw string line into a dictionary data"""

    d = {}
    stripped_line = raw_line.strip()
    hostname_part,rest = stripped_line.split(",",1)
    d["hostname"] = hostname_part.strip().lower()

    for i in rest.split(","):
        key,value = i.split("=")
        k = key.strip()
        v = float(value.strip())
        d[k] = v
    return d

status_of = lambda x: "OVER LIMIT" if x>=100 else "WARNING" if x>=90 else "OK"

with open("temp.txt","w") as f:
    f.write("  Srv-01 , rating=87 , age=100\n")
    f.write("SRV-02,rating=120,age=100\n")
    f.write("  srv-03,rating=45 ,age=100\n")
    f.write("Srv-04 , rating = 93 , age=100\n")
    f.write("SRV-05, rating = 87,    age = 100")

flag = 0
with open("temp.txt") as f:
    for line in f.readlines():
        d = parse_line(line)
        p = (d["rating"]/d["age"]) * 100

        st =status_of(p)
        if st == "OVER LIMIT":
            flag+=1
        print(f"{d}     {st}")

        
print(f"\n{flag} no of records were flagged in total.")