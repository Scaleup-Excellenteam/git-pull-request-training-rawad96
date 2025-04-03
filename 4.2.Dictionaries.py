# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:57:29 2025

@author: USER
"""

# Week 4, dictionaries

#ex 1, decrypt
def decrypt(decryption_key,text):
    
    decryptionText = ""
    
    for i in text:
        if i.upper() in decryption_key:
            decryptionText += decryption_key[i.upper()].lower()
        else:
            decryptionText += i
    
    return decryptionText


def changeDict(decryption_key, text):
    newDecryptionKey = {}
    for i in decryption_key:
        newDecryptionKey[decryption_key[i]] = i
    return decrypt(newDecryptionKey, text)

if __name__ == '__main__':
    decryption_key = {
    'O': 'A', 'D': 'B', 'F': 'C', 'I': 'D', 'H': 'E',
    'G': 'F', 'L': 'G', 'C': 'H', 'K': 'I', 'Q': 'J',
    'B': 'K', 'J': 'L', 'Z': 'M', 'V': 'N', 'S': 'O',
    'R': 'P', 'M': 'Q', 'X': 'R', 'E': 'S', 'P': 'T',
    'A': 'U', 'Y': 'V', 'W': 'W', 'T': 'X', 'U': 'Y',
    'N': 'Z',
    }
    song = """
sc, kg pchxh'e svh pckvl k covl svps
pcop lhpe zh pcxsalc pch vklcp
k okv'p lsvvo is wcop k isv'p wovp ps
k'z lsvvo jkyh zu jkgh
eckvkvl jkbh o ikozsvi, xsjjkvl wkpc pch ikfh
epovikvl sv pch jhilh, k ecsw pch wkvi csw ps gju
wchv pch wsxji lhpe kv zu gofh
k eou, coyh o vkfh iou
coyh o vkfh iou
"""
    # print(decrypt(decryption_key,song))

    print(changeDict(decryption_key, song))
