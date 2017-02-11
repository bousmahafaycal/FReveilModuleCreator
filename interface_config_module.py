from config_module import *
from time import sleep

class InterfaceConfigModule:
	def __init__(self, localisation):
		self.conf = ConfigModule(localisation)
		self.annonce()
		self.menuPrincipal()
		self.messageFinal()

	def annonce(self):
		# Annonce et crédit du programme
		print("Bienvenue dans l'interface de configuration du module du FReveil.")
		print("Cette interface a été crée par Fayçal Bousmaha.")
		print()
		print()

	def menuPrincipal(self):
		# Menu principal de cette interface
		print()
		liste = ["Quitter","Changer le nom","Gestion de l'arduino"]
		a = Outils.menu("MENU PRINCIPAL",liste)
		print()
		if a == 1:
			self.gestionNom()
		elif a == 2:
			self.gestionArduino()


	def lireConfig(self):
		# Fonction permettant d'actualiser la config d'un module
		self.conf.openConfig()



	def gestionArduino(self):
		# Va donner la précédente valeur de l'arduino et offrir le choix à l'utilisateur de le changer
		self.lireConfig()
		print()
		print("--------------------------------------------------------")
		if (self.conf.arduino ):
			print("Arduino utilisée : OUI")
		else:
			print("Arduino utilisée : NON")
		print()
		liste = ["Revenir au menu principal","Ce module utilise l'arduino","Ce module n'utilose pas l'arduino"]
		a = Outils.menu("GESTION DE L'ARDUINO",liste, False)
		print("--------------------------------------------------------")
		if a == 0:
			self.menuPrincipal()
		elif a == 1:
			self.conf.setArduino(True)
			print()
			print()
			self.gestionArduino()
		elif a == 2:
			self.conf.setArduino(False)
			print()
			print()
			self.gestionArduino()


	def gestionNom(self):
		# Gestion du nom
		self.lireConfig()
		print()
		print("Nom actuel du module : "+self.conf.nom)
		nom = input("Donnez le nouveau nom (n'entrez rien si vous ne voulez pas changer) : ")
		if (nom != ""):
			self.conf.nom = nom
		print()
		self.menuPrincipal()


	def messageFinal(self):
		print()
		print("Félicitations, vous êtes prêt à développer le module "+self.conf.nom)
		print("Pour ce faire vous devez modifier le fichier "+self.localisation+"module.py") # ATTENTION, porobleme potentiel si la localisation finit pas par /
		print()
		sleep(4)

if __name__ == '__main__':
	a = InterfaceConfigModule("")
