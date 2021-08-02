# admin panel

For this problem we were give a pcap file. I used WireShark to sniff the
packets and found that the traffic across the wire was through HTTP. Therefore,
there was no encryption. 

As a consequence, i was able to use strings on the pcap and grep the flag from
the output.

Script:
    strings data.pcap | grep -oE "picoCTF{.*}" --color=none > flag.txt

Flag:
   picoCTF{n0ts3cur3\_13597b43} 


