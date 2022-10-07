import requests

num = input("[*] Enter the number: ")
url = "https://api.apilayer.com/number_verification/validate?number=" + str(num)

payload = {}
headers = {
    "apikey": "6mY9LLuDF7AZx3oB1R0wWWKv2Uk4V6ql"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text
print(result)
