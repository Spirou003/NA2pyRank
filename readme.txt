Ce script permet de transformer un fichier de scores (structur� d'une fa�on pr�cise) en une page HTML, ainsi que de modifier le fichier de scores pour en ajouter de nouveaux. Il est sp�cialis� pour le jeu NaturalChimie.

Comment l'utiliser?

Ex�cutez le fichier script.py, une console s'ouvre.
Le script vous demande ce que vous voulez faire. Voici la liste des commandes possibles:
- help : afficher l'aide, qui contient l'ensemble des commandes existantes
- quit : quitter le script
- create [filename] : cr�er un nouveau fichier de scores (nom inderdit: quit.txt). Un param�tre optionnel [filename] donne le nom du fichier (sans le .txt)
- load : charger un fichier de scores existant. Un param�tre optionnel [filename] donne le nom du fichier (sans le .txt)
- save : enregistrer les modifications apport�es
- close : fermer le fichier courant
- insert [lieu score �cole] : ins�rer un nouveau score. Trois param�tres optionnels [lieu score �cole] permettent d'ins�rer directement un nouveau score. Remarque: il faut donner les trois param�tres en m�me temps, sinon cela ne fonctionne pas
- insert-help : d�tailler l'utilisation de la commande insert
- genere : �crire le fichier HTML
Toutes ces commandes peuvent s'utiliser sans param�tre. Si l'une en a besoin, elle le demande au moment venu ou le prend en param�tre optionnel.
Aucune des commandes cit�es ne demande de confirmation pour s'ex�cuter. Si l'action ne peut pas se faire normalement, la raison sera copi�e sur la console.

Les scores conserv�s sont les suivants:
- pour chaque lieu du jeu, le meilleur score
- les 10 meilleurs scores effectu�s, sur n'importe quel lieu, � l'exception de:
-- Mines du Volkor
-- Biblioth�que de Glace
-- Plateau des Th�ses
-- Prieur� Korki

La possibilit� de retirer un score (ou le remplacer) n'est pas impl�ment�e car le top 10 am�ne beaucoup de complications pour le faire. Cette fonctionnalit� sera peut-�tre un jour impl�ment�e si j'en trouve le courage, car je n'en ai jamais eu besoin. Une autre fonctionnalit� qui vera peut-�tre le jour est celle d'ex�cuter une liste d'actions �crites dans un fichier