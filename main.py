import subprocess
from maclookup import ApiClient
import logging

out = subprocess.Popen(['hcitool', 'con'],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
stdout, stderr = out.communicate()
ans = stdout.decode('utf-8')
mac_address = ans[20:38]
client = ApiClient('at_3XhxcPo9m1JSaQg1Atow8fCHyGgZ2')
logging.basicConfig(filename='myapp.log', level=logging.WARNING)
response = client.get(mac_address)
mac_address = "MAC Address is: "+mac_address
lines = [mac_address,
         "Company Name: "+response.vendor_details.company_name,
         "Company Address: "+response.vendor_details.company_address]
with open('output.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
