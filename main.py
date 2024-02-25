import joblib
import pandas as pd

from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request

from config.preprocessing import tier_value, blue_red_encoding

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/15m')
def surrender():
    return render_template("15m.html")

@app.route('/result_15m', methods = ['POST'])
def surrender_predict():
    model = joblib.load('./model/model1.pkl')
        
    team_colour = request.form['team-colour']

    bk = int(request.form['blue-kills'])
    rk = int(request.form['red-kills'])
    b_tower = int(request.form['blue-tower-destroyed'])
    r_tower = int(request.form['red-tower-destroyed'])
    b_in = int(request.form['blue-inhibitor-destroyed'])
    r_in = int(request.form['red-inhibitor-destroyed'])
    red_rift = int(request.form['red-rift'])
    blue_rift = int(request.form['blue-rift'])
    red_baron = int(request.form['red-baron'])
    blue_baron = int(request.form['blue-baron'])
    red_air = int(request.form['red-air'])
    blue_air = int(request.form['blue-air'])
    red_earth = int(request.form['red-earth'])
    blue_earth = int(request.form['blue-earth'])
    red_water = int(request.form['red-water'])
    blue_water = int(request.form['blue-water'])
    red_fire = int(request.form['red-fire'])
    blue_fire = int(request.form['blue-fire'])
    red_elder = int(request.form['red-elder'])
    blue_elder = int(request.form['blue-elder'])

    data = {'blue_kill': [bk],'red_kill': [rk],'blue_tower': [b_tower],'red_tower': [r_tower],
            'blue_inhibitor': [b_in],'red_inhibitor': [r_in],
            'b_RIF': [blue_rift],'r_RIF': [red_rift], 'b_BAR': [blue_baron],'r_BAR': [red_baron],
            'b_AIR':[blue_air],'r_AIR':[red_air],
            'b_EAR':[blue_earth],'r_EAR':[red_earth],
            'b_FIRE':[blue_fire],'r_FIRE':[red_fire],
            'b_WAT':[blue_water],'r_WAT':[red_water],
            'b_ELD':[blue_elder],'r_ELD':[red_elder] }
    df = pd.DataFrame(data)
    
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    if team_colour == 'blue':
        percent = f"{round(model.predict_proba(df_scaled)[0][0], 3) * 100}%"
    else:
        percent = f"{round(model.predict_proba(df_scaled)[0][1], 3) * 100}%"
    return render_template('result.html', predict=percent)

@app.route('/full')
def full():
    return render_template("full_time.html") 

@app.route('/result_full', methods = ['POST'])
def full_predict():
    model = joblib.load('./model/model2.pkl')
        
    team_colour = request.form['team-colour']
    
    tier = tier_value(request.form['player-tier'])
    
    first_blood = blue_red_encoding(request.form['first-blood'])
    first_tower = blue_red_encoding(request.form['first-tower'])
    first_in = blue_red_encoding(request.form['first-inhibitor'])
    first_baron = blue_red_encoding(request.form['first-baron'])
    first_dragon = blue_red_encoding(request.form['first-dragon'])
    first_rift = blue_red_encoding(request.form['first-herald'] )

    bk = int(request.form['blue-kills'])
    rk = int(request.form['red-kills'])
    b_tower = int(request.form['blue-tower-destroyed'])
    r_tower = int(request.form['red-tower-destroyed'])
    b_in = int(request.form['blue-inhibitor-destroyed'])
    r_in = int(request.form['red-inhibitor-destroyed'])
    red_rift = int(request.form['red-rift'])
    blue_rift = int(request.form['blue-rift'])
    red_baron = int(request.form['red-baron'])
    blue_baron = int(request.form['blue-baron'])
    red_air = int(request.form['red-air'])
    blue_air = int(request.form['blue-air'])
    red_earth = int(request.form['red-earth'])
    blue_earth = int(request.form['blue-earth'])
    red_water = int(request.form['red-water'])
    blue_water = int(request.form['blue-water'])
    red_fire = int(request.form['red-fire'])
    blue_fire = int(request.form['blue-fire'])
    red_elder = int(request.form['red-elder'])
    blue_elder = int(request.form['blue-elder'])

    data = {'tier': [tier], 'blue_kill': [bk],'red_kill': [rk],
            'blue_tower': [b_tower],'red_tower': [r_tower],
            'blue_inhibitor': [b_in],'red_inhibitor': [r_in],
            'blue_firstBlood': [first_blood], 'blue_firstTower': [first_tower],
            'blue_firstInhibitor': [first_in], 'blue_firstBaron': [first_baron],
            'blue_firstDragon': [first_dragon], 'blue_firstRiftHerald': [first_rift],
            'b_RIF': [blue_rift],'r_RIF': [red_rift], 'b_BAR': [blue_baron],'r_BAR': [red_baron],
            'b_AIR':[blue_air],'r_AIR':[red_air],
            'b_EAR':[blue_earth],'r_EAR':[red_earth],
            'b_FIRE':[blue_fire],'r_FIRE':[red_fire],
            'b_WAT':[blue_water],'r_WAT':[red_water],
            'b_ELD':[blue_elder],'r_ELD':[red_elder] }
    df = pd.DataFrame(data)
    
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    if team_colour == 'blue':
        percent = f"{round(model.predict_proba(df_scaled)[0][0], 3) * 100}%"
    else:
        percent = f"{round(model.predict_proba(df_scaled)[0][1], 3) * 100}%"
    return render_template('result.html', predict=percent)


if __name__ == "__main__":
    app.run()