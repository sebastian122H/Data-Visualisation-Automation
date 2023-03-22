import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import statistics as stat
import seaborn as sns
import yfinance as yf


TIME_PERIOD = "1y"
INTERVAL = "1wk"
IGNORE_TZ = True
PREPOST = False


## class File for creating the Data objects that should allow us to make the main.py page simpler

class DataAnalysis:

    def __init__(self):
        self.stock = ""

    def add_stock_info(self):
        self.df_s = yf.download(tickers = self.stock, period = TIME_PERIOD, interval = INTERVAL, ignore_tz = IGNORE_TZ, prepost = PREPOST)
        self.df_s.replace([np.inf, -np.inf, 0], np.nan).dropna(axis = 0)
        self.df_s.reset_index(inplace=True)

    def lineplot(self): ##<<-- Stock Price Line plot to visualize stock prices
        plt.plot(self.df_s["Date"],self.df_s["Close"], label=self.stock)
        plt.title('Stock over Time', fontsize=14)
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Stock Price', fontsize=14)
        plt.legend()
        return plt.show()
    
    def corr_heatmpat(self):  ##<----- Use the entire DataFrame and correlates ALL elements. 
                                ##Does not work if only two singular stocks are used
        corr = self.df_s.loc[:, df_s.columns!= "Date"].corr()
        figure = plt.figure(figsize=(5,5)) 
        sns.heatmap(corr, cmap="coolwarm", annot=True, fmt="0.2f")
        return plt.show()

    def polyfit(self, deg): ##<<-- Polynomial fit of the stock price
        for j in range(len(self.stock)):
            stock = self.stock[j]
            Y_data = []
            X_data = []
            for i in range(len(self.df_s["Date"])):
                Y_data = list(self.df_s["Close"][stock])
                X_data.append(i)
            params = np.polyfit(X_data, Y_data, deg=deg)
            fit = np.polyval(params, X_data)
            fig, ax1 = plt.subplots()
            ax1.scatter(X_data, Y_data, s=1, color='b', label= stock + ' Data points')
            ax1.plot(X_data, fit, color='r', alpha=1, label='Polynomial fit')
            ax1.set_title('Time Series Plot Stock Prices with Polynomial Fit')
            plt.xlabel('Date', fontsize=14)
            plt.ylabel('Price', fontsize=14)
            ax1.legend()
        return plt.show()

    def volatility(self, stock1, stock2):
        returns1 = self.df_s[stock1].pct_change()
        returns2 = self.df_s[stock2].pct_change()
        risk1 = returns1 - returns1.mean()
        risk2 = returns2 - returns2.mean()
        plt.plot(df_s["Date"],risk1)
        plt.plot(df_s["Date"],risk2)
        plt.title("Volatility")
        plt.xlabel("Date")
        plt.ylabel("Risk")
        return plt.show()
    
