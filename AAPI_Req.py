import re

import pandas as pd
import requests
import browser_cookie3
import json
import re
import warnings
warnings.filterwarnings("ignore")

mp_dict = {'1': 'iad', '3': 'dub', '4': 'dub', '5': 'dub', '44551': 'dub', '35691': 'dub', '6': 'pdx',
                   '328451': 'dub', '111172': 'pdx',
                   '7': 'iad', '771770': 'iad', '3240': 'pek', '712115121': 'dub', '338801': 'dub', '623225021': 'dub',
                   '44571': 'dub', '338851': 'dub',
                   '704403121': 'dub'}

mp_dict_MP = {'1': 'US', '3': 'UK', '4': 'DE', '5': 'FR', '44551': 'ES', '35691': 'IT', '6': 'JP',
                      '7': 'CA', '44571': 'IN'}
mp_dict_lang = {'1': 'en-US', '3': 'en-GB', '4': 'de-DE', '5': 'fr-FR', '44551': 'es-ES', '35691': 'it-IT',
                '6': 'ja-JP',
                '7': 'en-CA', '44571': 'en-IN'}

mp_dict_obfuscated = {'1': 'ATVPDKIKX0DER', '3': 'A1F83G8C2ARO7P', '4': 'A1PA6795UKMFR9', '5': 'A13V1IB3VIYZZH',
                      '35691': 'APJ6JRA9NG5V4'
    , '44551': 'A1RKKUPIHCS9HS', '6': 'A1VC38T7YXB528', '7': 'A2EUQ1WTGCTBG2', '44571': 'A21TJRUUN4KGV'}


mp = '1'
#asin = 'B0CP1VTYSR'
#asin = 'B075SYW1PS'
asin = 'B014S0DVDK'
# url = f'https://api-sso-access.corp.amazon.com/na-pre-prod-api-iad.iad.proxy.amazon.com/--/api/marketplaces/{mp_dict_obfuscated[mp]}/products/{asin}'

headers = {'Accept': 'application/vnd.com.amazon.api+json; type="product/v2"; expand="title(product.offer.title/v1),productImages(product.product-images/v2),productVideos(product.offer.product-videos/v1)"',
                'Accept-Language': 'en-US'}

cj = browser_cookie3.firefox()

#df = pd.read_excel(r'C://Users//louijose//Desktop//Olympic_Analysis_2//Image-Analysis-2.xlsx')

asin_list = []
image_list = []

url = f'https://api-sso-access.corp.amazon.com/api/marketplaces/{mp_dict_obfuscated[mp]}/products/{asin}'


r = requests.get(url, headers=headers, cookies=cj, verify=False)

data = r.content.decode()
data = json.loads(data)
print(data['entity']['productImages']['entity']['images'])
lis = data['entity']['productImages']['entity']['images']
# for ky,itn in dic.items():
cnt = 0
for itn in lis:
    for ky, itn in itn.items():
        #print(type(it))
        if isinstance(itn, str):
            if re.search('pt0', itn, flags=re.I):
                cnt += 1
print(cnt)

# if r.status_code == 200:
#     data = r.content.decode()
#     data = json.loads(data)
#     print(data['entity']['productVideos']['entity'])



# for ind,asin in enumerate(df['asin']):
#
#     try:
#         url = f'https://api-sso-access.corp.amazon.com/api/marketplaces/{mp_dict_obfuscated[mp]}/products/{asin}'
#
#
#         r = requests.get(url, headers=headers, cookies=cj, verify=False)
#
#         if r.status_code == 200:
#             print(ind,asin)
#             data = r.content.decode()
#             #print(data)
#             #cnts = re.findall('physicalId',data)
#             #print(len(cnts))
#             data = json.loads(data)
#             #print(data['entity']['productImages']['entity']['images'])
#             lis = data['entity']['productImages']['entity']['images']
#             #for ky,itn in dic.items():
#             cnt = 0
#             for itn in lis:
#                 for ky,itn in itn.items():
#                     if isinstance(itn,str):
#                         if re.search('main|pt0',itn,flags=re.I):
#                             cnt  += 1
#             asin_list.append(asin)
#             image_list.append(cnt-1)
#     except:
#         asin_list.append(asin)
#         image_list.append('NA')
#
# df2 = pd.DataFrame({"asin":asin_list,"images":image_list})
#
# df2.to_excel(r'C://Users//louijose//Desktop//Olympic_Analysis_2//image-result.xlsx',index=False)



        #print(ky)
        #print(itn)
    #imgeNums = len(data['entity']['productImages']['entity']['images'])
    #print(imgeNums)


"""
* cn/prod/1b (alias for api-prod-cn-cn-north-1b.pek.amazon.com)
  * dev/cn/prod (alias for dev-prod-api-cn-cn-north-1b.pek.amazon.com)
  * dev/eu/prod (alias for dev-prod-api-eu-eu-west-1a.dub.amazon.com)
  * dev/fe/prod (alias for dev-prod-api-fe-us-west-2a.pdx.amazon.com)
  * dev/na/prod (alias for dev-prod-api-na-us-east-1c.iad.amazon.com)
  * eu/prod/1a (alias for api-prod-eu-eu-west-1a.dub.amazon.com)
  * eu/prod/1b (alias for api-prod-eu-eu-west-1b.dub.amazon.com)
  * eu/prod/1c (alias for api-prod-eu-eu-west-1c.dub.amazon.com)
  * fe/prod/2a (alias for api-prod-fe-us-west-2a.pdx.amazon.com)
  * fe/prod/2b (alias for api-prod-fe-us-west-2b.pdx.amazon.com)
  * fe/prod/2c (alias for api-prod-fe-us-west-2c.pdx.amazon.com)
  * na/loadtest/prod (alias for na-prd-loadtest-api.iad.amazon.com)
  * na/prod/1a (alias for api-prod-na-us-east-1a.amazon.com)
  * na/prod/1b (alias for api-prod-na-us-east-1b.amazon.com)
  * na/prod/1d (alias for api-prod-na-us-east-1d.amazon.com)
  * na/prod/1e (alias for api-prod-na-us-east-1e.amazon.com)
  * na/prod/1f (alias for api-prod-na-us-east-1f.iad.amazon.com)
  * aapi-na-test-ssl-api.iad.amazon.com
  * aapi-soak-test.dub.amazon.com
  * aapi-soak-test.iad.amazon.com
  * amazon-api-unavailable.integ.amazon.com
  * api-prod-cn-cn-north-1b.pek.amazon.com
  * api-prod-cn-cnn1-az2.pek.amazon.com
  * api-prod-eu-eu-west-1a.dub.amazon.com
  * api-prod-eu-eu-west-1b.dub.amazon.com
  * api-prod-eu-eu-west-1c.dub.amazon.com
  * api-prod-eu-euw1-az1.dub.amazon.com
  * api-prod-eu-euw1-az2.dub.amazon.com
  * api-prod-eu-euw1-az3.dub.amazon.com
  * api-prod-fe-us-west-2a.pdx.amazon.com
  * api-prod-fe-us-west-2b.pdx.amazon.com
  * api-prod-fe-us-west-2c.pdx.amazon.com
  * api-prod-fe-usw2-az1.pdx.amazon.com
  * api-prod-fe-usw2-az2.pdx.amazon.com
  * api-prod-fe-usw2-az3.pdx.amazon.com
  * api-prod-na-us-east-1a.amazon.com
  * api-prod-na-us-east-1b.amazon.com
  * api-prod-na-us-east-1d.amazon.com
  * api-prod-na-us-east-1e.amazon.com
  * api-prod-na-us-east-1f.iad.amazon.com
  * api-prod-na-use1-az1.iad.amazon.com
  * api-prod-na-use1-az2.iad.amazon.com
  * api-prod-na-use1-az4.iad.amazon.com
  * api-prod-na-use1-az5.iad.amazon.com
  * api-prod-na-use1-az6.iad.amazon.com
  * ccapi-gremlin.iad.amazon.com
  * cn-clients-qa-gamma-api.pek.amazon.com
  * cn-dev-cache-api.pek.amazon.com
  * cn-devo-api.integ.amazon.com
  * cn-loadtest-api.pek.amazon.com
  * cn-pre-prod-api-pek.pek.proxy.amazon.com
  * cn-pre-prod-api.pek.amazon.com
  * cn-qa-beta-api.integ.amazon.com
  * cn-qa-gamma-api.pek.amazon.com
  * dev-beta-api.integ.amazon.com
  * dev-cache-jdk11-api.iad.amazon.com
  * dev-gamma-api.iad.amazon.com
  * dev-gamma-onebox-api.iad.amazon.com
  * dev-gamma-testoncr-api.iad.amazon.com
  * dev-gamma-testoncr-ccapi.iad.amazon.com
  * dev-prod-api-cn-cn-north-1b.pek.amazon.com
  * dev-prod-api-eu-eu-west-1a.dub.amazon.com
  * dev-prod-api-fe-us-west-2a.pdx.amazon.com
  * dev-prod-api-na-us-east-1c.iad.amazon.com
  * eu-clients-qa-gamma-api.dub.amazon.com
  * eu-dev-cache-api.dub.amazon.com
  * eu-devo-api.integ.amazon.com
  * eu-loadtest-api.dub.amazon.com
  * eu-prd-loadtest-api.dub.amazon.com
  * eu-pre-prod-api-dub.dub.proxy.amazon.com
  * eu-pre-prod-api.dub.amazon.com
  * eu-qa-beta-api.integ.amazon.com
  * eu-qa-gamma-api.dub.amazon.com
  * fe-clients-qa-gamma-api.pdx.amazon.com
  * fe-dev-cache-api.pdx.amazon.com
  * fe-devo-api.integ.amazon.com
  * fe-loadtest-api.pdx.amazon.com
  * fe-prd-loadtest-api.pdx.amazon.com
  * fe-pre-prod-api-pdx.pdx.proxy.amazon.com
  * fe-pre-prod-api.pdx.amazon.com
  * fe-qa-beta-api.integ.amazon.com
  * fe-qa-gamma-api.pdx.amazon.com
  * gpriyank-aapi.integ.amazon.com
  * gremlin-api.iad.amazon.com
  * na-clients-qa-gamma-api.iad.amazon.com
  * na-dev-cache-api.iad.amazon.com
  * na-devo-api.integ.amazon.com
  * na-loadtest-api.iad.amazon.com
  * na-onebox-loadtest-api.iad.amazon.com
  * na-prd-loadtest-api.iad.amazon.com
  * na-pre-prod-api-iad.iad.proxy.amazon.com
  * na-pre-prod-api.iad.amazon.com (default)
  * na-qa-beta-api.integ.amazon.com
  * na-qa-gamma-api.iad.amazon.com
  * rodleym.integ.amazon.com
  * storm-dev-gamma-api.iad.amazon.com
  * storm-dev-prod-api-na-us-east-1c.iad.amazon.com

"""