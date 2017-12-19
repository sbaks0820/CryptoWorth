#!/usr/bin/python
import json, requests, time
import urllib3

urllib3.disable_warnings()
BASE = 'https://api.coinmarketcap.com/v1/ticker/'

d = json.load(open('/home/surya/projects/tools/cryptoworth/balances.json'))
values = []
print '%30s | %10s | %10s | %10s' % ('Currency', 'Price', 'Amount', 'Value')
print '-'*(3*3 + 30 + 10 + 10 + 10)
for name,balance in d.iteritems():
    url = BASE + name + '/'
    r = requests.get(url, verify=False)
    assert r.status_code == 200, "status_code:%s" % str(r.status_code)
    r = r.json()[0]
    name = r['name']
    price = float(r['price_usd'])
    total = price * balance
    values.append(total)
    print '%30s | %10.2f | %10s | %10.2f ' % (name, price, str(balance), total)
    time.sleep(1)

print '-'*(3*2 + 30 + 10 + 4) + '%6s : %10.2f' % ('TOTAL', sum(values)) 

