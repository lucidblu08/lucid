from colorama import *
import mediafire_dl
import platform
import os
import time
import sys

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
		def convertTuple(tup):
		        # initialize an empty string
		    str = ''
		    for item in tup:
		        str = str + item
		    return str
		url = "https://www.mediafire.com/file/", folderName, "/", fileToDownload, ".py/file"
		url = convertTuple(url)
		tuple = "Scripts/", url[47:len(url) - 5]
		str = convertTuple(tuple)
		print(str)
		print("Downloading", url[47:len(url) - 5])
		output = str
		mediafire_dl.download(url, output, quiet=False)
		pass
	except:
		print(errorText)
		print("Invalid arguments\nExample python3 downloader.py -download\nIn this case the file to download is missing")
if "-update" in sys.argv:
	print("Update")
	try:
		fileToDownload = "downloader"
		print(downloadText)
		def convertTuple(tup):
		        # initialize an empty string
		    str = ''
		    for item in tup:
		        str = str + item
		    return str
		url = "https://www.mediafire.com/file/", folderName, "/", fileToDownload, ".py/file"
		url = convertTuple(url)
		tuple = "", url[47:len(url) - 5]
		str = convertTuple(tuple)
		print(str)
		print("Updating", url[47:len(url) - 5])
		output = str
		mediafire_dl.download(url, output, quiet=False)
		pass
	except:
		print(errorText)
		print("An error occured")