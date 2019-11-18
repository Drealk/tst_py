import json
import requests

trans_apikey = "trnsl.1.1.20191024T165117Z.57009a074ca3d940.72ace850426e658f63e0c232468aecfb86089638"
dict_apikey = "dict.1.1.20191026T160912Z.9914bb4956bd0ba4.54050504a407c27463ef82f054852724f239b8e7"

urltrans = "https://translate.yandex.net/api/v1.5/tr.json/translate"
urldict  = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"

uilang = "ru"
translang = "en-ru"
entxt = "table"
rutxt = ""

trans_options = {
    'key' : trans_apikey,
    'lang'  : translang,
    'text': entxt
}

dict_options = {
    'key' : dict_apikey,
    'lang': translang,
    'text': entxt,
    'ui'  : uilang
}

# trans_res_request = requests.get(urltrans, params = trans_options)

# print(trans_res_request.status_code)
# print (trans_res_request.text)

dict_res_request = requests.get(urldict, params = dict_options)

print()
print(dict_res_request.status_code)
print(dict_res_request.text)
print()

dict_result = json.loads(dict_res_request.text)

# print (len(dict_result))
print (" части речи: ", len (dict_result['def']))
# print(dict_result['def'])
print ()

for i in dict_result['def']:
    # print (i['pos'])
    print (i.get('pos'), "- количество записей -", len(i['tr']), ":") # количество элементов, описывающих ... (что-то )
    # print (type(i))
    for t in i['tr'] :
        print ("  ", t['text'], " (", len(t), t.keys(),")")
        # print (i['tr'])
        # print ('mean' in t)
        # for k in t.keys():
        #     print (k, t.get(k))
        # print()


# print(len(def_result))
# for i in def_result:
#     print(i)
#     print(type(i))


