class Employe:
    def __init__(self,num_permis,nom,prenom):
        self.num_permis=num_permis
        self.nom=nom
        self.prenom=prenom
        self.voitureService =  None
    def afficherInformation(self):
        print(f'Nom : {self.nom}',f'Prenom : {self.prenom}, Permis : {self.num_permis}')
        if self.voitureService is not None:
            print(f'Voiture Service :  {self.voitureService.marque} {self.voitureService.matricule}')
        else:
            print("Aucune voiture de service !")

    def affecterVoiture(self,voiture):
        if self.voitureService is not None:
            print("Une voiture de service est déja affectée a ce chauffeur !")
        elif voiture.chauffeur is not None:
            print("La voiture est déja affectée a un autre chauffeur !")
        else:
            self.voitureService = voiture
            voiture.chauffeur = self

    def retirerVoiture(self,voiture):
        if self.voitureService is None:
            print("Aucune voiture a retirer! ")
        elif self.voitureService != voiture:
            print("Cette voiture n'est pas affecter a ce chauffeur !")
        else:
            self.voitureService = None


class Voiture:
    def __init__(self,matricule,marque,annee,kilometrage):
        self.matricule=matricule
        self.marque=marque
        self.annee=annee
        self.kilometrage=kilometrage
        self.chauffeur=None
    def afficherInformation(self):
        print(f" matricule : {self.matricule}, marque : {self.marque}, anne : {self.annee}, "
              f"kilometrage : {self.kilometrage}")
        if self.chauffeur is not None:
            print(f"Chauffeur : {self.chauffeur.nom}, {self.chauffeur.prenom}")
