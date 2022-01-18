# coding: utf-8
import pandas as pd
from fonction import *
import csv
import glob

#Récupère la liste des fichiers spécifiés par le chemin au format liste
csv_files = glob.glob('C:/Users/anthony/Documents/RESANO/AILLAS/C2R/Fichier ex C2R/Miramont/*.csv')

#Préparez une liste pour ajouter le contenu du fichier csv
#Liste pour spécifier les colonnes que je veux lire
data_list = []                                       
colonnes = [1,4,5,6,8,9,11,12,19,20,22,25,28,29,30]  

#Scanne la liste des fichiers à lire
for file in csv_files:
     data_list.append(pd.read_csv(file, delimiter=";", encoding = "ISO-8859-1", usecols=colonnes, na_filter=False))
     

#Combine toutes les listes dans le sens alphabétique
df = pd.concat(data_list, axis=0)
total=df.sort_values(by=['NomLiv','VilleLiv'])
total.to_csv("C:/Users/anthony/Desktop/miramont/miramont-total.csv", index=False, sep=";")


Client = '' 
CodePost = 0
Metrage = 0.0
Poids = 0.0
Refclt = ''
cpt = 0
file_name = "C:/Users/anthony/Desktop/miramont/miramont.csv"
file = open(file_name , "w", newline="")
writer = csv.writer(file, delimiter = ';') 
    
for index, lines in total.iterrows():                                               #Je parcours la dataframe 


     if Client == lines['NomLiv'] and CodePost == lines['CPLiv'] or cpt == 0:       #Je veux additionner les valeurs pour le même transport 

               
               lpoids = lines['PoidsSSCC']
               z = poids(lpoids)                                                    #Fonction qui retourne le poids en décimal
               Poids = Poids + z
               Poids = round(Poids, 2)
               
               lmet= lines['MPL']
               u = metrage(lmet)
               Metrage = Metrage + u
               Metrage = round(Metrage, 2)
               
               if str(lines['NumCde']) not in str(Refclt):                           #Je veux juste additioner les valeurs manquantes
                 Refclt = str(lines['NumCde']) +'_'+ str(Refclt)
               
               cpt = cpt + 1
               
     else:
          
               writer.writerow(['1,1','1','33','C2RMIRAM',DateChg,'','','','','','F',DateLiv,Client,AdrLiv1,AdrLiv2,CodePost,Villedest,'F','',Refclt,'','',Poids,'','','',Metrage])
               
               lpoids = lines['PoidsSSCC']
               Poids = poids(lpoids)

               lmet = lines['MPL']
               Metrage = metrage(lmet)
               
               Refclt = str(lines['NumCde'])

     #J'actualise mes variables à chaque itération
     Client = lines['NomLiv']                            
     CodePost = lines['CPLiv']          
     DateChg = lines['DateExp']
     DateLiv = lines['DateLiv']
     AdrLiv1 = lines['AdresseLiv1'] 
     AdrLiv2 = lines['AdresseLiv2']
     Villedest = lines['VilleLiv']  
    
writer.writerow(['1,1','1','33','C2RMIRAM',DateChg,'','','','','','F',DateLiv,Client,AdrLiv1,AdrLiv2,CodePost,Villedest,'F','',Refclt,'','',Poids,'','','',Metrage])

#Fermeture du fichier
file.close()     
