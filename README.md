# FReveilModuleCreator
Un logiciel d'aide à la création de module du FReveil 

## Introduction
Ce logiciel permet à chaque développeur de créer son propre module du FReveil (<https://github.com/bousmahafaycal/FReveil>). Ainsi, tout 
le monde peut étendre les fonctionnalités du FReveil.


## Tester le FReveilModuleCreator
Pour créer son propre module, il faut lancer la commande suivante après avoir cloné ce dépot : 


`
python3 module_creator.py
`

Ensuite, on doit suivre les instructions s'affichant à l'écran. Lorsque ceux-ci sont terminées, un dossier avec des fichiers à l'interieur 
aura été créé. Ce dossier sera nommé comme le nom du module que vous souhaitez créer (demandé par le script module_creator). 

Pour que votre module amène un plus au FReveil, il faut qu'il fasse quelque chose. Pour cela, une fois que vous aurez écrit vos fonctions,
l'appel de fonction devra être fait dans la fonction start qui est dans le fichier module.py du dossier créé. C'est la fonction qui sera 
appelée par le FReveil lorsque votre module sera sollicité.


## Attention
- Ne pas modifier le fichier outils.py !
