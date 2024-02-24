import pandas as pd

def spread_monster(df):
    blue_list = ['b_RIF','b_BAR','b_AIR','b_EAR','b_FIRE','b_WAT','b_ELD']
    red_list = ['r_RIF','r_BAR','r_AIR','r_EAR','r_FIRE','r_WAT','r_ELD']
    monster_list = ['RIFTHERALD','BARON_NASHOR','AIR_DRAGON','EARTH_DRAGON','FIRE_DRAGON','WATER_DRAGON','ELDER_DRAGON']

    for i in range(len(monster_list)):
        df[blue_list[i]] = df["blue_monster"].apply(lambda x : monster_list[i] in x).astype(int)
        df[red_list[i]] = df["red_monster"].apply(lambda x : monster_list[i] in x).astype(int)
    
    df.drop('blue_monster', axis = 1,inplace = True)
    df.drop('red_monster', axis = 1,inplace = True)
    return df

def set_blue_score(df):
    blue_list2 = ['blue_firstBlood' , 'blue_firstTower' ,'blue_firstInhibitor' ,'blue_firstBaron' ,'blue_firstDragon' ,'blue_firstRiftHerald']

    for i in range(len(blue_list2)):
        df[blue_list2[i]] = df[blue_list2[i]].astype(int)
    return df

def tier_encoding(df):
    tier_list = ['BRONZE','SILVER','GOLD','PLATINUM','DIAMOND']
    
    for i in range(len(tier_list)):
        df.loc[df['tier'] == tier_list[i] ,'tier'] = i
        
    return df

def blue_red_encoding(form):
    if form == 'red':
        return 0
    else:
        return 1
    
def tier_value(form):
    tier_dict = {'bronze': 0,'silver': 1,'gold':2,'platinum':3,'diamond':4}
    if form in tier_dict:
        return tier_dict[form]
    else:
        return -1
    
