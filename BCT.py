import time
import winsound
min = 0
threshold = float(input("enter bitcoin price to be notified at: "))
while min != 480:
    time.sleep(300)  # coinbase api only updates every 5 minutes
    import urllib.request
    req = urllib.request.Request('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
    with urllib.request.urlopen(req) as response:
        read = response.read()
    raw = str(read[132:139])
    current_price = ''.join(c for c in raw if c not in ''' b'" ''')
    num_price = float(current_price)
    print("Bitcoin is currently $", num_price, sep='')
    if num_price < threshold:
        winsound.PlaySound("Gilfoyle.wav", winsound.SND_FILENAME)
        print("bitcoin is below efficient mining levels\n")

