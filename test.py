import requests
url = "https://notify-api.line.me/api/notify"
payload = ({'message':'Hello'})
files=[
  ('imageFile',('prayutt.jpg',open('./prayutt.jpg','rb'),'image/jpeg'))
]
headers = {
  'Authorization': 'Bearer zk7i0DIolDjpMM9uCW19NwFVg69s1ghqwENYCGXPBbB'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)