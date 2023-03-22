import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statistics as stat
import seaborn as sns
from graphic_class import DataAnalysis
import yfinance as yf

##Data Science Idea: Create a program that takes two stocks and automatically compares them using different statistical analysis
        ## Download stocks with positive momentum and alpha and create a statistcial model predicitng how they will move in the future
                ## Can also be done using machine learning


##Stock selection of the Stock 1 and Stock 2 (This can be exposed to yfinance library to give a larger scope of stocks)

data = DataAnalysis()
data.stock = ["MSFT","TSLA"]
data.add_stock_info()
data.polyfit(6)
data.lineplot()