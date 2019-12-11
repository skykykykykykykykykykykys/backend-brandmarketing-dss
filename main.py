from flask import Flask, render_template, send_file
from io import BytesIO
import jinja2
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([
     app.jinja_loader,
     jinja2.FileSystemLoader('/templates')
])
app.jinja_loader = my_loader

@app.route('/asia')
def show_visual():
     data = pd.read_csv('/data/data.csv')
     #Provide Pie Chart with 

     fig, ax = plt.subplots()

     country_data = data["contingent"]
     medal_data = data["gold_medal"]
     colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
     explode = (0.1, 0, 0, 0, 0)  
     plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
     autopct='%1.1f%%', shadow=True, startangle=140)
     plt.title("Channel Grouping from Asia Continents")
     plt.show()



     #exporting to png
     canvas = FigureCanvas(fig)
     img = BytesIO()
     fig.savefig(img)
     img.seek(0)
     return send_file(img, mimetype='image/png')

@app.route('/')
def index():
     return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)