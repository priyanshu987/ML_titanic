def predict_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    x = [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    rf = pickle.load(open('my_titanic_model.sav', 'rb'))
    prediction = rf.predict(x)
    if prediction == 1:
        prediction = 'survived'
    elif prediction == 0:
        prediction = 'Not Survived'
    return prediction
