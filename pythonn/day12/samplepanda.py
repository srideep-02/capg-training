# import pandas as pd
# data={
#     'Name':['john','bob','charlie','david'],
#     'Age':[25,30,31,40],
#     'city':['newyork','london','chicago','toronto']
    
# }
# dff = pd.DataFrame(data)
# print(dff)



# import pandas as pd 
# df = pd.read_csv("./pythonn/day12/annual-enterprise-survey-2023-financial-year-provisional.csv")
# df[df.index<2023].to_csv("./day12/output.csv", index=False)
# print(df[df.index<2023].sort_values(by='index',ascending = False))

# import pandas as pd

# data={
#     'Name':['Alice','Bob','Charlie','David'],
#     'Age':[25,30,35,40],
#     'City':['New York','Los Angels','Chicago','Houston']
# }

# df=pd.DataFrame(data)
# print(df)


import pandas as pd

data={
    'Name':['alice','bob','david'],
    'Age' :[1,2,3],
    'city':['dubai','newyork','los angeles']
}
df = pd.DataFrame(data)
print(df)

