import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit()

user_input = sys.argv[1]

try:   
    number = float(user_input)
    print("Float value:", number)

except ValueError:  
    print(f"Error: '{user_input}' is not a valid float.")
    sys.exit()


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# print(json.dumps(response.json(), indent=2))

x = response.json()
#for result in o[""]:
#   print(result["rate"])
print(x["bpi"]['USD']['rate'], "USD")

#value = x["bpi"]['USD']['rate']









    

