import requests

response = requests.get("https://inshortsapi.vercel.app/news?category=sports")
data = response.json()
print('Main keys- ', len(data))
print('Main keys are - ')
for i in data:
    print(i)

print('Total news- ', len(data['data']))

for i in range(0,len(data["data"])):
    print(i+1,'News: ',data['data'][i]['content'], ', Author: ', data['data'][i]['author'],', Date: ', data['data'][i]['date'])