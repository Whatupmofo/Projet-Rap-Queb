#coding: utf-8


import json
import csv
import re 
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.tokenize import MWETokenizer


artist_keys = ["Loud(Canada)","LaryKidd","LoudLaryAjust","Koriass","FouKi","AlaclairEnsemble","DeadObies","Kirouac","LaF(Montreal)","SansPression","RoiHeenok","Souldia","ObialeChef","Sarahmée","Marie-Gold(Canada)","ManuMilitari","O.G.B(Canada)","Rymz","LesAnticipateurs","LocoLocass","Taktika","IZZY-S","Dubmatique","Tizzo","Muzion","Rainmen","LaConstellation","AtachTatuq","Omnikrom","Telus","K6A","SirPathétik","K-maro","Connaisseur","Vendou","BrownFamily","Rowjay" ,"YesMccan","Lost[FR]","JayScøttXSmittyBacalley","STxLIAM","KenLo","EmanXVlooper","Enima","White-B","SebaetHorg","MaybeWatson","Anodajay","JoeRocca","BadNylon","OstiOne","M.B"]

y = str(artist_keys)


for y in artist_keys:
	fichier = "rap_" + y + ".csv"

	file_name = "Lyrics_" + y + ".json"

	json_data=open(file_name).read()

	data = json.loads(json_data)

	for i in range(0,len(data["songs"])):


		lyrics = str(data["songs"][i]["lyrics"].lower().replace("["," ").replace("1er"," ").replace("]"," ").replace("couplet"," ").replace(","," ").replace("!"," ").replace("?"," ").replace("("," ").replace(")"," ").replace("2e"," ").replace("refrain"," ").replace("hook"," ").replace("pre-hook"," ").replace("..."," ").replace("'","_").replace("’","_").replace("2ième"," ").replace("verse"," ").replace("outro"," ").replace("«"," ").replace("»"," ").replace("3e"," ").replace("3ième"," ").replace("pre-refrain"," ").replace("-"," ").replace("‘"," ").replace(":"," "))
	
		token = nltk.word_tokenize(lyrics)
		count = {}

		for word in token:
			infos = []
			infos.append(data["songs"][i]["artist"]) 
			infos.append(data["songs"][i]["title"]) 
			infos.append(data["songs"][i]["album"]) 
			infos.append(data["songs"][i]["year"])
			infos.append(word.replace("_","'"))

			if word in count:
				count[word] += 1
			else:
				count[word] = 1

		artist = data["songs"][i]["artist"]
		album = data["songs"][i]["album"]
		title = data["songs"][i]["title"]
		# print(artist)
		# print(album)	
		# print(title)
		# print(len(count.keys()))
		# print("________")
		for album in artist:
			total = len(count.keys())
			print(total)

			# f2 = open(fichier, "a")
			# z = csv.writer(f2)
			# z.writerow(infos)
	# artist = data["songs"][i]["artist"]
	
	# title = data["songs"][i]["title"]
	# print(artist)
	# print(title)
	# print(count)






		
		



		
	













			








