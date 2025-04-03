# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:57:39 2025

@author: USER
"""
# Week 4, loops

#ex 1, Acrostic
def Acrostic(song):
    linesArray = song.split('\n')
    returnedAcrostic = ""
    for i in range(len(linesArray)):
        returnedAcrostic += linesArray[i].lstrip()[0]
    
    return returnedAcrostic

#ex 2, stepsCouting
def stepsCouting(listOfSteps):
    x = 0;
    y = 0;
    for i in listOfSteps:
        x += i[0];
        y += i[1]
    
    return (x, y)

#ex 3, rabbitsCollector
def rabbitsCollector(rabbits):
    totalRabbits = 0
    returnedList = []
    for i in rabbits:
        totalRabbits += i
        returnedList.append(totalRabbits)
    return returnedList


if __name__ == '__main__':
   print(Acrostic("""Elizabeth it is in vain you say
Love not — thou sayest it in so sweet a way:
In vain those words from thee or L.E.L.
Zantippe's talents had enforced so well:
Ah! if that language from thy heart arise,
Breath it less gently forth — and veil thine eyes.
Endymion, recollect, when Luna tried
To cure his love — was cured of all beside —
His follie — pride — and passion — for he died."""))
print(stepsCouting([(1, 5), (6, -2), (4, 3)]))
print(rabbitsCollector([1, 2, 3, 4]))
