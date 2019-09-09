import datetime
import json
import httplib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = 'https://dsp.corpo.t-mobile.pl/npitapi/pn/saveAll';
headers = {'content-type': 'application/json'}
pay= {
        "msisdn": "483260329",
        "date_from": "2019-04-25T18:30:00.000+0000",
        "date_to": "2019-04-24T18:30:00.000+0000",
        "opr_recpn_id": 5,
        "date_last": "2019-04-21T18:30:00.000+0000"
}

response = requests.post(url, data=pay,verify=False,headers=headers) 
print(response.text,response.status_code)