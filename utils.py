#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt
import seaborn as sns


# Utility functions

### Function to change working directory
def change_path(path):
    if path:
        directory_train = '/kaggle/input/spaceship-titanic/train.csv'
        directory_test = '/kaggle/input/spaceship-titanic/test.csv'
    else:
        directory_train =  'train.csv'
        directory_test = 'test.csv'

    return directory_train, directory_test



### Function for data visualization


### Function to create pie chart
def draw_pie(values, labels, explode, color_palette, title, figsize = (12,8),  startangle = 90):

    plt.figure(figsize=figsize)

    explode_len = len(labels)
    explode = explode_len*(float(explode),)

    plt.pie(x = values,
            labels=labels,
            explode = explode,
            startangle=startangle,
            colors = sns.color_palette(color_palette),
            shadow=True, autopct='%.0f%%')
    plt.title(title)
    plt.show()


### Function to create count plot
def draw_count(x, hue, color_palette, title, xlabel, ylabel ):

    sns.countplot(x=x, hue=hue, palette = color_palette)
    plt.title(title, fontsize = 15)
    plt.xlabel(xlabel, fontsize = 15)
    plt.ylabel(ylabel, fontsize = 15)
    plt.show()
