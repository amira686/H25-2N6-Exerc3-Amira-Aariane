import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")
print(f"Le repertoire courant est {os.getcwd()}")




# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")
user_profile = os.environ.get('USERPROFILE')
print(f"La variable est {user_profile}")



# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
print(f"Q3{'_'*60}")
chemin = os.path.join(os.environ.get('USERPROFILE'), 'Documents')
os.chdir(chemin)
print(f"Voici le repertoire courant : {chemin}")




# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")
liste = os.listdir(chemin)
print("Voici la liste des fichiers et répertoire dans document:"  )
for item in liste:
    print(item)






# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")

os.mkdir('OS.ExercQ5')
print("Voici la liste des fichiers et répertoire dans document:"  )
for item in liste:
    print(item)







# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")

os.makedirs('OS-ExercQ6/Subdir1')
print("Voici la liste des fichiers et répertoire dans document:"  )
for item in liste:
    print(item)




#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q6{'_'*60}")
os.rename('OS-ExercQ6/Subdir1', 'Sous_repertoire')



# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
os.rmdir('OS-ExercQ6')
print("Voici la liste des fichiers et répertoire dans document:"  )
for item in liste:
    print(item)





