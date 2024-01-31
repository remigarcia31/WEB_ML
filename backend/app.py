from flask import Flask, render_template, request, send_file
import pkg_resources

devmode = True

app = Flask(__name__,
        static_folder = "../frontend/dist/assets",
        template_folder = "../frontend/dist")

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/api/python_pkg')
def pkg():
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s  %s" % (i.key, i.version) for i in installed_packages])
    return installed_packages_list


@app.route('/api/mode')
def getMode():
    return {"devmode":devmode}

@app.route('/api/upload', methods=['POST'])
def upload():
    import os
    if request.method == 'POST':
        csvFile = request.files['csvFile']
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path + "/datasets", csvFile.filename)
        csvFile.save(file_path)
    print(csvFile)
    return "File uploaded"

@app.route('/api/predict/<string:csvName>/<string:modelName>/<string:selectLearningTask>/<string:target>/<int:splitvalue>')
def predict(csvName:str, modelName:str, selectLearningTask:str,target:str,splitvalue:int):
    import os
    import xgboost as xgb
    import sklearn as sk
    import pandas as pd
    from io import BytesIO

    # Select model that will be used for training
    if modelName.lower() == "xgboost":
        if selectLearningTask.lower() == "classification":
            model = xgb.XGBClassifier()
        else:  
            model = xgb.XGBRegressor()

    if modelName.lower() == "adaboost":
        if selectLearningTask.lower() == "classification":
            from sklearn.ensemble import AdaBoostClassifier
            model = AdaBoostClassifier()
        else:
            from sklearn.ensemble import AdaBoostRegressor
            model = AdaBoostRegressor()
    

    # Load data
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path,csvName)
    df = pd.read_csv(file_path)

    # Split data into X and y
    y = df[target]
    X = df.drop(target,axis=1)

    # Label Encode Y
    y = sk.preprocessing.LabelEncoder().fit_transform(y)

    # Split into train and test
    X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(X, y, test_size=(splitvalue/10), random_state=42)
    # Train model
    if modelName.lower() == "xgboost":
        if selectLearningTask.lower() == "classification":
            model.fit(X_train,y_train, eval_set=[(X_train, y_train), (X_test, y_test)], eval_metric='mlogloss')
        else:
            model.fit(X_train,y_train, eval_set=[(X_train, y_train), (X_test, y_test)], eval_metric='rmse')

        # Get results
        results = model.evals_result()

        # Plot results
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig = plt.figure()
        if selectLearningTask.lower() == "classification":
            plt.plot(results['validation_0']['mlogloss'], label='Train')
            plt.plot(results['validation_1']['mlogloss'], label='Test')
        else:
            plt.plot(results['validation_0']['rmse'], label='Train')
            plt.plot(results['validation_1']['rmse'], label='Test')
        plt.legend()
        plt.title("Model Accuracy")

        img = BytesIO() 
        fig.savefig(img, format='png')
        img.seek(0)

        model.save_model('models/model.json')

        return send_file(img, mimetype='image/png')
    else:
        model.fit(X_train,y_train)

        # Predict
        y_val_pred = model.predict(X_test)

        # Evaluate
        if selectLearningTask.lower() == "classification":
            score = sk.metrics.accuracy_score(y_test,y_val_pred)
            train = sk.metrics.accuracy_score(y_train,model.predict(X_train))
        else:
            score = sk.metrics.mean_squared_error(y_test,y_val_pred)
            train = sk.metrics.mean_squared_error(y_train,model.predict(X_train))

        # Plot results
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig = plt.figure()
        plt.bar(['Training Set', 'Evaluation Set'], [score, train], color=['blue', 'orange'])
        plt.ylim(0, 1)
        plt.title("Model Accuracy")

        img = BytesIO() 
        fig.savefig(img, format='png')
        img.seek(0)

        model.save_model('models/model.json')
        
        return send_file(img, mimetype='image/png')
    



if __name__ == '__main__':
    app.run(port=4000,debug=devmode)