#!/bin/bash

strings data.pcap | grep -oE "picoCTF{.*}" --color=none > flag.txt
