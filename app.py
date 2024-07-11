from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained model
with open('multioutput_gb_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input values from form
    age = int(request.form['Age'])
    gender = int(request.form['Gender'])
    sleep_duration = float(request.form['Sleep duration'])
    awakenings = float(request.form['Awakenings'])
    exercise_frequency = float(request.form['Exercise frequency'])
    caffeine_consumption = float(request.form['Caffeine consumption'])
    alcohol_consumption = float(request.form['Alcohol consumption'])
    smoking_status = request.form['Smoking status']
    
    # Convert input values to match training data format
    input_data = {
        'Age': age,
        'Gender': gender,
        'Sleep duration': sleep_duration,
        'Awakenings': awakenings,
        'Exercise frequency': exercise_frequency,
        'Caffeine consumption': caffeine_consumption,
        'Alcohol consumption': alcohol_consumption,
        'Smoking status_No': 1 if smoking_status == 'No' else 0,
        'Smoking status_Yes': 1 if smoking_status == 'Yes' else 0
    }

    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])
    
    # Make prediction using the model
    prediction = model.predict(input_df)
    
    # Prepare the prediction output
    output = {}
    metrics = ['Sleep efficiency', 'REM sleep percentage', 
               'Deep sleep percentage', 'Light sleep percentage']
    
    for i, metric in enumerate(metrics):
        output[metric] = prediction[0][i]
    
    return render_template('index.html', prediction=output)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
