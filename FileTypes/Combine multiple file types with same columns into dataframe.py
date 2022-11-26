#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Have user select excel sheet with needed data.
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.lift()
root.withdraw()

# This code block will open a specific file. (Uncomment the lines after this comment to use them.)
#print('Opening dialogue box for file selection. Please choose a file.')
#file_path = filedialog.askopenfilename()
#print('File selected:')

# This code block will get a directory path. (Uncomment the lines after this comment to use them.)
print('Opening dialogue box for folder selection. Please choose a folder.')
file_path = filedialog.askdirectory()
print('Folder selected:')

print(file_path)


# In[13]:


# Make sure correct files are recognized.

import os
import pandas as pd

# List the files in the directory.
files = os.listdir(file_path)
print(files)

# List of file types we want to add
file_types = ['xlsx','csv','json','xml']

# create a list of files for each file type
files_csv = [f for f in files if f[-3:] == 'csv']
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
files_json = [f for f in files if f[-4:] == 'json']
files_xml = [f for f in files if f[-3:] == 'xml']

print(files_csv,files_xlsx,files_json,files_xml)


# In[14]:


import json
import requests 
import xml.etree.ElementTree as ET

# Iterate through the files in the directory and append each one into the dataframe.
# This will only work correctly if the files have the exact same column names.
df_list = []
for f in files_csv:
    data = pd.read_csv(str(file_path) + '/' + str(f), index_col=None, header=0)
    data['Source'] = f
    df_list.append(data)
    
for f in files_xlsx:
    data = pd.read_excel(str(file_path) + '/' + str(f))
    data['Source'] = f
    df_list.append(data)
    
# Iterate through the json files and add data from each to a list.
json_list = []
for f in files_json:
    with open(str(file_path) + '/' + str(f)) as json_file:
        json_obj = json.load(json_file)
        json_obj['Source'] = f
        json_list.append(json_obj.copy())
# Turn the combined list into a dataframe.
data = pd.DataFrame(json_list)
# Add the data frame to the list of dataframes.
df_list.append(data)
    
# Iterate through the xml files and add data from each to a list.
xml_list = []
for f in files_xml:
    # create element tree object 
    tree = ET.parse(str(file_path) + '/' + str(f))
    # get root element 
    root = tree.getroot()
    # create dictionary from XML tags and values
    itemdict = {}
    for item in root:
        itemdict[item.tag] = item.text
    itemdict['Source'] = f
    xml_list.append(itemdict.copy())
# Turn the combined list into a dataframe.
data = pd.DataFrame(xml_list)
# Add the data frame to the list of dataframes.
df_list.append(data)

# Combine all the data frames in the list into a single data frame.    
df =  pd.concat(df_list, axis=0, ignore_index=True, sort=False)

# See how many rows the data frame has.
print(len(df.index))

# Show the data in the data frame.
df


# In[ ]:


# Save the dataframe to a new combined csv file.

# Add today's date to the name of the new file.
from datetime import date
today = date.today()
print(today)

filename = str(file_path) + '/' + 'NewCombinedFile_' + str(today) + '.csv'
print(filename)

df.to_csv(filename, index=False)
print('File saved.')

