from outils import *
class ConfigModule:
	def __init__(self,endroit):
		self.endroit = endroit + "configModule.f"
		self.openConfig()

	def initialisation(self):
		# Initialise les variables
		self.nom = ""
		self.arduino = ""


	def setNom(self,nom):
		# Fonction permettant de modifier le nom du module dans le fichier de config
		self.nom= nom
		self.save()

	def setArduino(self,arduino):
		self.arduino = arduino
		self.save()


	def save (self):
		# Sauvegarde du fichier
		chaine = Outils.constitueBalise("Nom",str(self.nom)) + "\n" + Outils.constitueBalise("Arduino",str(self.arduino))
		Outils.ecrireFichier(self.endroit,chaine)

	def openConfig(self):
		# Permet d'ouvrir la configuration si elle existe
		self.initialisation()
		if (Outils.testPresence(self.endroit)):
			chaine = Outils.lireFichier(self.endroit)
			self.arduino = Outils.recupereBaliseAuto(chaine, "Arduino", 1, "Arduino") == "True"
			self.nom =Outils.recupereBaliseAuto(chaine,"Nom",1)
			

