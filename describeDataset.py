# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 00:51:36 2022

@author: garci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Estadistica:
    
    def __init__(self, df):
        self.df = df
        self.min = self.min()
        self.max = self.max()
        self.mean = self.mean()
        self.var = self.var()
        self.std = self.std()
        self.numberOfInstanceOfAtrr = self.numberOfInstanceOfAtrr() 
        self.numberOfEmptyInstanceOfAtrr = self.numberOfEmptyInstanceOfAtrr()
        self.observations = self.observations()
        
    def min(self):
        minimos = {}
        for i in self.df:
            minimos[i] = self.df[i].min()
        return minimos
    
    def max(self):
        maximos = {}
        for i in self.df:
            maximos[i] = self.df[i].max()
        return maximos 
    
    def mean(self):
        promedios = {}
        for i in self.df:
            if(type(self.df[i].min()) != str):
                promedios[i] = self.df[i].mean()
        return promedios
    
    def std(self):
        desviacion = {}
        for i in self.df:
            if(type(self.df[i].min()) != str):
                desviacion[i] = self.df[i].std()
        return desviacion
    
    def var(self):
        v = {}
        for i in self.df:
            if(type(self.df[i].min()) != str):
                v[i] = self.df[i].var()
        return v
    
    def desc(self):
        return self.df.describe()
    
    def numberOfInstanceOfAtrr(self):
        numInstancias = {}
        for i in self.df:
            numInstancias[i] = self.df[i].count()
        return numInstancias
    
    def observations(self):
        numInstancias = {}
        for i in self.df:
            numInstancias[i] = len(self.df[i].unique().tolist())
        return numInstancias
    
    def numberOfEmptyInstanceOfAtrr(self):
        numInstancias = {}
        for i in self.df:
            numInstancias[i] = self.df[i].isnull().sum()
        return numInstancias
    
    def numeroAtributos(self):
        numAtributos = 0
        for i in self.df:
            numAtributos += 1
        return numAtributos
    
    def plotAll(self):
        self.df['Tool wear [min]'] = self.df['Tool wear [min]'].astype('float64')
        self.df['Rotational speed [rpm]'] = self.df['Rotational speed [rpm]'].astype('float64')
        self.df['Target'] = self.df['Target'].astype('float64')
        
        # Primerla letra del id
        self.df['Product ID'] = self.df['Product ID'].apply(lambda x: x[1:])
        self.df['Product ID'] = pd.to_numeric(self.df['Product ID'])
        sns.histplot(data=self.df, x='Product ID', hue='Type')
        plt.show()
        
        
        # Porcentaje
        value = self.df['Type'].value_counts()
        porcentaje = 100*value/self.df.Type.shape[0]
        labels = porcentaje.index.array
        x = porcentaje.array
        plt.pie(x, labels = labels, colors=sns.color_palette('tab10')[0:3], autopct='%.0f%%')
        plt.title('Porcentaje de caldiad del producto')
        plt.show()
        
        # Tipo de Distribucion
        
        encabezado = [col for col in self.df.columns
                    if self.df[col].dtype=='float64' or col =='Type']
        
        
        nEncabezado = [titulo for titulo in encabezado if  self.df[titulo].dtype=='float64']
       
        
        fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(30,12))
        fig.suptitle('Correlacion de los atributos numericos con las fallas')
        custom_palette = {'L', 'M', 'H'}
        for j, feature in enumerate(nEncabezado):
            sns.kdeplot(ax=axs[j//3, j-3*(j//3)], data=self.df, x=feature,
                      hue='Type', fill=True)
        plt.show()
        
        fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(30,12))
        fig.suptitle('Correlacion de los atributos numericos con la etiqueta de fallo(1) o no fallo(0)')
        enumerate_features = enumerate(nEncabezado)
        for j, feature in enumerate_features:
            sns.kdeplot(ax=axs[j//3, j-3*(j//3)], data=self.df, x=feature,
                        hue='Target', fill=True)
        plt.show()
        return 
    
    def __str__(self): 
        self.plotAll()
        
        returnTypes = ""
        for i in self.min:
            returnTypes += (i +":"+ str(type(self.min[i])) + "\n")
        returnObservations = ""
        for i in self.observations:
            returnObservations += (i +":"+ str(self.observations[i]) + "\n")
        returnInstanceOf = ""
        for i in self.numberOfInstanceOfAtrr:
            returnInstanceOf += (i +":"+ str(self.numberOfInstanceOfAtrr[i]) + "\n")
        returnEmpyInstance = ""
        for i in self.numberOfEmptyInstanceOfAtrr:
            returnEmpyInstance += (i +":"+ str(self.numberOfEmptyInstanceOfAtrr[i]) + "\n")
        returnMin = ""
        for i in self.min:
            returnMin += (i +":"+ str(self.min[i]) + "\n" if (type(self.min[i]) != str) else "")
        returnMax = ""
        for i in self.max:
            returnMax += (i +":"+ str(self.max[i]) + "\n" if (type(self.max[i]) != str) else "")
        returnMean = ""
        for i in self.mean:
            returnMean += (i +":"+ str(self.mean[i]) + "\n" if (type(self.mean[i]) != str) else "")
        returnVar = ""
        for i in self.var:
            returnVar += (i +":"+ str(self.var[i]) + "\n" if (type(self.var[i]) != str) else "")
        returnStd = ""
        for i in self.std:
            returnStd += (i +":"+ str(self.std[i]) + "\n" if (type(self.std[i]) != str) else "")
        return ("El número de atributos es: " + str(self.numeroAtributos()) + "\n\n" + 
                "Los tipos son (Atributo: valor): \n" + returnTypes + "\n\n" + 
                "El numero de instancias por atributo es (Atributo: valor): \n" + returnInstanceOf + "\n\n" + 
                "El numero de observaciones por atributo es (Atributo: valor): \n" + returnObservations + "\n\n" + 
                "El numero de datos faltantes por atributo es (Atributo: valor): \n" + returnEmpyInstance + "\n\n" + 
                "Los valores mínimos son (Atributo: valor): \n" + returnMin + "\n\n" + 
                "Los valores máximos son (Atributo: valor): \n" + returnMax + "\n\n" +
                "Los valores desviación estandar son (Atributo: valor): \n" + returnStd + "\n\n" +
                "Los valores de variación son (Atributo: valor): \n" + returnVar + "\n\n" +
                "Los valores promedio son (Atributo: valor): \n" + returnMean + "\n\n")
        




url = 'https://drive.google.com/file/d/1_dElPy5hHvvgqvQ9qYgx3JfaGJmXP8cz/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

dfCaracteristicas = Estadistica(pd.read_csv(path))
a = dfCaracteristicas.desc()
print(dfCaracteristicas)


