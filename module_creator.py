import os
from config_module import *
import time 

class ModuleCreator:
	# Classe permettant de créer un module pour le FReveil
	def __init__(self):
		self.annonce()
		self.demandeInfos()
		self.creeDossier()
		self.configModule()
		self.createFile()


	def annonce(self):
		# Annonce et crédit du programme
		print("Bienvenue dans l'interface de création d'un module du FReveil.")
		print("Ce programme a été crée par Fayçal Bousmaha.")
		print()
		print()

	def demandeInfos(self):
		# Fonction demandant toutes les informations nécéssaires à la création du module
		print("Ne vous inquietez-pas ces informations seront modifiable ulterieurement en utilisant interface_config_module.py")
		print()
		self.nom = input("Quel est le nom du module ? ")
		print()
		self.arduino = input("Ce module compte-il communiquer avec l'Arduino (o/N) ? ") == "o"


	def creeDossier(self):
		# Fonction allant cree le dossier du module
		self.nomDossier = self.nom .replace(" ","_")+os.sep
		Outils.creeDossier(self.nomDossier)

	def configModule(self):
		# Fonction qui va créer le fichier de configuration du module
		c = ConfigModule(self.nomDossier)
		c.setNom(self.nom)
		c.setArduino(self.arduino)


	def createFile(self):
		# Fonction allant copier/créer les fichiers nécéssaires au fonctionnement du module
		temps_tab = time.localtime()
		chaine = """\"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : {}
Nom initial du module : {}

\"""

def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	pass
		""".format("{}_{}_{}".format(temps_tab[0],temps_tab[1],temps_tab[2]),self.nom)
		Outils.ecrireFichier(self.nomDossier+"module.py",chaine)
		chaine = Outils.lireFichier("outils.py")
		Outils.ecrireFichier(self.nomDossier+"outils.py",chaine)
		chaine = Outils.lireFichier("config_module.py")
		Outils.ecrireFichier(self.nomDossier+"config_module.py",chaine)
		chaine = Outils.lireFichier("interface_config_module.py")
		Outils.ecrireFichier(self.nomDossier+"interface_config_module.py",chaine)



a = ModuleCreator()