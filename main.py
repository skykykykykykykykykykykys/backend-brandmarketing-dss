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

     
     data.set_index(['Name'], inplace=True)
     data.index.name=None
     females = data.loc[data.Gender=='f']
     males = data.loc[data.Gender=='m']
     return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
     titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == '__main__':
     app.run(debug=True)