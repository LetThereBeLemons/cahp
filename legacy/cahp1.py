#!/bin/python3

# Cahp1 - A random sentence generator
# A LetThereBeLemons creation
# Liscenced under DONT STEAL MY CODE YOU ASSHOLE (DSMCYA)
version = "c1v80-r3"
release = 0
#* If `release` is 0, it's a test build.
#* Latest release: 1 @ c1v77-r1

import random, build
from random import choice as rc
from time import sleep as ts
from os import name as sysname, system as ex
from sys import exit as sysexit


redrawMode = False
savepath = "./cahp1-save.txt"
premium = False #* This is completely fake, change to True if you find it annoying.
infoStat = None
tipstat = True

# Colours are now imported from cahp1_data.py
#// colours = {}


def clear():
	if sysname == "posix":
		ex("clear")
	elif sysname == "nt":
		ex("cls")
	else:
		print("ERROR:\nUnrecognised system, program has failed.\n")
		sysexit()
clear()



from cahp1_data import *
# Using a python file to store the data makes it easier to add new
# words to the game without modifying the actual logic of the program.


def fin():
	print("\n" + colours["green"] + colours["bold"] + rc(goodbies) + colours["reset"] +"\n")
	ts(0.5)
	sysexit()


if premium == False: punctuation.append(". Upgrade to premium to see the full story!")

def default():
	return colours["green"] + colours["bold"] + "---> " + colours["reset"] + colours["bold"] + rc(adjectives) + " " + rc(things) + " " + rc(hasbeens) + " " + rc(verbs) + " by " + rc(adjectives).lower() + " " + rc(things) + rc(punctuation)

def setPhrase():
	global infoStat
	p, t, s = "promo", "tip", "story"
	choice = rc([s, s, s, s, s, s, s, s, s, s, s, s, s, s, t, t, t, t, t, p])

	if choice == "promo" and premium == False:
		phrase = colours["green"] + colours["bold"] + "Notice: " + colours["reset"] + "Upgrading to premium will get you more, better content!"
		infoStat = "promo"
	elif choice == "tip" and tipstat == True:
		tipchoice = random.randint(0, len(tips)-1)
		phrase = colours["green"] + colours["bold"] + "Tip #" + str(tipchoice) + ": " + colours["reset"] + tips[tipchoice]
		infoStat = "promo"
	elif choice == "story":
		phrase = default()
		infoStat = "availible"

	return phrase



def setInfo():
	name = rc(writtenby_f) + " " + rc(writtenby_l)
	info = "Written by " + name + " on " + rc(["January","February","March","April","May","June","July","August","September","October","November","December"]) + " " + str(random.randint(1, 31)) + ", " + str(random.randint(2016, 2021))
	return info

def main():

	global redrawMode
	clear()
	print("Cahp1 - A LetThereBeLemons creation\nPress h for help, enter for a new story.")
	print("\n" + colours["green"] + colours["bold"] + rc(["Good evening paedophiles.", "I hope you're sitting comfortably.", "Morning all."]) + colours["reset"])

	while True:
		
		if redrawMode == True:
			clear()

		print()

		try:

			phrase = setPhrase()
			info = setInfo()

			if infoStat == "availible":
				phraseinput = input(phrase + "\n" + colours["green"] + colours["bold"] + "   > " + colours["reset"] + info + " ")
			elif infoStat == "me":
				phraseinput = input(phrase + "\n" + colours["green"] + colours["bold"] + "   > " + colours["reset"] + "Written by me about ten seconds ago" + " ")
			elif infoStat == "promo":
				phraseinput = input(phrase + "\n" + colours["green"] + colours["bold"] + "   > " + colours["reset"] + " ")

			if phraseinput == "v":
				print("\nCahp1 version " + str(version))
				print("Cahp1 - A random sentence generator.\nCreated by LetThereBeLemons")
			elif phraseinput == "c":
				clear()
			elif phraseinput == "h":
				print(helppage)
			elif phraseinput == "r":
				if redrawMode == True:
					redrawMode = False
				elif redrawMode == False:
					redrawMode = True
				else:
					print("Error: What?! How?! Huh?!")
			elif phraseinput == "s":
				ex("echo '" + phrase + "' >> " + savepath)
				print("Saved.")
			elif phraseinput == "sp":
				savepath = input("Enter a new path: ")
			elif phraseinput == "build":
				build.build(release)
				sysexit()
			elif phraseinput == "":
				continue
			else:
				print("That's not a valid command. Type h for help.")
			
		except KeyboardInterrupt:
			fin()
		except EOFError:
			fin()

def init():
	prompt = colours["green"] + colours["bold"] + "[Cahp1] " + colours["reset"]

	print("Welcome to Cahp1! Type `h` for help.")

	try:
		while True:
			action = input(prompt)
			if action == "h":
				print("CAHPSHELL HELP:\nType `s` to start Cahp1.\nType `v` to see the version.")
			elif action == "v":
				print("Cahp1 version " + str(version))
			elif action == "s":
				main()
			elif action == "":
				continue
			else:
				print("That's not a valid command. Type `h` for help.")
	except KeyboardInterrupt:
		fin()
	except EOFError:
		fin()


if __name__ == "__main__":
	init()