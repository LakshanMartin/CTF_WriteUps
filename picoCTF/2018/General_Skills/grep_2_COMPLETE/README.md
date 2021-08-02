grep 2
------

This problem was solved wholly in the picoCTF shell server. 

This problem is similiar to grep 1, but more complex. Basically, the flag is
hidden within one of the several nested directories. We must use the -R flag
for grep to traverse recursively through each directory to locate the flag.

To find the flag:
    grep -R -oE picoCTF{.*}

Flag:
    picoCTF{grep_r_and_you_will_find_24c911ab}
