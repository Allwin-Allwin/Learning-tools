"""
Welcome!,Its a special tool for students who wants to learn about web development 
It simply get the url and return its original source code as a file 

Usage :

    -python URLSRC.py -url example.com
"""
# Importing required modules

from requests import get as _get
import os, sys

def getURL() :
	global url
	url = input("Enter Target URL :")
	if "https://" in url:
			if url[0:8] == "https://":
				pass
			else:
				print("URL ERROR \nCheck URL ")
				Terminate()
	else:
		url = "https://" + url
	print(url)									#TESTING
	return url

def getSRC(url):
	try :
		http_request = _get(url)
		if http_request.status_code != 200 :
			print("ERROR Code ",http_request.status_code)
			Terminate()
		src_code = str(http_request.text)

	except :
		print("ERROR OCCURED IN GETTING SRC...\nTry Again")
		Terminate()
	writeInFile(src_code)

def writeInFile(src_code):
	path = os.getcwd() + "/URLSRC"
	os.chdir(path)
	filename = input("Enter File Name:")
	file = open(filename,'w')
	file.write(str(src_code))
	file.close()
	print(src_code)
	print(f"Copy is Stored at {path} with name {filename}")
	Terminate()


def main():
	global url 
	if len(sys.argv) == 1:
		url = getURL()

	else :
		try :
			_index = sys.argv.index('-url')
			url = sys.argv[_index + 1]
			if "https://" in url:
				if url[0:8] == "https://":
					pass
				else:
					print("URL ERROR \nCheck URL ")
					Terminate()
			else:
				url = "https://" + url


			print(url) 										#TESTING
		except ValueError :
			print("ERROR OCCURED ENTER URL AGAIN")
			url = getURL()
	getSRC(url)


def Terminate():
	sys.exit()




if __name__ == "__main__" :
	main()
