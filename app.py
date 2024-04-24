import pickle
import numpy as np
from flask import Flask, request, render_template
my_app = Flask(__name__)

# Load the model
xgboostmodel = pickle.load(open('xgboost.pkl', 'rb'))

@my_app.route('/')
def home():
    return render_template('index.html')

@my_app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = [float(x) for x in request.form.values()]
    
    # Convert features to a numpy array
    X = np.array([data])
    
    # Make predictions
    predictions = xgboostmodel.predict(X)
    
    
    # Print predictions
    print("Predictions:", predictions)
    
    # Interpret predictions
    if predictions[0] == 0:
        predict_value = "does not need to be addmitted"
    elif predictions[0] == 1: 
        predict_value = "likely to have a regular case of Covid-19 and is predicted to be admitted in a regular ward"
    elif predictions[0] == 2:
        predict_value = "likely to become semi-intensive and should be monitored closely"
    else:
        predict_value = "likely to become a critical case and should be prepared for intensive care"
    
    return render_template("index.html", prediction_text="This patient is {}".format(predict_value))

if __name__ == "__main__":
    my_app.run(debug=True)
