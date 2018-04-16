import random


class Block:
    def __init__(self):
        self.voters = 10000
        #self.xlr = random.randint(-10.0,10.0)
        #self.yal = random.randint(-10.0,10.0)

        xbias = random.uniform(-5.0,5.0)
        ybias = random.uniform(-5.0,5.0)

        self.location = random.uniform(-5.0,5.0)
        self.econstats = random.uniform(-5.0,5.0)
        self.diversity = random.uniform(-5.0,5.0)
        self.religious = random.uniform(-5.0,5.0)

        self.percentageVoters = random.uniform(0.200, 1.000)

        self.xecon = self.location + self.econstats + xbias
        self.yauth = self.diversity + self.religious + ybias

    def loadStats(self, location, econstats, diversity, religious, xecon, yauth):
        self.location = location
        self.econstats = econstats
        self.diversity = diversity
        self.religious = religious
        self.xecon = xecon
        self.yauth = yauth

    def printStats(self):
        print("location:",self.location)
        print("economic status:",self.econstats)
        print("diversity:",self.diversity)
        print("religious importance:",self.religious)
        print("x value:",self.xecon)
        print("y value:",self.yauth)

    def spreadStats(self):
        if random.randint(0,1) == 0:
            dir = -10
        else:
            dir = 10
            #print(10)
        self.changeYStats(dir, 1)
        if random.randint(0,1) == 0:
            dir = -10
        else:
            dir = 10
            #print(10)
        self.changeXStats(dir, 1)

    def polarize(self):
        if self.xecon > -9.0 and self.xecon < 0:
            self.xecon -= 1
        elif self.xecon <9.0 and self.xecon > 0:
            self.xecon += 1

        if self.yauth > -9.0 and self.yauth < 0:
            self.yauth -= 1
        elif self.yauth < 9.0 and self.yauth > 0:
            self.yauth += 1


    def changeLocationStats(self, changeCoordinates, importance):

        loc = self.location

        if self.location < changeCoordinates:
            self.location += importance
            if self.location > changeCoordinates:
                self.location = changeCoordinates
        elif self.location > changeCoordinates:
            self.location -= importance
            if self.location < changeCoordinates:
                self.location = changeCoordinates

        change = self.location - loc
        self.xecon += change

    def changeEconStats(self, changeCoordinates, importance):  #coordinates need to be between -5 and 5

        econ = self.econstats

        if self.econstats < changeCoordinates:
            self.econstats += importance
            if self.econstats > changeCoordinates:
                self.econstats = changeCoordinates
        elif self.econstats > changeCoordinates:
            self.econstats -= importance
            if self.econstats < changeCoordinates:
                self.econstats = changeCoordinates

        change = self.econstats - econ
        self.xecon += change

    def changeDiversityStats(self, changeCoordinates, importance):

        div = self.diversity

        if self.diversity < changeCoordinates:
            self.diversity += importance
            if self.diversity > changeCoordinates:
                self.diversity = changeCoordinates
        elif self.diversity > changeCoordinates:
            self.diversity -= importance
            if self.diversity < changeCoordinates:
                self.diversity = changeCoordinates

        change = self.diversity - div
        self.yauth += change

    def changeReligiousImportance(self, changeCoordinates, importance):

        rel = self.religious

        if self.religious < changeCoordinates:
            self.religious += importance
            if self.religious > changeCoordinates:
                self.religious = changeCoordinates
        elif self.religious > changeCoordinates:
            self.religious -= importance
            if self.religious < changeCoordinates:
                self.religious = changeCoordinates

        change = self.religious - rel
        self.yauth += change

    def changeXStats(self, change, importance):
        if self.xecon < change:
            self.xecon += importance
            if self.xecon >change:
                self.xecon = change
        elif self.xecon > change:
            self.xecon -= importance
            if self.xecon < change:
                self.xecon = change

    def changeYStats(self, change, importance):
            if self.yauth < change:
                self.yauth += importance
                if self.yauth >change:
                    self.yauth = change
            elif self.yauth > change:
                self.yauth -= importance
                if self.yauth < change:
                    self.yauth = change

    def changeStatsXandY(self, change, importance):#change is coordinates(x,y) and importance is a float
        #if change < 0:
        if self.xecon < change[0]:
            self.xecon += importance
            if self.xecon >change[0]:
                self.xecon = change[0]
        elif self.xecon > change[0]:
            self.xecon -= importance
            if self.xecon < change[0]:
                self.xecon = change[0]

        if self.yauth < change[1]:
            self.yauth += importance
            if self.yauth >change[1]:
                self.yauth = change[1]
        elif self.yauth > change[1]:
            self.yauth -= importance
            if self.yauth < change[1]:
                self.yauth = change[1]
