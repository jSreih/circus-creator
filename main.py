import cirque as C
dict = {}
print("La création des cirques :)")
# Create options for the user
while True:
  choix = input('''\nChoisi entre les 5 options si-dessous.
1. Ajouter une cirque.
2. Modifier les propriété du cirque.
3. Enlever une cirque.
4. Afficher les valeurs d'un de tes cirques
5. Tapez q pour terminer 
''')

  if choix == "1": 
    # Demande à l'utilisateur de fournir de l'information pour son cirque. 
    nom = input("\nQuelle est le nom de ton cirque? ")
    clo = input("Combien de clown veux-tu? ")
    ele = input("Combien d'éléphant veux-tu? ")
    mag = input("Combien de magicien veux-tu? ")
    
    # Utiliser la fonction setter pour valider chaque input. 
    dict[nom] = C.Cirque(nom, clo, ele, mag)
    dict[nom].clown = clo
    dict[nom].elephant = ele
    dict[nom].magicien = mag
    dict[nom].ajoute_acte()

    # En appellant au fonction __str__, __len et __get__, le système imprime les propriétés, la longeur du liste et chaque acte dans la liste.
    print(dict[nom])
    print(f"Il y aura {len(dict[nom])} actes durant le cirque qui consiste de: ")
    for acte in dict[nom]:
      print(acte)


      
  # Imprime chaque cirque créer, et demande lui à prendre le cirque qu'il veut changer. Le système imprime les données relier au cirque, ensuite, il imprime des options. 
  elif choix == "2":
    if len(dict) > 0:
      print("\nVoici chacun de tes cirques: ")
      for key in (dict):
        print(key)
      key = input("Écrit le nom du cirque que tu veux modfier: ")
      if key in dict.keys():
        print(dict[key])
        change = input('''\nQuelle propriété veux-tu changer
1. Nom
2. Nombre de clown
3. Nombre d'éléphant
4. Nombre de magicen
''')
        
        # 1. Change le nom du cirque. En changeant le nom, le programme doit changer le clé du cirque. Appelle la fonction delete pour effacer le nom et encore delete pour enlever l'ancienne clé. 
        if change == '1':
          del dict[key].nom
          nom = input("\nQuelle est le nom nouvel de ton cirque? ")
          dict[nom] = dict[key]
          dict[nom] = C.Cirque(nom, clo, ele, mag)
          print(f"Il faut réadresser les actes à cause du changement. ")
          dict[nom].ajoute_acte()
          print(f"\nVoici ta cirque modifier: {dict[nom]}")
          for acte in dict[nom]:
            print(acte)
          del dict[key]
          
        # 2. Change le nombre de clown. Appelle la fonction delete pour effacer l'ancienne nombre, et la fonction setter pour valider le nombre. 
        elif change == "2":
          del dict[key].clown
          clo = input("\nCombien de clown veux-tu? ")
          dict[key] = C.Cirque(nom, clo, ele, mag)
          dict[key].clown = clo
          print(f"Il faut réadresser les actes à cause du changement. ")
          dict[nom].ajoute_acte()
          print(f"\nVoici ta cirque modifier: {dict[key]}")
          for acte in dict[nom]:
            print(acte)
            
       # 3. Change le nombre d'éléphant. Appelle la fonction delete pour effacer l'ancienne nombre, et la fonction setter pour valider le nombre. 
        elif change == "3":
          del dict[key].elephant
          ele = input("\nCombien de éléphant veux-tu? ")
          dict[key] = C.Cirque(nom, clo, ele, mag)
          dict[key].elephant = ele
          print(f"Il faut réadresser les actes à cause du changement. ")
          dict[nom].ajoute_acte()
          print(f"\nVoici ta cirque modifier: {dict[key]}")
          for acte in dict[nom]:
            print(acte)
            
        # 4. Change le nombre de magicien. Appelle la fonction delete pour effacer l'ancienne nombre, et la fonction setter pour valider le nombre. 
        elif change == "4":
          del dict[key].magicien
          mag = input("\nCombien de magicien veux-tu? ")
          dict[key] = C.Cirque(nom, clo, ele, mag)
          dict[key].magicien = mag
          print(f"Il faut réadresser les actes à cause du changement. ")
          dict[nom].ajoute_acte()
          print(f"\nVoici ta cirque modifier: {dict[key]}")
          for acte in dict[nom]:
            print(acte)
            
        # L'option est invalide pour changer les propriétés. 
        else:
          print("Cette option n'est pas valide. ")

      # Si le nom du cirque donnée n'existe pas, imprime que le cirque n'existe pas. 
      else:
        print(f"Il n'y a pas de cirque sous le nom {key}.")
        
    # S'il n'y a pas d'objet, le système ne va pas actionner la fonction.
    else: 
      print("\nIl n'y a pas d'objet à modifier. ")


      
  # Si le choix est 3, imprime les cirques qui existe. 
  elif choix == "3":
    if len(dict) > 0:
      print("\nVoici chacun de tes cirques: ")
      for key in (dict):
        print(key)
      delete = input("\nÉcrit le nom du cirque que veux-tu enlever:  ")

    # En utilisant l'input d'avant, le système enlève le cirque que l'utlisateur ne veut pas garder. Ensuite, il imprime encore la liste pour démontrer que la fonction s'execute.
      if delete in dict.keys():
        del dict[delete]
        print("Voici les cirques qui reste: ")
        for key in (dict):
          print(key)

    # Imprime si l'utilisateur donne une cirque qui n'existe pas. 
      else:
        print(f"Il n'y a pas de cirque sous le nom {delete}.")
    # S'il n'y a pas de cirque qui existe au moment. 
        
    else: 
      print("\nIl n'y a pas d'objet à modifier. ")


      
  # Imprime encore les cirques déjà crée et invite l'utilisateur à choisir lequel il veut revoir. 
  elif choix == "4":
    if len(dict) > 0:
      print("\nVoici chacun de tes cirques: ")
      for key in (dict):
        print(key)
      prop = input("\nÉcrit le nom du cirque que tu aimerais regarder: ")

      # En appellant au fonction __str__, __len et __get__, le système imprime les propriétés, la longeur du liste et chaque acte dans la liste. 
      if prop in dict.keys():
        print(dict[prop])
        print(f"Il y aura {len(dict[prop])} actes durant le cirque qui consiste de: ")
        for acte in dict[prop]:
          print(acte)

      else: 
        print(f"Il n'y a pas de cirque sous le nom {prop}.")
    # Displays text if the user hasnt created a circue yet      
    else:
      print("\nIl n'y a pas de cirque à modifier. ")


      
  # If the option is q, exit the loop
  elif choix == "q":
    break

  # Si le choix n'est pas valide, imprime ceci. 
  else: 
    print("Ce choix n'est pas valide.")

print("\n\nMerci beaucoup :D")