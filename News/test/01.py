import requests
import json

url = "http://192.168.244.192:8000/api/format"

data={
    "time":"31 January 2022"
}

headers = {
            "Content-Type": "application/json"
}
resp = requests.post(url,headers=headers,data=json.dumps(data))

print(resp.json())