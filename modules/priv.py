import os

sh = os.system
obj = []
vpns = 5
verbose=1

headers = {"headers": "Kali Linux ; Chrome / 1.0.5 / Safari / iOS"}
cookies = {'JKtOlaCfGQRxpHJxMq3X5MnzBX6A8PHd'}
host = {'Host': 'unknow'}
sh("sc query")
while(verbose<int(vpns)):
	#cmd = sh("ip tunnel show proxy")
	obj.append({
	"headers": headers,
	"cookies": cookies,
	"hostname": host,
	"host": host})
	print(f"[+] VPN No{verbose} creado exitosamente")
	verbose=verbose+1
