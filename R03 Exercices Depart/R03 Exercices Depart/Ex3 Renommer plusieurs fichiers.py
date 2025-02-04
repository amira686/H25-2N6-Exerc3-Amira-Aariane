# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier


import os
print()
print(__file__)
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
print(os.getcwd())
print()

chemin = os.path.join(os.environ.get('USERPROFILE'), 'Documents', 'GitHub', 'H25-2N6-Exerc3-Amira-Aariane', 'R03 Exercices Depart', 'R03 Exercices Depart', 'Ex3 Videos')
os.chdir(chemin)
liste = os.listdir(chemin)
for item in list:
    print('item')


