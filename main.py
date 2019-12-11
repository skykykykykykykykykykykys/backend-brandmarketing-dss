from flask import Flask, render_template, request
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def show_tables():
     data = pd.read_csv('/data/data.csv')
     #Provide Pie Chart with 

     country_data = data["contingent"]
     medal_data = data["gold_medal"]
     colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
     explode = (0.1, 0, 0, 0, 0)  
     plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
     autopct='%1.1f%%', shadow=True, startangle=140)
     plt.title("Gold medal achievements of five most successful\n"+"contingents in 2016 Summer Olympics")
     plt.show()



     
     data.set_index(['Name'], inplace=True)
     data.index.name=None
     females = data.loc[data.Gender=='f']
     males = data.loc[data.Gender=='m']
     return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
     titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == '__main__':
     app.run(debug=True)