import os
from config_module import *
import time 

class ModuleCreator:
	# Classe permettant de créer un module pour le FReveil
	def __init__(self):
		#self.version = "1"
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
		print()
		self.ressourceAudio = input("Souhaitez-vous utiliser de l'audio (musique ou synthèse vocale par exempel) dans ce module (o/N) ? ")


	def creeDossier(self):
		# Fonction allant cree le dossier du module
		self.nomDossier = self.nom .replace(" ","_")+os.sep
		Outils.creeDossier(self.nomDossier)

	def configModule(self):
		# Fonction qui va créer le fichier de configuration du module
		c = ConfigModule(self.nomDossier)
		c.setNom(self.nom)
		c.setArduino(self.arduino)
		c.setRessourceAudio(self.ressourceAudio)


	def createFile(self):
		# Fonction allant copier/créer les fichiers nécéssaires au fonctionnement du module
		temps_tab = time.localtime()
		c = ConfigModule(self.nomDossier)
		chaine2 = ""
		chaine3 = ""
		if (c.ressourceAudio):
			chaine2 = """
def giveRequestAudio(id):
	# Lache l'autorisation d'utiliser l'audio pour qu'un autre module puisse l'utiliser.
	conf.setLockAudio(False,id)

def requestAudio(): 
	# Demande l'autoristion d'utiliser l'audio. Cette méthode est bloquante jusqu'à ce que l'autorisation soit donnée.
	conf = Config ()
	id = conf.getId()
	audio =  0
	while audio != 1:
		audio = conf.setLockAudio(True,id)
	return id
"""

			chaine3 = """
	# Le code qui suit jusqu'à #FIN est un code pour recuperer l'exclusivité pour utiliser l'audio au sein du FReveil.
	# Il suffit d'insérer votre code utilisant l'audio à l'endroit indiquer.
	# A chaque fois que vous souhaitez utiliser l'audio vous devriez utiliser ce code :

	id = requestAudio()
	# Votre code utilisant l'audio
	giveRequestAudio(id)

	#FIN
			"""
		chaine = """\"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : {}
Nom initial du module : {}

\"""
from config_module import *
from config import *

def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	{}
	pass

{}
		""".format("{}_{}_{}".format(temps_tab[0],temps_tab[1],temps_tab[2]),self.nom,chaine3, chaine2)
		Outils.ecrireFichier(self.nomDossier+"module.py",chaine)
		chaine = Outils.lireFichier("outils.py")
		Outils.ecrireFichier(self.nomDossier+"outils.py",chaine)
		chaine = Outils.lireFichier("config_module.py")
		Outils.ecrireFichier(self.nomDossier+"config_module.py",chaine)
		chaine = Outils.lireFichier("interface_config_module.py")
		Outils.ecrireFichier(self.nomDossier+"interface_config_module.py",chaine)



a = ModuleCreator()