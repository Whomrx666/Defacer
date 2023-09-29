#date/bin/bash

	apt update && apt upgrade
	apt install python2
        pip2 install requests
        apt install git
        cd /sdcard
	mkdir DEFACER
	cd $HOME
	cd Defacer
        read -p "Enter Untuk Memindahkan Ke sdcard"
	cd
        cd Defacer
	mv -f Defacer.py target.txt /sdcard/DEFACER
	cd /sdcard/DEFACER
        ls
	read -p "ENTER UNTUK MELANJUTKAN"
	clear
        python2 Defacer.py
