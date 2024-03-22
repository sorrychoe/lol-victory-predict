import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from config.data import load_full_data, load_15m_data
from config.preprocessing import spread_monster, set_blue_score, tier_encoding

def clf_model_15m():
    data = load_15m_data()
    df = spread_monster(data)

    real_df = df.drop(["matchId", "blue_win"], axis=1)
    scaler = StandardScaler()
    scaler.fit(real_df)

    X = scaler.transform(real_df)

    y = df['blue_win'].to_numpy()

    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, './model/model1.pkl')
    
    
def clf_model_full():
    data = load_full_data()
    data2 = spread_monster(data)
    data3 = set_blue_score(data2)
    df = tier_encoding(data3)

    real_df = df.drop(["matchId", "makeTime", "blue_win"],axis=1)
    scaler = StandardScaler()
    scaler.fit(real_df)

    X = scaler.transform(real_df)

    y = df['blue_win'].to_numpy()

    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, './model/model2.pkl')
    
    
if __name__ == "__main__":
    clf_model_full()
    clf_model_15m()