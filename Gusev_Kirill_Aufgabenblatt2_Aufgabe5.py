"""
Created on Mon May 24 13:41:16 2021

@author: Gusev Kirill
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Donut:
    #Konstruktor
    def __init__(self,R=2,r=1):
        self.R = R
        self.r = r
        
    #Methoden    
    def x(self,theta,phi):
        return (self.R+self.r*np.cos(theta))*np.cos(phi)
    def y(self,theta,phi):
        return (self.R+self.r*np.cos(theta))*np.sin(phi)
    def z(self,theta):
        return self.r*np.sin(theta)
 
    def oberfl(self):
        return 4*np.pi**2*self.R*self.r
        
    def volumen(self):
        return 2*np.pi**2*self.R*self.r**2

    def __str__(self):
        return 'Donut mit Radien: ('+str(self.R)+','+str(self.r)+') und Oberfläche='+str(round(self.oberfl(),2)) + ', Volumen='+ str(round(self.volumen(),2))

    def __gt__(self,other):
        if self.volumen() > other.volumen():
            return True
        else:
            return False
        
    #Bonusaufgaben
    #1.Aufgabe
    def show(self):
        
        theta = np.linspace(0,2*np.pi,101)
        phi = np.linspace(0,2*np.pi,101)
        theta, phi = np.meshgrid(theta,phi)
        x = self.x(theta,phi)
        y = self.y(theta,phi)
        z = self.z(theta)
        #Figure
        figure = plt.figure(figsize=(5,5))
        ax = plt.axes(projection ='3d')
        ax.plot_surface(x,y,z, cmap = plt.cm.OrRd, alpha = 0.6, antialiased=True)
        ax.view_init(50,30)#Betrachtungshöhe und Winkel
        ax.set_xlabel('x Achse')
        ax.set_ylabel('y Achse')
        ax.set_zlabel('z Achse')
        ax.set_xlim(-2*self.R,2*self.R)#Scale image
        ax.set_ylim(-2*self.R,2*self.R)
        ax.set_zlim(-2*self.R,2*self.R)
        plt.show()
        
    #2.Aufgabe    
    def save(self,filename='donut.png'):
        theta = np.linspace(0,2*np.pi,101)
        phi = np.linspace(0,2*np.pi,101)
        theta, phi = np.meshgrid(theta,phi)
        x = self.x(theta,phi)
        y = self.y(theta,phi)
        z = self.z(theta)
        #Figure
        figure = plt.figure(figsize=(5,5))
        ax = plt.axes(projection ='3d')
        ax.plot_surface(x,y,z, cmap = plt.cm.OrRd, alpha = 0.6, antialiased=True)
        ax.view_init(50,30)#Betrachtungshöhe und Winkel
        ax.set_xlabel('x Achse')
        ax.set_ylabel('y Achse')
        ax.set_zlabel('z Achse')
        ax.set_xlim(-2*self.R,2*self.R)#Scale image
        ax.set_ylim(-2*self.R,2*self.R)
        ax.set_zlim(-2*self.R,2*self.R)
        plt.savefig(filename)
        
        
R = int(input('Geben Sie ein R: '))
r = int(input('Geben Sie ein r: '))
if R<=r:
    print('Warning: R muss grösser als r sein. Die Defaultwerte (R=2,r=1) den R,r sind zugewiesen.' )
    d = Donut()
else:
    d = Donut(R,r)

k = Donut(5,2)

print(d)
print(k)
print(k>d)
d.save()