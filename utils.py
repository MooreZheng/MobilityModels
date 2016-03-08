# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:35:44 2015
data structures for mobility models
@author: zimu
"""
import random

class Point:
    def __init__(self, X=0, Y=0, Z=0, LOC=0):
        self.x = X 
        self.y = Y
        self.z = Z
        self.loc = LOC

class Citizen:
    def __init__(self, WLAYER, WBUILD, HOMELOC):
        self.workLayer = WLAYER #0 is for traffic, not for working space, start from 1
        self.workBuilding = WBUILD #0 is for road, start from -1 
        self.homeloc = HOMELOC #home loc in map

class Building:
    def __init__(self, LOC, N_WL):
        self.loc = LOC
        self.nWL = N_WL
        
class Map:
    def __init__(self, SIZE=100, N_MN=100, N_WL=10, N_BB=1):
    #N_MN: the num of mobile nodes (citizen)
    #N_WL: the num of working layers per building
    #N_BB: the num of business buildings
        self.size = SIZE
        self.points = []
        for i in range(SIZE):
            for j in range(SIZE):
                self.points.append(Point(i,j,0,0))
        
        self.buildings = []
        for i in range(N_BB):
            i_poi = random.randint(0,SIZE*SIZE-1)
            while self.points[i_poi].loc != 0:
                i_poi = random.randint(0,SIZE*SIZE-1)
            build = Building(i_poi, N_WL)
            self.buildings.append(build)
            self.points[i_poi].loc = -i-1 
            #negative indexes are for buildings, starting from -1
            
        print self.buildings[0]    
        self.citizens = []
        for i in range(N_MN):
            wbuild = random.randint(-N_BB, -1)
            wlayer = random.randint(1, (self.buildings[-wbuild-1]).nWL) #layer 0 is for traffic, not for working space
            homeloc = random.randint(0, SIZE*SIZE-1)
            while self.points[homeloc].loc != 0:
                homeloc = random.randint(0,SIZE*SIZE-1)
            self.points[homeloc].loc = i+1 #postive indexes are for home, starting from -1
            ctzen = Citizen(wlayer, wbuild, homeloc)
            self.citizens.append(ctzen)
            #print "set {}".format(i)
        
    def printMap(self):
        for i in range(self.size):
            for j in range(self.size):
                print self.points[i*self.size+j].loc, " ",
            print ""
            
    def printBuilding(self):
        for i in range(len(self.buildings)):
            print "For building", -i-1
            print "It has {} layers".format(self.buildings[i].nWL)
    
    def printCitizens(self):
        for i in range(len(self.citizens)):
            print "For citizen", i+1
            print "He/She lives in Home Location {}.".format(self.citizens[i].homeloc)
            print "He/She works in Building {}, Layer {}.".format(self.citizens[i].workBuilding, self.citizens[i].workLayer)

        
if __name__ == "__main__":
    m=Map(10,10,10,1)
    m.printMap()
    m.printBuilding()
    m.printCitizens()