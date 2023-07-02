try:
	import aiohttp
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
		print("Downloading")
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
			print("Invalid arguments\nExample python3 main.py -download\nIn this case the file to download is missing")
	if "-update" in sys.argv:
		print("Update")
		try:
			fileToDownload = "main"
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
			fileToDownload = "main"
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
		print("Help:\n-download {file name}\n-help\n-update\n-run\n\nExample:\npython3 main.py -download password -update -help -run password\n\nFiles:\npassword - password mananger with a gui")
	if "-run" in sys.argv:
		print("Running")
		indexRun = sys.argv.index("-run")
		try:
			sys.path.insert(1, 'Scripts')
			fileToRun = sys.argv[indexRun + 1]
			print(sysText)
			__import__(fileToRun)
			pass
		except Exception as e:
			print(errorText)
			print(e)
			print("Invalid arguments\nExample python3 main.py -run\nIn this case the file to run is missing")

except:
	import subprocess
	import sys

	print("Error occured attempting to fix by installing packages please wait")

	# implement pip as a subprocess:
	subprocess.check_call([sys.executable, '-m', 'pip', 'install',
	'colorama'])
	subprocess.check_call([sys.executable, '-m', 'pip', 'install',
	'requests'])
	subprocess.check_call([sys.executable, '-m', 'pip', 'install',
	'aiohttp'])
	
	# process output with an API in the subprocess module:
	reqs = subprocess.check_output([sys.executable, '-m', 'pip',
	'freeze'])
	installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
	installed_packages = str(installed_packages)

	print(installed_packages)
	print()
	print("Please rerun the script")
