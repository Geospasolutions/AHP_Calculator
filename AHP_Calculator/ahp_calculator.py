import ipysheet
from ipysheet import sheet, cell
import ipywidgets as widgets
from IPython.display import display, clear_output
import numpy as np
import pandas as pd


class AHP_calculator():

    def __init__(self,):
        
        self.params = []
        self.input_params = widgets.Text(layout={'width': '550px'})
        self.save_params_button = widgets.Button(description="Done")
        self.descLabel=widgets.Label(
                'Enter all params in comma seperated form. eg: River,Road,Shettlement')
        self.grid = None
        self.inputs_widgets = {}
        self.output = widgets.Output()
        self.bottomWidgets = widgets.VBox()
        self.allwidgets = widgets.VBox([])

        self.save_params_button.on_click(self.params_save)

    def params_save(self, change):
        self.params = self.input_params.value.split(',')
        self.grid = widgets.GridspecLayout(
            len(self.params)+1, len(self.params)+1)
        self.allwidgets.children = [
            self.descLabel,
            widgets.HBox([
                self.input_params, self.save_params_button]), self.grid, self.bottomWidgets, self.output]
        self.build_grid()
        self.convertInputToNumpyarray()

    def create_Input(self, default=0):
        return widgets.FloatText(
            value=default,
            layout=widgets.Layout(width='50px',color='red'),
            disabled=False,
            color='red'
        )

    def get_input_widget(self, owner):
        for key, value in self.inputs_widgets.items():
            if(value == owner):
                k = key
                break
        return k

    def convertInputToNumpyarray(self):

        length = len(self.params)
        mat = np.full((length, length), 1, dtype=float)
        for i in range(1, length+1):
            for j in range(1, length+1):
                mat[i-1, j-1] = self.grid[i, j].value
        print(mat,self.grid[1,1])

    # def onCalculate():

    def onchange(self, change):
        owner = change['owner']
        [row, column] = self.get_input_widget(owner).split('-')
        row = int(row)
        column = int(column)
        if(self.grid[column, row].value != change['new']):
            self.grid[column, row].value = 1/change['new']
        if(row == column and (row != 0 and column != 0)):
            self.grid[column, row].value = 1

    def build_grid(self):
        for i in range(len(self.params)+1):
            for j in range(len(self.params)+1):
                if(i != j and (i == 0 or j == 0)):
                    if(i == 0):
                        labelindex = j-1
                    else:
                        labelindex = i-1

                    self.grid[i, j] = widgets.Label(
                        self.params[labelindex])

                if(i != 0 and j != 0):
                    self.grid[i, j] = self.create_Input()
                    self.inputs_widgets['{}-{}'.format(i, j)] = self.grid[i, j]
                    self.grid[i, j].observe(self.onchange, 'value')

                if(i == j and (i != 0 and j != 0)):
                    self.grid[i, j] = self.create_Input(default=1,)
                    self.inputs_widgets['{}-{}'.format(i, j)] = self.grid[i, j]
                    self.grid[i, j].observe(self.onchange, 'value')

    def open_calculator(self):

        self.allwidgets.children = [
            self.descLabel,
            widgets.HBox([
                self.input_params, self.save_params_button]), self.bottomWidgets, self.output]

        return self.allwidgets
