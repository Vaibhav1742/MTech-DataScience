import requests

response = requests.get("https://isro.vercel.app/api/spacecrafts")
data = response.json()
print('no of main keys  - ', len(data))
print('Main keys - ')
for i in data:
    print(i)

print('Total Num of spacecrafts  - ', len(data['spacecrafts']))

for i in range(0,len(data["spacecrafts"])):
    print(data['spacecrafts'][i]['id'], ':', data['spacecrafts'][i]['name'])

userinput = input('Enter the name of space craft: ')

for i in range(0,len(data["spacecrafts"])):
    if userinput == data['spacecrafts'][i]['name']:
        print('Found')
else:
    print('Not Found')
