class Cirque:
  # Crée des données a être utiliser pour les fonctions du classes. 
  def __init__(self, nom, clo, ele, mag):
    self._actes = []
    self._strNom = nom
    self._intClown = clo
    self._intElephant = ele
    self._intMagicien = mag


# Imprime des données relier à l'objet en question. 
  def __str__ (self):
    return f"\nDans {self._strNom}, il y a {self._intClown} clown, {self._intElephant} elephant et {self._intMagicien} magiciens. "

# Imprime le lenght du seule liste de l'objet. 
  def __len__ (self): 
    return len(self._actes)

# Elle fait fonctioner le for loop pour imprimer chaque composante du liste.
  def __getitem__(self, position):
    return self._actes[position]

  # Prend la liste et donne l'oppurtunité à l'utilisateur d'ajouter des actes. 
  def ajoute_acte(self):
    while True: 
      strActe = input("Écrit une acte que tu-veux ajouter ou tape q pour quitter: ")
      if strActe == "q":
        break
      else:
        self._actes.append(strActe)

  # Créer une propriété qui facilite le get pour le nom. 
  @property
  def nom(self):
    return self._strNom

  # Le deleter facilite le delete. 
  @nom.deleter
  def nom(self):
    del self._strNom

  # Créer une propriété qui facilite le get pour le clown
  @property
  def clown(self):
    return self._intClown

  # Le setter sert a valider l'input pour que l'utilisateur ne met pas un donné inadmissable. 
  @clown.setter
  def clown(self, clo):
    while type(clo) is not int: 
      try:
        clo =int(clo)
        if clo < 0:
          clo = input("\nIl ne peut pas avoir un nombre negative de clown. Combien de clown veux-tu? ")
      except: 
        clo = input("\nCette valeur de clown n'est pas acceptable. Combien de clown veux-tu? ")
    self._intClown = clo

  # Le deleter facilite le delete.
  @clown.deleter
  def clown(self):
    del self._intClown

  # Créer une propriété qui facilite le get pour l'éléphant
  @property
  def elephant(self):
    return self._intElephant

   # Le setter sert a valider l'input pour que l'utilisateur ne met pas un donné inadmissable. 
  @elephant.setter
  def elephant(self, ele):
    while type(ele) is not int: 
      try:
        ele =int(ele)
        if ele < 0:
          ele = input("\nIl ne peut pas avoir un nombre negative d'elephant. Combien d'éléphant veux-tu? ")
      except: 
        ele = input("\nCette valeur d'elephant n'est pas acceptable. Combien d'éléphant veux-tu? ")
    self._intElephant = ele

    
  # Le deleter facilite le delete.
  @elephant.deleter
  def elephant(self):
    del self._intElephant

  # Créer une propriété qui facilite le get pour le magicien
  @property
  def magicien(self):
    return self._intMagicien

   # Le setter sert a valider l'input pour que l'utilisateur ne met pas un donné inadmissable. 
  @magicien.setter
  def magicien(self, mag):
    while type(mag) is not int: 
      try:
        mag =int(mag)
        if mag < 0:
          mag = input("\nIl ne peut pas avoir un nombre negative de magicien. Combien de magicien veux-tu? ")
      except: 
        mag = input("\nCette valeur de magicien n'est pas acceptable. Combien de magicien veux-tu? ")
    self._intMagicien = mag
    
  # Le deleter facilite le delete.
  @magicien.deleter
  def magicien(self):
    del self._intMagicien