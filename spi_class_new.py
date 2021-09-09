# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:46:24 2021

@author: ShendR
"""

from nptdms import TdmsFile
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from tkinter import filedialog
from tkinter import *
import numpy as np


class SPI_tDMS_Data(object):
    def __init__(self):
        self.channels = []
        self.groups = []
        self.root_obj_keys=[]
        self.root_obj_values=[]
            
    
    def run_open_tdms(self):
            # Open tDMS file        
        root = Tk()
        root.withdraw()
        root.call('wm', 'attributes', '.', '-topmost', True)
        root.filename = filedialog.askopenfilename(initialdir='C:\ShendR\Python\SPI tDMS\TDMS files' , title='Select a file', filetypes=(('TDMS files', '*.tdms'),('All files','*.*')))
        self.tdms_file = TdmsFile(root.filename)
        root.destroy()
        root.mainloop()
        
            # Get basic info from file
        root_object=self.tdms_file.object()
        root_properties=root_object.properties.items()
        for key, value in root_properties:
            self.root_obj_keys.append(key)
            self.root_obj_values.append(value)
            
            # Get Channels names from file Groups
        self.groups = self.tdms_file.groups()    
        channel_list = self.tdms_file.group_channels(self.groups[0])
        for c in channel_list:
            self.channels.append(c.channel)
                    
        return self.tdms_file
    
    
    def get_data_nparray(self, channel='TimeStamp'):
        channels_data = self.tdms_file.object(self.groups[0], channel)
        data = channels_data.data
        unit = channels_data.property('Unit') #-------------Unit
        nparray = np.array(data)
        return [nparray, unit]
    
    def plot_channels_data(self, channel):
        x = self.get_data_nparray()[0]              #-----------TimeStamp
        x_unit = self.get_data_nparray()[1]         #---------TimeStamp unit
        y = self.get_data_nparray(channel)[0]
        y_unit = self.get_data_nparray(channel)[1]
        plt.plot(x,y)
        plt.xlabel('Time' + ' [' + x_unit + ']')
        plt.ylabel(channel + ' [' + y_unit + ']')
        
        
    def plot_clicked(self, plot_area, item_clicked):
        x = self.get_data_nparray()[0]              #-----------TimeStamp
        x_unit = self.get_data_nparray()[1]         #---------TimeStamp unit
        y = self.get_data_nparray(item_clicked)[0]
        y_unit = self.get_data_nparray(item_clicked)[1]
        
        plot_area.fig.clf()
        itemclicked = plot_area.fig.add_subplot(111)
        itemclicked.plot(x, y)
        itemclicked.set_ylabel(item_clicked + ' ' + '[' + y_unit + ']')    
        itemclicked.set_xlabel('TimeStamp' +' [s]')           
        plot_area.draw()
    
    
    
    
#spi_data = SPI_tDMS_Data()
#spi_data.run_open_tdms()
#spi_data.channels
#spi_data.groups
#spi_data.root_obj_values
#spi_data.get_data_nparray()
#spi_data.plot_channels_data('Heat 0 Timeout')