# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:41:08 2021

@author: Danjour
"""

import random

class CreatePass:   
        
    def listAlphabet(self):
        Alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','!', '#', '$', '%', '&', '(', ')', 
                  '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        random.shuffle(Alphabet)
        return Alphabet
    
    
    def CreatePassword(self,Caracteres):
        Password = ""
        Letters=self.listAlphabet()
        for _ in range(Caracteres):
            Password=(Letters[random.randint(0,len(Letters))])+Password
        
        return (Password)


Create=CreatePass()

Caracteres=int(input("Number of characters in the password? "))

print(f'{Create.CreatePassword(Caracteres)}')

        
    
    
  
    
    

    