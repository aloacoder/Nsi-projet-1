# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:14:18 2022

@author: tapar
"""

class question:
    def __init__(self, prop = "", bonne_rep = ""):
        self.fichier = open("fichier_questions_2.txt", "r")
        self.prop = prop
        self.bonne_rep = prop
        
    def enoncer(self,n):
        ligne = self.fichier.readlines()
        var = ligne[n].split("?")
        q = var[0]
        self.prop = self.methode_reponse(var[1])
        return q + "?"
    
    def methode_reponse(self,liste_reponse):
        var = liste_reponse.split("[")
        self.bonne_rep = self.methode_bonne_rep(var[1])
        proposition = var[0]
        return proposition
    
    def methode_bonne_rep(self,liste_bonne_rep):
        liste_divise = liste_bonne_rep.split("]")
        lettre_bonne_reponse = liste_divise[0].split(";")
        return lettre_bonne_reponse[0]
    
    
a = question()
print(a.enoncer(1))
print(a.prop)
print(a.bonne_rep)
