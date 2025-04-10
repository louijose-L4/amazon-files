import pandas as pd
import glob

#df = pd.read_json(r'C://Users//louijose//Desktop//Defect_Identifaction//file-1.json',lines=True)
#df.to_excel(r'C://Users//louijose//Desktop//Defect_Identifaction//result-1.xlsx',index=False)

df2 = pd.DataFrame()

for fil in glob.glob(r'C://Users//louijose//Desktop//WEEK-25-AR//16-06-2024//*'):
    df_r = pd.read_json(fil,lines=True)
    if df2.empty:
        df2 = df_r
    else:
        df2 = df2._append(df_r,ignore_index=True)
print(len(df2))
df3 = df2[:500000]
df4 = df2[500000:1000000]
df5 = df2[1000000:1500000]
df6 = df2[1500000:2000000]
df7 = df2[2000000:]
df3.to_excel(r'C://Users//louijose//Desktop//WEEK-25-AR//10-06-2024//result-16-06-2024_1.xlsx',index=False)
df4.to_excel(r'C://Users//louijose//Desktop//WEEK-25-AR//10-06-2024//result-16-06-2024_2.xlsx',index=False)
df5.to_excel(r'C://Users//louijose//Desktop//WEEK-25-AR//10-06-2024//result-16-06-2024_3.xlsx',index=False)
df6.to_excel(r'C://Users//louijose//Desktop//WEEK-25-AR//10-06-2024//result-16-06-2024_4.xlsx',index=False)
df7.to_excel(r'C://Users//louijose//Desktop//WEEK-25-AR//10-06-2024//result-16-06-2024_5.xlsx',index=False)