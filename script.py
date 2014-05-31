# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys

def cmpval(x,y):
	if (x[3] < y[3]):
		return -1
	elif (x[3] == y[3]):
		if (x[0] > y[0]):
			return -1
		elif (x[0] == y[0]):
			return 0
		else:
			return 1
	else:
		return 1

def raw_input_low(str):
	return (raw_input(str)).lower().strip().decode(sys.stdin.encoding)

def load_dict():
	try:
		File = open("dict.stxt")
	except BaseException, e:
		print e
		return None
	else:
		d = []
		i = 0
		for line in File:
			if (len(line) >= 5):
				sline = line.strip()
				d.append((sline[3:], sline[0], sline[1]))
				#NomLieu , Ecole , Normal?
				i += 1
		File.close()
		return (d, i)

def load_scores(File, N):
	d = []
	PPPPP = []
	i = 0
	for line in File:
		if (len(line) > 3):
			sline = line.strip().split(' ')
			if (i < N):
				d.append([int(sline[0]), int(sline[1])])
				i += 1
			else:
				#print str(i) + "e"
				PPPPP.append([int(sline[0]), int(sline[1]), int(sline[2])])
	return (d, PPPPP)

def save_scores(File, d, PPPPP):
	File.seek(0)
	for EEEEE in d:
		File.write(str(EEEEE[0]))
		File.write(" ")
		File.write(str(EEEEE[1]))
		File.write("\n")
	for EEEEE in PPPPP:
		File.write(str(EEEEE[0]))
		File.write(" ")
		File.write(str(EEEEE[1]))
		File.write(" ")
		File.write(str(EEEEE[2]))
		File.write("\n")
	File.flush()

def create(SSSSS, DDDDD):
	try:
		File = open(SSSSS, "w+")
	except BaseException, EEEEE:
		print EEEEE
		return None
	else:
		AAAAA = []
		BBBBB = []
		for KKKKK in DDDDD:
			File.write("0 0\n")
			AAAAA.append([0, 0])
		for KKKKK in range(0, 10):
			File.write("0 0 0\n")
			BBBBB.append([0, 0, 0])
		File.flush()
		return (File, AAAAA, BBBBB)

def file_load():
	SSS = raw_input_low("Entrez le nom du fichier (sans le .txt): ")
	if (SSS != "quit"):
		try:
			FFF = open(SSS + ".txt", "r+")
		except BaseException, e:
			print e
			return None
		else:
			(Scores, mScores) = load_scores(FFF, ndict)
			i = 0
			for el in Scores:
				print dict[i][0], ": "+nsep(el[0])
				i += 1
			print ""
			for el in mScores:
				print dict[el[0]][0], ": "+nsep(el[1])
			print ""
			return (FFF, Scores, mScores, SSS)

"""
maxdict compte le nombre de lieux pour chaque ecole et en retourne une liste
"""
def maxdict(DDDDD):
	LLLLL = {}
	for EEEEE in DDDDD:
		if (int(EEEEE[1]) not in LLLLL):
			LLLLL[int(EEEEE[1])] = 1
		else:
			LLLLL[int(EEEEE[1])] += 1
	#print LLLLL
	return [LLLLL[0], LLLLL[1], LLLLL[2], LLLLL[3], LLLLL[4]]

def m8(n):
	if (n > 8):
		return 8
	else:
		return n

def nsep(n):
	k = list(str(n))
	s = ""
	k.reverse()
	i = 0
	for c in k:
		i += 1
		s = c+s
		if (i%3 == 0 and i != len(k)):
			s = '.'+s
	#print s
	return s

def genere(FFFFF, sdict, sbdict, dict, mdict, scores, mscores, max):
    FFFFF.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
    FFFFF.write('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">\n')
    FFFFF.write('\t<head>\n')
    FFFFF.write('\t\t<title>Statistiques NaturalChimie 2</title>\n')
    FFFFF.write('\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf8"/>\n')
    FFFFF.write('\t\t<link rel="stylesheet" media="screen" type="text/css" title="Design" href="css.css"/>\n')
    FFFFF.write('\t</head>\n')
    FFFFF.write('\t<body>\n')
    FFFFF.write('\t\t<table><tr>\n')
    trilist = []
    i = 0
    for e in dict:
        trilist.append([int(scores[i][0]), int(scores[i][1]), e[0], int(e[1])])
        i += 1
    #print trilist
    #print ""
    trilist.sort(cmpval)
    i = 0
    k = 0
    for e in sbdict:
        FFFFF.write('\t\t<td><table class="'+sdict[i]+'">\n')
        FFFFF.write('\t\t\t<tr><td colspan="2"><img alt="1" src="' + e + '.png"></td></tr>\n')
        FFFFF.write('\t\t\t<tr><td>Lieu</td><td>Score</td></tr>\n')
        j = 0
        while (j < mdict[i]):
            print trilist[k]
            FFFFF.write('\t\t\t<tr><td>')
            FFFFF.write(str(trilist[k][2]))
            FFFFF.write('</td><td><span class="' + str(sdict[trilist[k][1]]) + '">' + nsep(trilist[k][0]) + '</span></td></tr>\n')
            j += 1
            k += 1
        while (j < max):
            j += 1
            FFFFF.write('\t\t\t<tr><td></td><td></td></tr>\n')
        FFFFF.write('\t\t\t<tr><td colspan="2"><img alt="1" src="' + e + '.png"></td></tr>\n')
        FFFFF.write('\t\t</table></td>\n')
        i += 1
    FFFFF.write('\t\t</tr></table>\n')
    FFFFF.write('\t\t<table><tr><td><table class="Rank">\n')
    FFFFF.write('\t\t\t<tr><td><img alt="Numero" src="p0.png"></td><td>Scores</td><td>Lieux</td></tr>\n')
    FFFFF.write('\t\t\t<tr class="Gold"><td><img alt="1" src="p1.png"></td><td><span class="')
    FFFFF.write(sdict[int(mscores[0][2])])
    FFFFF.write('M">')
    FFFFF.write(nsep(mscores[0][1]))
    FFFFF.write('</span></td><td><span class="')
    FFFFF.write(sdict[int(dict[int(mscores[0][0])][1])])
    FFFFF.write('M">')
    FFFFF.write(dict[int(mscores[0][0])][0])
    FFFFF.write('</span></td></tr>\n')
    FFFFF.write('\t\t\t<tr class="Silv"><td><img alt="2" src="p2.png"></td><td><span class="')
    FFFFF.write(sdict[int(mscores[1][2])])
    FFFFF.write('M">')
    FFFFF.write(nsep(mscores[1][1]))
    FFFFF.write('</span></td><td><span class="')
    FFFFF.write(sdict[int(dict[int(mscores[1][0])][1])])
    FFFFF.write('M">')
    FFFFF.write(dict[int(mscores[1][0])][0])
    FFFFF.write('</span></td></tr>\n')
    FFFFF.write('\t\t\t<tr class="Iron"><td><img alt="3" src="p3.png"></td><td><span class="')
    FFFFF.write(sdict[int(mscores[2][2])])
    FFFFF.write('M">')
    FFFFF.write(nsep(mscores[2][1]))
    FFFFF.write('</span></td><td><span class="')
    FFFFF.write(sdict[int(dict[int(mscores[2][0])][1])])
    FFFFF.write('M">')
    FFFFF.write(dict[int(mscores[2][0])][0])
    FFFFF.write('</span></td></tr>\n')
    i = 3
    while (i < 10):
        FFFFF.write('\t\t\t<tr><td><img alt="' + str(i+1) + '" src="p' + str(m8(i+1)) + '.png"></td><td><span class="' +\
        sdict[int(mscores[i][2])] + '">' + nsep(mscores[i][1]) + '</span></td><td><span class="' +\
        sdict[int(dict[int(mscores[i][0])][1])] + '">')
        FFFFF.write(dict[int(mscores[i][0])][0])
        FFFFF.write('</span></td></tr>\n')
        i += 1
    FFFFF.write('\t\t</table></td></tr></table>\n')
    FFFFF.write('\t</body>\n')
    FFFFF.write('</html>\n')

#print dict

#print str

namefile = ""
(dict, ndict) = load_dict()
mdict = maxdict(dict)
max = max(mdict)
scores = None
mscores = None
sdict = ("Guil", "Aude", "Gemi", "Kash", "Jeez")
sbdict = ("igub", "iapb", "igmb", "iskb", "ijzb")
Str = "1"
file = None
var = None
#print sys.stdout.encoding
while (Str != "quit"):
	Str = raw_input_low("Que voulez-vous faire? (help pour aide) ")
	if (Str == "help"):
		print "-\"quit\": quitter le programme, ou le menu courant"
		print "-\"load\": charger un fichier"
		print "-\"save\": sauver le fichier courant"
		print "-\"insert\": insérer un score dans le fichier courant"
		print "-\"insert-help\": obtenir l'aide du mode \"insert\""
		print "-\"create\": créer un fichier vierge"
		print "-\"unlock\": libérer le fichier courant"
		print "-\"genere\": générer le fichier HTML"
		print "NB: tous les noms de fichier sont autorisés, sauf \"quit.txt\""
	elif (Str == "insert-help"):
		print "Les écoles et lieux sont représentés par un numéro suivant la liste:"
		i = 0
		print "Écoles:"
		for ecole in sdict:
			print str(i) + " :\t" + ecole
			i += 1
		print "\nLieux:"
		i = 0
		for lieu in dict:
			print str(i) + " :\t" + lieu[0].decode("utf8")
			i += 1
	elif (Str == "load"):
		if (file != None):
			if (raw_input_low("Voulez-vous fermer le fichier actuel? (Y/N) ") == "y"):
				file.close()
				var = file_load()
				if (var != None):
					(file, scores, mscores, namefile) = var
		else:
			var = file_load()
			if (var != None):
				(file, scores, mscores, namefile) = var
	elif (Str == "save"):
		if (file != None):
			save_scores(file, scores, mscores)
			print "Sauvegarde OK"
		else:
			print "Échec de la sauvegarde: aucun score chargé"
	elif (Str == "insert"):
		if (file == None):
			print "Erreur: aucun fichier chargé"
		else:
			Str = raw_input_low("Entrez le score a inserer (lieu score ecole): ")
			if (Str == "quit"):
				Str = "1"
			else:
				Str = Str.split(' ')
				try:
					Str[0] = int(Str[0])
					Str[1] = int(Str[1])
					Str[2] = int(Str[2])
					if (Str[2] not in {0, 1, 2, 3, 4} or Str[0] < 0 or Str[0] >= ndict):
						raise BaseException("list index out of range")
				except BaseException, EEEEE:
					print EEEEE
				else:
					if (scores[Str[0]][0] < Str[1]):
						print "Ancien record: "+nsep(scores[Str[0]][0])+" ; nouveau record: "+nsep(Str[1])
						scores[Str[0]][0] = Str[1]
						scores[Str[0]][1] = Str[2]
					else:
						print "Meilleur score: "+nsep(scores[Str[0]][0])+" ; votre score: "+nsep(Str[1])
					i = 9
					while (i >= 0 and mscores[i][1] < Str[1]):
						i -= 1
					i += 1
					#if (dict[Str[0]][2] == '1'): pour eviter les mines dans le classement
					if (dict[Str[0]][2] == '1'):
						mscores.insert(i, [Str[0], Str[1], Str[2]])
						if (i == 10):
							pass
						else:
							def mlsk_1d56f(n):
								if (n == 0):
									return "-er"
								else:
									return "-eme"
							print "C'est le "+str(i+1) + mlsk_1d56f(i) + " meilleur score!"
							print "Score battu: "+nsep(mscores[i+1][1])
						popped = mscores.pop()
					print ""
	elif (Str == "create"):
		if (file != None):
			if (raw_input_low("Voulez-vous fermer le fichier actuel? (Y/N) ") == "y"):
				file.close()
				file = None
			Str = "1"
		if (file == None):
			Str = raw_input_low("Entrez le nom du fichier (sans le .txt): ")
			if (Str != "quit"):
				(file, scores, mscores) = create(Str + ".txt", dict)
				namefile = Str
			else:
				Str = "1"
	elif (Str == "genere"):
		if (file == None):
			print "Erreur: aucun fichier chargé"
		else:
			try:
				htmlfile = open(namefile + '.html', "w+")
			except BaseException, E:
				print E
			else:
				genere(htmlfile, sdict, sbdict, dict, mdict, scores, mscores, max)
				print "Fichier HTML écrit"
				htmlfile.close()
	elif (Str == "unlock" or Str == "quit"):
		if (file != None):
			file.close()
			file = None

