from colorama import *
import requests
import profile as profile
import platform
import os
import time
import sys

def convertTuple(tup):
		        # initialize an empty string
		    str = ''
		    for item in tup:
		        str = str + item
		    return str

def request():
    r = requests.get(url, stream=True)
    with open(output, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

folderName = "xnsl649dwttbhc2"
errorText = Fore.RED
normalText = Fore.BLUE
sysText = Fore.GREEN
downloadText = Fore.YELLOW
normalText = Fore.WHITE

match platform.system():
	case "Windows":
		os.system("cls")
	case "Linux":
		os.system("clear")

print(sysText)
print()
print(platform.platform())
print()
print(platform.system())
print()
print(os.name)
os.system("ls")
print()
os.system("mkdir Scripts")
print()
print(os.getcwd())
print()
print(len(sys.argv))
print()
os.system("ls")

time.sleep(1)

if "-download" in sys.argv:
	print("Download")
	indexDownload = sys.argv.index("-download")
	try:
		fileToDownload = sys.argv[indexDownload + 1]
		print(downloadText)
		url = "https://raw.githubusercontent.com/lucidblu08/lucid/main/", fileToDownload, ".py"
		url = convertTuple(url)
		tuple = "Scripts/", url[56:len(url)]
		str = convertTuple(tuple)
		print(len(url) - 13)
		print()
		print(str)
		print("Downloading", url[56:len(url)])
		output = str
		profile.run('request()')
		pass
	except:
		print(errorText)
		print("Invalid arguments\nExample python3 downloader.py -download\nIn this case the file to download is missing")
if "-update" in sys.argv:
	print("Update")
	try:
		fileToDownload = "downloader"
		print(downloadText)
		url = "https://raw.githubusercontent.com/lucidblu08/lucid/main/", fileToDownload, ".py"
		url = convertTuple(url)
		tuple = "", url[56:len(url)]
		str = convertTuple(tuple)
		print(len(url) - 13)
		print(str)
		print("Updating", url[56:len(url) - 5])
		output = str
		profile.run('request()')
		pass
	except:
		print(errorText)
		print("An error occured")
if "-testupdate" in sys.argv:
	print("Update")
	try:
		fileToDownload = "downloader"
		print(downloadText)
		url = "https://raw.githubusercontent.com/lucidblu08/lucid/main/", fileToDownload, ".py"
		url = convertTuple(url)
		tuple = "test_", url[56:len(url)]
		str = convertTuple(tuple)
		print(len(url) - 13)
		print(str)
		print("Updating", url[56:len(url) - 5])
		output = str
		profile.run('request()')
		pass
	except:
		print(errorText)
		print("An error occured")
if "-help" in sys.argv:
	print(downloadText)
	print("Help:\n-download {file name}\n-help\n-update\n\nExample:\npython3 downloader.py -download passwordmaster -update -help")
