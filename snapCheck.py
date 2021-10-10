#!/usr/bin/python3

"""
Check if a phone number is linked to a SnapChat account.
Author: @crypt0jan
"""

import sys, getopt
import requests
import json
import time

if len(sys.argv) <= 1:
	sys.exit('ERROR: I need at least two arguments. Run the script with -h to learn more.')

def check(countrycode, phonenumber, xsrf_token):
    url = "https://accounts.snapchat.com/accounts/validate_phone_number"
    cookies = {
      "xsrf_token":xsrf_token
    }
    headers = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    data = {"phone_country_code":countrycode,"phone_number":phonenumber,"xsrf_token":xsrf_token}
    request = requests.post(url,data=data,headers=headers,cookies=cookies).json()
    response = str(request)
    #print(response)
    if response.find('OK') >= 0:
        print("Phone number is NOT linked to any account.")
    else:
        print("!! Phone number is LINKED to an account !!")

def main(argv):
    countrycode = ''
    phonenumber = ''
    xsrf_token = 'hLQpFffDQzedKYqbxGEJxM' # Random 22 character string
   
    try:
      opts, args = getopt.getopt(argv,"c:h:p:",["country=","phone="])
   
    except getopt.GetoptError:
      print ('Number of arguments given:', len(sys.argv), 'arguments.')
      print ('Argument list:', str(sys.argv))
      print ('Usage: checkSnap.py -c <countrycode> -p <phonenumber>')
      sys.exit(2)
   
    for opt, arg in opts:
      if opt == '-h':
         print ('Usage: checkSnap.py -c <countrycode> -p <phonenumber>')
         sys.exit()
      elif opt in ("-c", "--country"):
         countrycode = arg
      elif opt in ("-p", "--phone"):
         phonenumber = arg
   
    if (countrycode != "" and phonenumber != ""):
      print ('Country code is :', countrycode)
      print ('Phone number is :', phonenumber)

      # Perform check()
      check(countrycode, phonenumber, xsrf_token)
    else:
        print ('Usage: checkSnap.py -c <countrycode> -p <phonenumber>')
        sys.exit('ERROR: You did not specify the mandatory arguments.')

if __name__ == "__main__":
   main(sys.argv[1:])
