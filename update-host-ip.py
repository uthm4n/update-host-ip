import requests
from jsonpath_ng import jsonpath, parse
import json
import warnings 

warnings.filterwarnings("ignore")

url = "https://<MORPHEUS-APPLIANCE-URL>/api/servers/<serverID>"

headers = {
    "accept": "application/json",
    "authorization": "Bearer <API-TOKEN>"
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()
netInterface1IP = parse('server.interfaces[0].ipAddress')   # adjust [0] to index of the appropriate interface. 0 = network interface 1, 1 = network interface 2, etc...

finalIP = [match.value for match in netInterface1IP.find(data)]
print(finalIP)

url = "https://<MORPHEUS-APPLIANCE-URL>/api/servers/<serverID>"

payload = {
  "server": {
    "internalIp": f"{finalIP}", 
	"externalIp": f"{finalIP}", 
	"sshHost": f"{finalIP}"
  }
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer <API-TOKEN>"
}

response = requests.put(url, json=payload, headers=headers, verify=False)
print(response.text)
