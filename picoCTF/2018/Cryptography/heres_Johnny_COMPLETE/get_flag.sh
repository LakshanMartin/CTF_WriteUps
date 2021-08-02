#!/bin/bash

#  BEFORE RUNNING THIS SCRIPT:
#   1 - Obtain rockyou.txt password list from 
#	https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt
#
#   2 - Use John The Ripper to brute force the password with the 
#	rockyou.txt file.
#  	example: john --wordlist=rockyou.txt shadow
#			[shadow] being the file containing the hashed password

(echo 'root'; echo 'password1') | nc 2018shell.picoctf.com 42165 | 
	grep -o "picoCTF{.*}" --color=none

