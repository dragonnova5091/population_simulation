import random
import os
import popBlock
import utils
import time
import threading

try:
    import pickle
except:
    os.system('pip install pickle')
    import pickle



GRAPHRANGE = [-10,10,-10,10]
PATH = os.getcwd() #"e:\programming\python programs\large projects\population simulation"
EVENTLIKELYNESS = 0.05

class Controller:
    def __init__(self):
        #self.accessPopulationBlocks()
        #self.makeBlocks()
        #self.saveBlocks()
        #self.populationBlocks = None
        #self.loadPopulationBlocks()

        inputt = input("do you wish to load you previous population? y/n ")
        #inputt = "n"
        if inputt == "y":
            self.loadPopulationBlocks()
        else:
            self.makeBlocks()
            self.saveBlocks()

        #utils.drawGraph(self.populationBlocks, GRAPHRANGE)

        #self.eventscheduler = sched.scheduler(time.time, time.sleep)

        #for i in range(0,10):
        #self.timepassing()

        self.starttime = time.time()
        #self.schedule()

        self.events_list = []




        #utils.drawGraph(self.populationBlocks, GRAPHRANGE)
        print("--------------------------------")
    def update(self):
        print("0")

    def makeBlocks(self):
        pop = []
        #size = int(input("how many population blocks? >: "))
        size = 100
        for i in range(0,size):
            pop.append(popBlock.Block())
        print("Initialized Population")
        #utils.drawGraph(pop, GRAPHRANGE)

        self.populationBlocks = pop

    def saveBlocks(self):
        os.chdir(PATH)
        #os.chdir("popchunks")

        found = False
        for obj in os.listdir("."):
            if obj == "popchunks":
                found = True

        if found == False:
            os.mkdir("popchunks")
        os.chdir("popchunks")

        file = open("popchunks.txt", "wb")

        pickle.dump(self.populationBlocks, file)

        file.close

    def loadPopulationBlocks(self):
        os.chdir(PATH)
        #print(os.listdir("."))

        found = False
        for obj in os.listdir("."):
            if obj == "popchunks":
                found = True

        if found == False:
            os.mkdir("popchunks")
        os.chdir("popchunks")

        found = False
        for obj in os.listdir("."):
            if obj == "popchunks.txt":
                found = True

        if found is True:
            file = open("popchunks.txt", "rb")
            self.populationBlocks = pickle.load(file)

    def schedule(self):



        if time.time() - self.starttime > 10:
            self.timepassing()
            self.starttime = time.time()






    def timepassing(self, days):
        #time.sleep(5)
        #self.schedule_timepassing(5)
        for i in range(0, int(days)):

            if random.uniform(0,1) < EVENTLIKELYNESS:
                self.randomEvent()
                #time.sleep(2)
            else:
                if random.uniform(0,1) < EVENTLIKELYNESS * 3:
                    for block in self.populationBlocks:
                        block.spreadStats()

        #utils.drawGraph(self.populationBlocks, GRAPHRANGE)

        ##self.thread2.run()


    def changeAllBlocks(self, arg, extra=None):
        if extra is not None:
            print(extra)
        for block in self.populationBlocks:
            eval("block." + arg)


    def return_closest(self, n, keys):
        round_to = keys[0]
        for index, key in enumerate(keys):
            if n > key:
                round_to = keys[index+1]
        return(round_to)


    def randomEvent(self):
        percent = random.randint(0,100)
        #percent = 95
        """
        events = {
            22: ["the market is improving", "changeEconStats(10, 1)"],
            40: ["the market is decreasing", "changeEconStats(-10, 1)"],
            46: ["diversity is increasing", "changeDiversityStats(-10, 1)"],
            50: ["diversity is decreasing", "changeDiversityStats(10, 1)"],
            56: ["the cities are becoming more urban", "changeLocationStats(-10, 1)"],
            60: ["the cities are becoming more rural", "changeLocationStats(10, 1)"],
            62: ["an influential book was written", "changeStatsXandY([random.uniform(-7.0, 7.0), random.uniform(-7.0, 7.0)], random.uniform(1.0, 3.0))"]
            100: ["the public polarizes themselves", "polarize()"]

        }
        self.changeAllBlocks(events[self.return_closest(percent, list(events.keys()))][1])
        print(events[self.return_closest(percent, list(events.keys()))][0]) """

        event=""

        if percent < 22:
            event = "the market is improving"
            for block in self.populationBlocks:
                block.changeEconStats(5, 1)
        elif percent < 40:
            event = "the market is decreasing"
            for block in self.populationBlocks:
                block.changeEconStats(-5, 1)
        elif percent < 46:
            event = "diversity is increasing"
            for block in self.populationBlocks:
                block.changeDiversityStats(-5, 1)
        elif percent < 50:
            event = "diversity is decreasing"
            for block in self.populationBlocks:
                block.changeDiversityStats(5, 1)
        elif percent < 56:
            event = "the cities are becoming more urban"
            for block in self.populationBlocks:
                block.changeLocationStats(-5, 1)
        elif percent < 60:
            event = "the cities are becoming more rural"
            for block in self.populationBlocks:
                block.changeLocationStats(5, 1)
        elif percent < 62:
            event = "an influential book was written "
            location = [random.uniform(-7.0, 7.0), random.uniform(-7.0, 7.0)]
            event = event + "the public draws towards" + str(location[0]) + " " + str(location[1])
            for block in self.populationBlocks:
                block.changeStatsXandY(location, random.uniform(1.0, 3.0))
        elif percent < 63:
            event = "a natural disaster occurs"
            for block in self.populationBlocks:
                block.changeYStats(10.0, 2)
        elif percent < 64:
            event = "a famine occurs"
            for block in self.populationBlocks:
                block.changeYStats(10.0, 2)
        elif percent < 66:
            event = "a massacre occurs"
            for block in self.populationBlocks:
                block.changeYStats(10.0, 3)
        elif percent < 71:
            event = "the economy drops"
            for block in self.populationBlocks:
                block.changeEconStats(-10, 3)
        elif percent < 76:
            event = "the economy spikes"
            for block in self.populationBlocks:
                block.changeEconStats(10, 3)
        elif percent < 80:
            event = "New Technology is created"
            for block in self.populationBlocks:
                block.changeStatsXandY([4,-3], 1.5)
        elif percent < 90:
            event = "the public opinion shifts towards "
            location = [random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)]
            event = event + str(location[0]) + " " + str(location[1])
            importance = random.uniform(1,5)
            event = event + "by " + str(importance) + "amount"
            for block in self.populationBlocks:
                block.changeStatsXandY(location, importance)
        elif percent < 100:
            event = "the public are left alone, and polarize themselves"
            for block in self.populationBlocks:
                block.spreadStats()


        print(event)

        self.events_list.append(event)
