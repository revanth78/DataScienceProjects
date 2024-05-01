from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def predict():
    if request.method == "POST":
    # Get feature values from form
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        feature4 = float(request.form['feature4'])
        feature5 = float(request.form['feature5'])
        feature6 = float(request.form['feature6'])
        feature7 = float(request.form['feature7'])
        feature8 = float(request.form['feature8'])
        feature9 = float(request.form['feature9'])
        feature10 = float(request.form['feature10'])


    # Add more features as needed

    # Make prediction
    predicted_genre = model.predict([[feature1, feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10]])[0]

    return render_template('result.html', genre=predicted_genre)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
