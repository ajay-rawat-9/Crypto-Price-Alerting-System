import time,json,conf,requests
from boltiot import Bolt
from datetime import datetime
def fetch_price(f,t):
    URL="https://min-api.cryptocompare.com/data/price?fsym="+f+"&tsyms="+t
    response=requests.request("GET",URL)
    response=json.loads(response.text)
    current_price=response[t]
    return current_price
fsymbol="BTC"
print("Enter the CRYPTO you want to be monitored:")
print("1. Bitcoin\n2. Etherium\n3. Dogecoin\n4. Enter the symbol for crypto")
choice=int(input())
if choice==1:
    fsymbol="BTC"
elif choice==2:
    fsymbol="ETH"
elif choice==3:
    fsymbol="DOGE"
elif choice==4:
    fsymbol=input()
else:
    fsymbol="BTC"
print("Enter the currency in terms of which you wish to monitor",fsymbol)
print("1. INR\n2. USD\n3. EUR")
choice=int(input())
tsymbol="INR"
if choice==2:
    tsymbol="USD"
elif choice==3:
    tsymbol="EUR"
else:
    tsymbol="INR"
print("Enter the selling threshold value:")
s_threshold=int(input())
print("Enter the buying threshold value:")
b_threshold=int(input())
mydev=Bolt(conf.api_dev,conf.dev_id)
while True:
    price=fetch_price(fsymbol,tsymbol)
    if price>s_threshold:
        print("Current price of",fsymbol,"is",price,"!!")
        print("SELL YOUR CRYPTO NOW!!!!")
        mydev.digitalWrite('0','HIGH')
        time.sleep(3)
        mydev.digitalWrite('0','LOW')
        break
    elif price<b_threshold:
        print("Current price of",fsymbol,"is",price,"!!")
        print("BUY CRYPTO NOW!!!!")
        mydev.digitalWrite('0','HIGH')
        time.sleep(1)
        mydev.digitalWrite('0','LOW')
        time.sleep(1)
        mydev.digitalWrite('0','HIGH')
        time.sleep(1)
        mydev.digitalWrite('0','LOW')
        break
    time.sleep(30)
