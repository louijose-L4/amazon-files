def attribute_present_in_bp(data):
    import json
    import re
    import traceback

    def regex_match(attribute, sentence):
        regex_attribute = r'\W' + re.escape(attribute) + r'\W'
        if re.search(regex_attribute, ' ' + sentence + ' ', re.IGNORECASE):
            result = True
        else:
            result = False
        return result

    def get_atb(dictionary, attr):
        def get_into_loop(dictionary, atb, data_key=''):

            if str(data_key) == atb:
                key_content = dictionary
                return key_content

            if str(type(dictionary)) in ["<class 'list'>", "<class 'dict'>"]:
                for one_key in dictionary:
                    if str(type(dictionary)) in ["<class 'list'>"]:
                        found_key = get_into_loop(one_key, atb, data_key=one_key)
                        if found_key != None:
                            return found_key
                    elif str(type(dictionary)) in ["<class 'dict'>"]:
                        found_key = get_into_loop(dictionary[one_key], atb, data_key=one_key)
                        if found_key != None:
                            return found_key
            return None

        result_dict = ""
        for one_atb in attr.split(r'.'):

            if result_dict == "":
                result_dict = get_into_loop(dictionary=dictionary, atb=one_atb)
            else:
                result_dict = get_into_loop(dictionary=result_dict, atb=one_atb)

        # print(result_dict)
        normalized_value = get_into_loop(dictionary=result_dict, atb='normalized_value')

        attribute = ""
        if normalized_value != None:
            VALUE = get_into_loop(dictionary=normalized_value, atb='value')
            DECIMAL_VALUE = get_into_loop(dictionary=normalized_value, atb='decimal_value')
            STRING_VALUE = get_into_loop(dictionary=normalized_value, atb='string_value')
            UNIT = get_into_loop(dictionary=normalized_value, atb='unit')
            if VALUE != None:
                if type(VALUE) == float:
                    attribute = round(VALUE, 2)
                else:
                    attribute = VALUE
            elif DECIMAL_VALUE != None:
                if type(DECIMAL_VALUE) == float:
                    attribute = round(DECIMAL_VALUE, 2)
                else:
                    attribute = DECIMAL_VALUE
            elif STRING_VALUE != None:
                attribute = STRING_VALUE
            if UNIT != None:
                attribute = str(attribute) + ' ' + UNIT
            return {attr: attribute}

        VALUE = get_into_loop(dictionary=result_dict, atb='value')
        DECIMAL_VALUE = get_into_loop(dictionary=result_dict, atb='decimal_value')
        STRING_VALUE = get_into_loop(dictionary=result_dict, atb='string_value')
        UNIT = get_into_loop(dictionary=result_dict, atb='unit')
        if VALUE != None:
            if type(VALUE) == float:
                attribute = round(VALUE, 2)
            else:
                attribute = VALUE
        elif DECIMAL_VALUE != None:
            if type(DECIMAL_VALUE) == float:
                attribute = round(DECIMAL_VALUE, 2)
            else:
                attribute = DECIMAL_VALUE
        elif STRING_VALUE != None:
            attribute = STRING_VALUE
        if UNIT != None:
            attribute = str(attribute) + ' ' + UNIT
        return {attr: attribute}

    def get_end_vals(data):

        end_vals = data['BYODOutput']['output']
        end_vals_list = {}

        try:
            end_vals.pop("attributes")
        except:
            pass

        try:
            end_vals.pop("Platform")
        except:
            pass

        if end_vals.__len__() != 0:
            for one_key in end_vals.keys():

                end_vals_list[one_key] = []

                try:
                    end_vals_list[one_key] = end_vals_list[one_key].__add__(end_vals[one_key]['Valid'])
                except:
                    pass

                try:
                    syn_list = []
                    for each_syn in end_vals[one_key]['Synonyms']:
                        for one_syn in str(each_syn).strip(' ').split('|'):
                            syn_list.append(str(one_syn).strip(' '))
                    end_vals_list[one_key] = end_vals_list[one_key].__add__(syn_list)
                except:
                    pass

        return end_vals_list

    def get_atb_list(data):
        return data['BYODOutput']['output']['attributes']

    try:
        sable_dict = json.loads(json.loads(data['ASIN_DATA']['data'])['SABLE'])
        product_type = sable_dict['product']['product_type'][0]['value']
        product_type = str(product_type)
        bp_list = sable_dict['product']['bullet_point']
        bp = []

        for i in bp_list:
            for key, val in i.items():
                if key == 'value':
                    bp.append(val)

        bp_string = str('\n'.join(bp))

        mp_id = sable_dict['marketplace_id']

        mapping = {
            338801: 'AE', 111172: 'AU', 526970: 'BR',
            7: 'CA', 771770: 'MX', 328451: 'NL',
            338811: 'SA', 338851: 'TR', 623225021: 'EG',
            712115121: 'PL', 704403121: 'SE', 104444012: 'SG',
            4: 'DE', 44551: 'ES', 5: 'FR', 44571: 'IN',
            35691: 'IT', 6: 'JP', 1: 'US',
            3: 'GB'}

        mp = mapping[int(mp_id)]

        list_atb = get_atb_list(data)

        pt_atb_value_dict = get_end_vals(data)

        response_data = {}

        for one_atb in list_atb:
            atb_val = get_atb(sable_dict['product'], one_atb)
            valid_val_list = []
            if atb_val[one_atb] != '':

                match_result = regex_match(atb_val[one_atb], bp_string)

                try:
                    valid_val_list = list(
                        map(lambda x: str(x).lower(), pt_atb_value_dict[str(mp) + '_' + str(product_type) + '_' + str(one_atb)]))
                except:
                    valid_val_list = []

                if str(atb_val[one_atb]).lower() in valid_val_list:
                    response_data[one_atb] = {'Available': 'YES', 'value': str(atb_val[one_atb]),
                                              'bullet_point_match': match_result, 'EnD_Match': 'YES'}
                else:
                    response_data[one_atb] = {'Available': 'YES', 'value': str(atb_val[one_atb]),
                                              'bullet_point_match': match_result, 'EnD_Match': 'NO'}
            else:
                response_data[one_atb] = {'Available': 'NO', 'value': '', 'bullet_point_match': False,
                                          'EnD_Match': 'NO'}

        response_data['bullet_point'] = str(bp_string)

        return {'isPassed': False, 'context_data': json.dumps(response_data)}

    except Exception as e:
        a = str(traceback.format_exc())
        return {'isPassed': False, 'context_data': str(a)}


import requests
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import json

kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)

Myheaders = {'Accept': 'application/json',
             'Authorization': 'SableBasic GetProductMetadata'}

data = {}

MP_ID = 1
x_asin = 'B0BLK3MKJV'


sable_url = "http://sable-responders-adhoc-iad.iad.proxy.amazon.com/datapath/query/catalog/item/-/" \
                    + str(MP_ID) + "/" \
                    + str(x_asin) \
                    + "?languages%3D[en_US]"

r = requests.get(sable_url, headers=Myheaders, auth=kerberos_auth, verify=False)

jresponse = r.json()

data['SABLE'] = json.dumps(jresponse)


f = open(r'C:\Users\kethos\Downloads\part-00000-f1b070cd-63f1-49e9-9d4e-01e4dd02aced-c000.json')

d = json.loads(f.readline())

for i in d['Output']:
    a = json.loads(i)
    data['BYODOutput'] = {}
    data['BYODOutput']['output'] = a['result']
    break

print(attribute_present_in_bp(data))
