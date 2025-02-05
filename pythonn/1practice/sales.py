import math
sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales":12000},
]
total={}
for i in sales_data:
    region=i["region"]
    sales=i["sales"]
    if region in total:
        total[region]+=sales
    else:
        total[region]=sales
print(total)