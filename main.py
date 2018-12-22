import time
import os

amountJSFile = open("data.js", "r")

amount = int(amountJSFile.read().split("\"")[1])

amountJSFile.close()

while True:
	amount += 1;
	os.system('streamer -s 640x360 -o images/img_' + str(amount) + '.jpeg -c /dev/video0')
	amountJSFileWrite = open("data.js","w")
	amountJSFileWrite.write("var amountData = \"" + str(amount) + "\"")
	amountJSFileWrite.close()
	time.sleep(0.75)
