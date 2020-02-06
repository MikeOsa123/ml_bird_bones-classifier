import pickle
import numpy as np
from flask import Flask, request


model = None
app = Flask(__name__)

def load_model():
    global model
    # model variable refers to the global variable
    with open('bird_bones_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json() # Get data posted as a json
        data = np.array(data)[np.newaxis, :] # converts shape from (n,) to (1, n)
        prediction = model.predict(data) # runs globally loaded model on the data
        print(prediction[0])
    return (prediction[0])


if __name__ == '__main__':
    load_model() # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)