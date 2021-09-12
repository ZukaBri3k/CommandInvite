<h1>Python commande interpreteur</h1>

<p>Ce projet a pour but de coder un interpreteur de commande en python. Pour ce projet plusieurs librairie Python on été utilisées :</p>
<li>Tkinter : pour la partie graphique</li>
<li>os : pour la manipulation de fichiers</li>
<li>re : pour la manipulation de string</li>
<li>shutil : pour la manipulation de dossier</li>
<li>datetime : pour récupérer l'heure et la date</li>

<h1>Utilisation</h1>
<p>Executer le fichier main.py</p>

<h1>Liste des commandes :</h1>
<li>add fileExtension name -- créer un fichier dans le répertoire courant</li>
<li>rem fileName -- supprime un fichier dans le répertoire courant</li>
<li>cd folderName -- change le répertoire courant</li>
<li>cdlist -- liste tous les élements du répertoire courant</li>
<li>ren oldName;newName -- renome un fichier du répertoire courant</li>
<li>addfold foldName -- créer un dossier dans le répertoire courant</li>
<li>remfold foldName -- supprime un dossier du répertoire courant</li>
<li>now -- affiche la date et l'heure actuelle</li>

<h1>Ajouter une commande :</h1>
<p>Dans le fichier invite.py ajouter à la suite du if ligne 30 :</p>
<p>elif cmd[0] == 'nomDeVotreCommande':</p>
<p>commands.nomDeVotreCommande(cmd)</p>
<p>Dans le fichier commands.py ajouter une fonction du nom de votre commande:</p>
<p>def nomDeVotreCommande(cmd):</p>
<p>Votre code<p>
