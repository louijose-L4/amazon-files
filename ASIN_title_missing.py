import requests
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
import json
import pandas as pd



Myheaders = {'Accept': 'application/json',
             'Authorization': 'SableBasic GetProductMetadata'}

df = pd.read_excel(r'C://Users//louijose//Desktop//Autotitle-files//ASIN+with+NULL+title.xlsx')
title_list = []

for index,asin in enumerate(df['ASIN']):
    if index % 10 == 0:
        print(asin)
    try:
        sable_url = 'http://sable-responders-adhoc-iad.iad.proxy.amazon.com/datapath/query/catalog/item/-/1/' + str(asin) + '?languages%3D[en_US]'

        r = requests.get(sable_url, headers=Myheaders, auth=kerberos_auth, verify=False)

        jresponse = r.json()
        #data = {'SABLE': json.dumps(jresponse['product'])}
        data = json.dumps(jresponse['product'])
        data = json.loads(data)
        title_list.append(data['item_name'][0]['value'])
    except:
        title_list.append("sable data not available")

df['title'] = title_list
df.to_excel(r'C://Users//louijose//Desktop//Autotitle-files//ASIN+with+NULL+title+result.xlsx',index=False)
#data = json.dumps(data)

#print(data)
