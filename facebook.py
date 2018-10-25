# coding:utf-8

import requests
import time
import pickle
import random
token = 'EAANtG5nmr70BAHYsogbTNpNvrdnumF4miWufZA50Ec2b24Dxip500PsXXvFuY2RrCZB33OD6UyZBZBN4kWDDlE0XDIZCchzOGL9llEFrz2YYeGbGtEZAE90DoHH6RBoGyilwL2FwVbskvSJfeIh5v9ZClpGkue9XeNLPf8SZBNTkRevL9LOyMjBribqN9ybNQZBnAS087zq3dXRZBaXJZAOQZCU5yqLcgBzHOEGMUH6uEKZCynwZDZD'

# results = r.json()

def req_facebook(req):
    r = requests.get('https://graph.facebook.com/v3.1/' + req , {'access_token' : token})
# me?fields=id,meeting_for,address
    return r

# req="/posts?fields=comments,likes&limit=4"
req="me?fields=last_name%2Cfirst_name"
results =req_facebook(req).json()
print(results)

data=[]

i=0
while True:
    try:
        time.sleep(random.randint(2.5))
        data.extend(results['pagina']['next'])
        results=r.json()
    except:
        print("done")
        break

# pickle.dump(data,open("steam_data.pkl","wb"))
# loaded_data=pickle.load(file=open("steam_data.pkl"))
