from random import randint as r

class question:
    def __init__(self):
        self.fichier = open("fichier_questions_2.txt", "r")
       
    def enoncer(self,n):
        ligne = self.fichier.readlines()
        var = ligne[n].split("?")
        q = var[0]
        return q + "?"



a = question()
print(a.enoncer(8))