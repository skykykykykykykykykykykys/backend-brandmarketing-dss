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
df = pd.read_csv('/data/data.csv')
continent = df.groupby('contingent')

@app.route('/pie1/')
def show_visual():
     #Provide Pie Chart with Asia and Channel Group
     continent_count = {'Americas': 0, 'Asia': 0, 'Europe': 0, 'Oceania': 0, 'Africa': 0}
     for continent in df['continents']:
          if continent == 'Americas':
               continent_count['Americas'] += 1
          if continent == 'Asia':
               continent_count['Asia'] += 1
          if continent == 'Europe':
               continent_count['Europe'] += 1
          if continent == 'Oceania':
               continent_count['Oceania'] += 1
          if continent == 'Africa':
               continent_count['Africa'] += 1
     
     labels = continent_count.keys()
     data = continent_count.values()
     explode = (0.05, 0, 0,0,0)

     plt.figure(figsize=(5,5))
     plt.pie(data, labels=labels, explode=explode, autopct='%1.1f%%', startangle=55)
     plt.title('Visits per Continent')
     plt.axis('equal') 
     fig, ax = plt.subplots()
     continent_data = continent["asia"]
     


     #medal_data = data["gold_medal"]
     #colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
     #explode = (0.1, 0, 0, 0, 0)  
     #plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
     #autopct='%1.1f%%', shadow=True, startangle=140)
     #plt.title("Channel Grouping from Asia Continents")

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