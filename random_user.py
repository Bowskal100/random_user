# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:32:57 2020

@author: sshobowale
"""

#!/bin/python3

import requests, json
import prometheus_client
import time
from flask import Response, Flask
from prometheus_client import Info

app = Flask(__name__)

REQUEST_GENDER = Info('rand_user_gender', 'Gender of Random user')

@app.route("/")
def get_user():
    start = time.time()
    req = requests.get('https://randomuser.me/api/')
    end = time.time()
    
    request_time = str(end - start)   #calculate how long request takes

    print(req.json())
    user_info = req.json()['results'][0]


    #parse request response object    
    rand_user_first_name = user_info['name']['first']
    rand_user_last_name = user_info['name']['last']
    rand_user_location_street = str(user_info['location']['street']['number']) + ' ' + user_info['location']['street']['name']
    rand_user_location_city = user_info['location']['city']
    rand_user_location_state = user_info['location']['state']
    rand_user_location_country = user_info['location']['country']
    rand_user_location_postcode = user_info['location']['postcode']
    rand_user_gender = user_info['gender']
    
    rand_user_name = rand_user_first_name + ' '+ rand_user_last_name
    rand_user_address = rand_user_location_street + ', ' + rand_user_location_city + ', ' + rand_user_location_state + ', ' + rand_user_location_country + ' ' + str(rand_user_location_postcode) 
    
    print(rand_user_name)
    print(rand_user_address)


    raw_response = {
        'name':  rand_user_name,
        'address': rand_user_address
    }

    json_response = json.dumps(raw_response, ensure_ascii=False).encode("utf8")

    REQUEST_GENDER.info({'rand_user_gender': rand_user_gender, 'response_time': request_time })
    
    return Response(json_response.decode(), content_type='application/json')
    
@app.route("/metrics")
def get_metrics():  
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")

#print(rand_user_name)
#get_user()
if __name__ == "__main__":
    app.run()