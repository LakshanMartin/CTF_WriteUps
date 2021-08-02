#!/bin/bash

curl -s "https://picoctf.com/resources" | grep -oE "picoCTF{.*}" --color=none
