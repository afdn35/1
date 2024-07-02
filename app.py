import requests
import time
import json

def main():
	while True:
		url = "https://api.hamsterkombat.io/clicker/sync"
		headers = {
          'User-Agent': "Mozilla/5.0 (Linux; Android 10; AGRK-L09 Build/HUAWEIAGRK-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Safari/537.36",
          'Accept-Encoding': "gzip, deflate",
          'Authorization': "Bearer 1719540379870ceA8yqtXsJcyHPurPkyxD4bPWOgiChPU30VReBJQa1LKV6fsu84sVRX2wb9D67Ge1298878071",
          'Origin': "https://hamsterkombat.io",
          'X-Requested-With': "org.telegram.plut",
          'Sec-Fetch-Site': "same-site",
          'Sec-Fetch-Mode': "cors",
          'Sec-Fetch-Dest': "empty",
          'Referer': "https://hamsterkombat.io/",
          'Accept-Language': "en,en-EG;q=0.9,ar-QA;q=0.8,ar;q=0.7,en-US;q=0.6"
      }
      
		requests.post(url, headers=headers)
		
		url_x = "https://api.hamsterkombat.io/clicker/tap"
		payload_x = json.dumps({
		"count": 10,
		"availableTaps": 8493,
		"timestamp": 1719551781
		})

		headers_x = {
          'User-Agent': "Mozilla/5.0 (Linux; Android 10; AGRK-L09 Build/HUAWEIAGRK-  L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chme/92.0.4515.105 Safari/537.36",
          'Accept': "application/json",
          'Accept-Encoding': "gzip, deflate",
          'Content-Type': "application/json",
          'authorization': "Bearer 1719540379870ceA8yqtXsJcyHPurPkyxD4bPWOgiChPU30VReBJQa1LKV6fsu84sVRX2wb9D67Ge1298878071",
          'Origin': "https://hamsterkombat.io",
          'X-Requested-With': "org.telegram.plut",
          'Sec-Fetch-Site': "same-site",
          'Sec-Fetch-Mode': "cors",
          'Sec-Fetch-Dest': "empty",
          'Referer': "https://hamsterkombat.io/",
          'Accept-Language': "en,en-EG;q=0.9,ar-QA;q=0.8,ar;q=0.7,en-US;q=0.6"
       }
		
		response_x = requests.post(url_x, data=payload_x, headers=headers_x)
		data = response_x.json()
		availableTaps = data["clickerUser"]["availableTaps"]
		print(availableTaps)
		if availableTaps < 16:
			time.sleep(600)
			main()
main()
