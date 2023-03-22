# import pandas as pd
# import matplotlib.pyplot as plt 
# import numpy as np
# import statistics as stat
# import seaborn as sns

# ##Data Science Idea: Create a program that takes two stocks and automatically compares them using different statistical analysis
#         ## Download stocks with positive momentum and alpha and create a statistcial model predicitng how they will move in the future
#                 ## Can also be done using machine learning


# df_s = pd.read_excel("Stock_Price Data.xlsx", index_col = 0) #<-- for temporary testing of the program while wifi is down
# df_s.replace([np.inf, -np.inf, 0], np.nan).dropna(axis = 0)
# df_s.reset_index(inplace=True)

# ##Stock selection of the Stock 1 and Stock 2 (This can be exposed to yfinance library to give a larger scope of stocks)
# stock1 = "APPF"
# stock2 = "MC"

# ##This is a general function used to encompusalte all the other functions, 
# ##makes the stock selection and automation process easier
# def Data_Analysis(stock1,stock2): 

#     def price_lineplot(stock1,stock2): ##<<-- Stock Price Line plot to visualize stock prices
#         plt.plot(df_s["Date"],df_s[stock1], label=stock1)
#         plt.plot(df_s["Date"], df_s[stock2], label=stock2)
#         plt.title('Stock over Time', fontsize=14)
#         plt.xlabel('Time', fontsize=14)
#         plt.ylabel('Stock Price', fontsize=14)
#         plt.legend()
#         return plt.show()
#     price_lineplot(stock1, stock2)

#     def correlation_heatmap(): ##<<-- Correlation of all available stocks in the Stock_price Data table
#         corr = df_s.loc[:, df_s.columns!= "Date"].corr()
#         figure = plt.figure(figsize=(5,5)) 
#         sns.heatmap(corr, cmap="coolwarm", annot=True, fmt="0.2f")
#         return plt.show()
#     correlation_heatmap()

#     def Polyfit(stock1,stock2): ##<<-- Polynomial fit of the stock price with 6 degrees
#         poly_list = [stock1,stock2]
#         for j in range(2):
#             stock = poly_list[j]
#             X_data = []
#             Y_data = []
#             for i in range(len(df_s["Date"])):
#                 Y_data = list(df_s[stock])
#                 X_data.append(i)
#             params = np.polyfit(X_data, Y_data, deg=6)
#             fit = np.polyval(params, X_data)
#             fig, ax1 = plt.subplots()
#             ax1.scatter(X_data, Y_data, s=1, color='b', label= stock + ' Data points')
#             ax1.plot(X_data, fit, color='r', alpha=1, label='Polynomial fit')
#             ax1.set_title('Time Series Plot Stock Prices with Polynomial Fit')
#             plt.xlabel('Date', fontsize=14)
#             plt.ylabel('Price', fontsize=14)
#             ax1.legend()
#         plt.show()
#         return  
#     Polyfit(stock1,stock2)

#     def volatility(stock1,stock2): ##<<-- Volatility of two stocks
#         returns1 = df_s[stock1].pct_change()
#         returns2 = df_s[stock2].pct_change()
#         risk1 = returns1 - returns1.mean()
#         risk2 = returns2 - returns2.mean()
#         plt.plot(df_s["Date"],risk1)
#         plt.plot(df_s["Date"],risk2)
#         plt.title("Volatility")
#         plt.xlabel("Date")
#         plt.ylabel("Risk")
#         return plt.show()
#     volatility(stock1,stock2)

# Data_Analysis(stock1,stock2)