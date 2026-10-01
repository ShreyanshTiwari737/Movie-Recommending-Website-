import os
print("Current Working Directory:", os.getcwd())
import pandas as pd
from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/secondpage')
def secondpage():
    return render_template("secondpage.html")
@app.route('/Submit',methods=['POST'])
def submit():
    visit=0
    enjoy=0
    read=0
    holiday=0
    feeling=0
    villain=0

    visit=int(request.form.get('visit'))
    enjoy=int(request.form.get('enjoy'))
    read=int(request.form.get('read'))
    holiday=int(request.form.get('holiday'))
    feeling=int(request.form.get('feeling'))
    villain=int(request.form.get('villain'))
    
    time=(visit)
    pace=(enjoy)
    logic=(read)
    setting=(holiday)
    mood=(feeling)
    conflict=(villain)

    return redirect(url_for('movie',time=time,pace=pace,logic=logic,setting=setting,mood=mood,conflict=conflict))
@app.route('/movie')
def movie():
    data = pd.read_csv("moviesheet2.csv")
    time=int(request.args.get('time',0))
    pace=int(request.args.get('pace',0))
    logic=int(request.args.get('logic',0))
    setting=int(request.args.get('setting',0))
    mood=int(request.args.get('mood',0))
    conflict=int(request.args.get('conflict',0))

    if(logic==-1):
        if(mood==1):
            if(conflict==-1):
                movie_data = data['Action'].sample(n=5, random_state=1)
            else:
                movie_data = data['Scifi'].sample(n=2, random_state=1)
                movie_data = data['Horror'].sample(n=2, random_state=1)
        else:
            movie_data = data['Comedy'].sample(n=5, random_state=1)
    else:
        if(pace==1):
            if(setting==1):
                if(conflict==-1):
                    movie_data = data['Action'].sample(n=2, random_state=1)
                    movie_data = data['Thriller'].sample(n=2, random_state=1)
                else:
                    movie_data = data['Scifi'].sample(n=5, random_state=1)
            else:
                movie_data = data['Horror'].sample(n=5, random_state=1)
        else:
            if(conflict==-1):
                if(mood==-1):
                    movie_data = data['Romantic'].sample(n=5, random_state=1)
                else:
                    movie_data = data['Dramatic'].sample(n=5, random_state=1)
            else:
                if(setting==1):
                    movie_data = data['Scifi'].sample(n=2, random_state=1)
                    movie_data = data['Biopic'].sample(n=2, random_state=1)
                else:
                    movie_data = data['Horror'].sample(n=5, random_state=1)
                
    return render_template('movie.html',movie_data=movie_data, time=time, pace=pace, logic=logic, setting=setting, mood=mood, conflict=conflict)
if __name__=="__main__":
    app.run(debug=True)