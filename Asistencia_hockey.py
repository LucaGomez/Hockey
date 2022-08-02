# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 00:34:19 2022

@author: Luca
"""
import pandas as pd
import os

os.chdir (r"C:\Users\Luca\Desktop\Hockey\Código para lista\Listas")

#%%

print('¿Qué fecha es hoy? (DDMMAAAA)')
fecha=input('')

Jug=[str('Juli'),str('Santi'),str('Manu'), str('Mica Sani')]
List=[]
for i in range(len(Jug)):
    print('¿Vino '+Jug[i]+'?')
    P=input('')
    if P==str('s'):
        List.append(1)
    else: 
        List.append(0)

data = {'Jugadores': Jug,
        'Asistencia': List}

df = pd.DataFrame(data, columns = ['Jugadores', 'Asistencia'])

df.to_csv(str(fecha)+'.csv')

#%%

data=pd.read_csv(str(fecha)+'.csv',skiprows=1,names=['Jugadores','Asistencia'])