import pandas as pd

def load_full_data():
    df = pd.read_csv("data/match_full_time.csv")
    
    df.drop('blue_gold', axis = 1,inplace = True)
    df.drop('red_gold', axis = 1,inplace = True)
    df.drop('gameDuration', axis = 1,inplace = True)
    
    return df

def load_15m_data():
    df = pd.read_csv("data/match_15m.csv")
    
    df.drop('blue_gold', axis = 1,inplace = True)
    df.drop('red_gold', axis = 1,inplace = True)
    df.drop('current_time', axis = 1,inplace = True)
    
    return df