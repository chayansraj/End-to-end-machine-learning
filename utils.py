#!/usr/bin/env python
# coding: utf-8

# Import libraries and packages
import numpy as np
import pandas as pd
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



### Function to print training and validation curves for neural networks
import matplotlib.pyplot as plt
def plot_results(history):

    val_loss = history.history['val_loss']
    acc = history.history['accuracy']
    loss = history.history['loss']
    val_acc = history.history['val_accuracy']

    plt.figure(figsize=(10,4))
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.plot(loss)
    plt.plot(val_loss)
    plt.legend(['Training','Validation'])

    plt.figure(figsize=(10,4))
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.plot(acc)
    plt.plot(val_acc)
    plt.legend(['Training','Validation'])

    plt.show()



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
