#!/bin/bash

zsteg husky.png | grep -oE "picoCTF{.*}" --color=none > flag.txt
