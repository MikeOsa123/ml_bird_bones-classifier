import pickle
import numpy as np 
import traceback
from flask import Flask, request, jsonify
from sklearn.externals import joblib


model = None
app = Flask(__name__)

# previous approach to loading model
'''
def load_model():
    global model
    # model variable refers to the global variable
    with open('bird_bones_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
'''

@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    print(type(lr))
    print(lr)
    if lr and request.method == 'POST':
        try:
            data = request.get_json() # Get data posted as a json
            data = np.array(data)[np.newaxis, :] # converts shape from (n,) to (1, n)
            prediction = lr.predict(data) # runs globally loaded model on the data
            return jsonify(prediction[0])
        
        except:

            return jsonify({'trace':traceback.format_exc()})

    else:
        print('Train the model first!')
        return ('No model here to use!')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input to specify the port to use
    except:
        port = 80 # if no port is provided then the default port will be set to 80

    
    lr = joblib.load("bird_bones_trained_model.pkl") # load model at the beginning once only
    print('Model Loaded')


    app.run(host='0.0.0.0', port=port, debug=True)