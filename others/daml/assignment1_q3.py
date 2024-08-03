import matplotlib.pyplot as plt
import  requests

url1 = requests.get("https://isro.vercel.app/api/spacecrafts")
data1 = url1.json()
url2 = requests.get("https://isro.vercel.app/api/customer_satellites")
data2 = url2.json()

isrodata = [len(data1['spacecrafts']),len(data2["customer_satellites"])]
plt.pie(isrodata,labels=['ISRO INDIA WORK','FOREIGN WORK'],autopct='%1.0f%%')
plt.show()