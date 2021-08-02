#!/usr/bin/env python3

import base64

cipher = 'dGg0dF93NHNfczFtcEwz'

# following lines to get rid of 'b' in the decoded output
decrypt = base64.b64decode(bytes(cipher, 'utf-8'))
print("picoCTF{%s}" %decrypt.decode('ascii'));
