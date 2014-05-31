Ce script permet de transformer un fichier de scores (structuré d'une façon précise) en une page HTML, ainsi que de modifier le fichier de scores pour en ajouter de nouveaux. Il est spécialisé pour le jeu NaturalChimie.

Comment l'utiliser?

Exécutez le fichier script.py, une console s'ouvre.
Le script vous demande ce que vous voulez faire. Voici la liste des commandes possibles:
- help : afficher l'aide, qui contient l'ensemble des commandes existantes
- quit : quitter le script
- create : créer un nouveau fichier de scores (nom inderdit: quit.txt)
- load : charger un fichier de scores existant
- save : enregistrer les modifications apportées
- close : fermer le fichier courant
- insert : insérer un nouveau score
- insert-help : détailler l'utilisation de la commande insert
- genere : écrire le fichier HTML
Toutes ces commandes s'utilisent sans paramètre. Si l'une en a besoin, elle le demande au moment venu.
Aucune des commandes citées ne demande de confirmation pour s'exécuter. Si l'action ne peut pas se faire normalement, la raison sera copiée sur la console.

Les scores conservés sont les suivants:
- pour chaque lieu du jeu, le meilleur score
- les 10 meilleurs scores effectués, sur n'importe quel lieu, à l'exception de:
-- Mines du Volkor
-- Bibliothèque de Glace
-- Plateau des Thèses
-- Prieuré Korki

La possibilité de retirer un score (ou le remplacer) n'est pas implémentée car le top 10 amène beaucoup de complications pour le faire. Cette fonctionnalité sera peut-être un jour implémentée si j'en trouve le courage, car je n'en ai jamais eu besoin. Une autre fonctionnalité qui vera peut-être le jour est celle d'exécuter une liste d'actions écrites dans un fichier