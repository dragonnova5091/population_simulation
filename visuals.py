import os
#os.system('pip install pyforms')

import utils
import popBlock
import master

try:
    import pyforms
except:
    os.system('pip install pyforms')
    import pyforms

from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

try:
    import matplotlib
except:
    os.system('pip install matplotlib')
    import matplotlib

import matplotlib.pyplot as plt



PYFORMS_STYLESHEET = 'style.css'


class Window_1(BaseWidget):

    def __init__(self):
    #    print("it is running")
        super(Window_1,self).__init__('window 1')
    #    print("it is running")

        #self.second_window = Window_2()

        self.day_current = 1

        self.controller = master.Controller()

        self.graph_button = ControlButton("show the graph")
        self.days = ControlText('how many days have passed')
        self.random_event_button = ControlButton('enter')
        self.save_population_button = ControlButton('save the population')
        self.other_window_button = ControlButton('other window')

        self.graph_button.value = self.make_graph  #utils.send_to_plot(self.controller.populationBlocks))
        self.random_event_button.value = self.call_random_event
        self.save_population_button.value = self.controller.saveBlocks
        self.other_window_button.value = self.open_other_window
        #self.label = ControlTextArea(utils.labelgraphPrint(self.controller.populationBlocks, [-10,10,-10,10]), font_size=14)
        #self.timeline = ControlEventTimeline("timeline1")

        #BaseWidget.generate_tabs(dictionary)
        self.mainmenu = [
            {'File': [
                {'exit': exit()},
                {'test1': self.__buttonAction()}
            ]
            }
        ]
        #self.timeline.add_graph("name", [1,[2,3]])

        #self.make_graph()
    def open_other_window(self):
        pyforms.start_app( Window_2, geometry=(400,400,400,400))

    def call_random_event(self):
        self.day_current += int(self.days.value)

        self.controller.timepassing(self.days.value)

        self.make_graph()


    def __buttonAction(self):
        print("something happended")

    def make_graph(self): #coordinates):
        if plt.get_fignums():
            plt.close()
        coordinates = utils.send_to_plot(self.controller.populationBlocks)
        #plt.scatter([], [])
        #plt.show()
        plt.scatter(coordinates[0], coordinates[1], color=(0,0,0))
        plt.ylim(ymin=-10, ymax=10)
        plt.xlim(xmin=-10, xmax=10)
        plt.title("day " + str(self.day_current))
        plt.xlabel('economic')
        plt.ylabel('authority')
        plt.show()




#Execute the application
if __name__ == "__main__":  pyforms.start_app( Window_1 , geometry=(800,400,800,400))
    #pyforms.start_app( Window_2, geometry=(400,400,400,400))
