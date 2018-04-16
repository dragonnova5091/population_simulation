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

class Window_2(Contrller, BaseWidget):
    def __init__(self):
        Controller.__init__(self)
        BaseWidget.__init__(self, 'window 2')

        self.text = ControlText('this is some extra text')
        self.button = ControlButton('draw_the graph')
        self.button.value = utils.drawGraph(Controller.)

class Window_1(BaseWidget):

    def __init__(self):
        super(Window_1,self).__init__('window 1')

        """#Definition of the forms fields
        self._firstname     = ControlText('First name', 'Default value')
        self._middlename    = ControlText('Middle name')
        self._lastname      = ControlText('Lastname name')
        self._fullname      = ControlText('Full name')"""


        self.controller = master.Controller()

        self.graph_button = ControlButton("show the graph")
        self.random_event_button = ControlButton('random event')
        self.save_population_button = ControlButton('save the population')

        self.graph_button.value = self.make_graph  #utils.send_to_plot(self.controller.populationBlocks))
        self.random_event_button.value = self.call_random_event
        self.save_population_button.value = self.controller.saveBlocks
        #self.label = ControlTextArea(utils.labelgraphPrint(self.controller.populationBlocks, [-10,10,-10,10]), font_size=14)
        #self.timeline = ControlEventTimeline("timeline1")
        self.label1 = ControlText('enter text here')

        #self.timeline.add_graph("name", [1,[2,3]])

        #self.make_graph()

    def call_random_event(self):
        self.controller.randomEvent()
        self.make_graph()


    def __buttonAction(self):
        print("something happended")

    def make_graph(self): #coordinates):
        if plt.get_fignums():
            plt.close()
        coordinates = utils.send_to_plot(self.controller.populationBlocks)
        plt.scatter(coordinates[0], coordinates[1], color=(0,0,0))
        plt.ylim(ymin=-10, ymax=10)
        plt.xlim(xmin=-10, xmax=10)
        plt.title('test1 ')
        plt.xlabel('economic')
        plt.ylabel('authority')
        plt.show()




#Execute the application
if __name__ == "__main__":   pyforms.start_app( Window_1 , geometry=(800,400,800,400))
