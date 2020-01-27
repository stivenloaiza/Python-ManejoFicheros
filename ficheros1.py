# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:49:44 2019

@author: Fire & Soft
"""

from io import open

class ManejoFicheros:
    texto=""
    lineas=[]
    
    def __init__(self):
        self.texto="Linea 1\n Linea 2"
    
    def abrirArchivoNuevo(self):
        self.fichero = open('fichero.txt','w')
        
    def abrirArchivoLectura(self):
        self.fichero = open('fichero.txt','r')
        
    def analizarDato(self):
        self.fichero = open('fichero.txt','r')
        self.lineas= self.fichero.readlines()
        if self.lineas[0] == "0":
            print("apagar toma "+ self.lineas[0])
        else:
            print("prender "+ self.lineas[0])
            
    def abrirArchivoLecturaLineas(self):
        self.fichero = open('fichero.txt','r')
        self.lineas = self.fichero.readlines()
        
    def abrirArchivoEdicionAlFinal(self):
        self.fichero = open('fichero.txt','a')
        
    def abrirArchivoEdicionInicio(self):
        self.fichero= open('fichero.txt','r+')
        
    def enviarTexto(self, textoUsuario):
        self.fichero.write(textoUsuario)
        self.fichero.close()
    
    def enviarTextoAlFinal(self, textoUsuario):
        self.fichero.write("\n"+textoUsuario)
        self.fichero.close()
        
    def enviarTextoInicio(self, textoUsuario):
        self.fichero.write(textoUsuario)
        self.fichero.close()
        
    def enviarTextoLineaMod(self, textoUsuario):
        self.lineas= self.fichero.readlines()
        self.lineas[2] = textoUsuario
        self.fichero.seek(0)
        self.fichero.writelines(self.lineas)
        self.fichero.close
        
    def llenarArchivo(self):
        self.fichero.write(self.texto)
        self.fichero.close()
        
    def borrarFichero(self):
        #no funciono
        del(self.fichero)
        
    def imprimirArchivoLeido(self):
        print(self.fichero.read())
        self.fichero.close()
    
    def imprimirArchivoLeidoLineas(self):
        print(self.lineas)
        self.fichero.close()
    
    def imprimirArchivoLeidoLineas2(self, numeroLinea):
        print(self.lineas[numeroLinea])
        self.fichero.close()
        
    def imprimirDesdePuntero(self, puntero):
        self.fichero.seek(puntero)
        print(self.fichero.read())
        
    def imprimirLosXPrimeros(self, punteroInicio):

        print(self.fichero.read(punteroInicio))
        
    
m = ManejoFicheros()
#print(m.texto)
#m.abrirArchivoEdicionAlFinal()
#m.abrirArchivoLecturaLineas()
#m.abrirArchivoLectura()
#m.abrirArchivoEdicionInicio()
#m.enviarTexto(input("Ingrese el contenido"))
#m.llenarArchivo()
#m.borrarFichero
#m.imprimirArchivoLeidoLineas()
#m.imprimirArchivoLeidoLineas2(0)
#m.imprimirDesdePuntero(int(input("Desde donde:\n")))
#m.imprimirLosXPrimeros(int(input("hasta:\n")))
#m.enviarTextoLineaMod(input("Ingrese el contenido\n"))
#m.enviarTextoInicio(input("Ingrese el contenido\n"))
m.analizarDato()

