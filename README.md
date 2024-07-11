# Sleep Efficiency Predictor

This project is a Flask web application that predicts sleep efficiency and other sleep metrics based on user input. The model used for prediction is a pre-trained Gradient Boosting model saved as `multioutput_gb_model.pkl`.

## Features

- Predicts the following sleep metrics:
  - Sleep efficiency
  - REM sleep percentage
  - Deep sleep percentage
  - Light sleep percentage
- Uses user input for age, gender, sleep duration, awakenings, exercise frequency, caffeine consumption, alcohol consumption, and smoking status.

## Setup and Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sleep-efficiency-predictor.git
    cd sleep-efficiency-predictor
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the web application.

## Usage

1. Enter the required input values in the web form:
   - Age
   - Gender (Male/Female)
   - Sleep duration
   - Awakenings
   - Exercise frequency
   - Caffeine consumption
   - Alcohol consumption
   - Smoking status (Non-smoker/Smoker)

2. Click the "Predict" button.

3. The predicted sleep metrics will be displayed on the same page.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the web interface.
- `multioutput_gb_model.pkl`: The pre-trained model file (not included in the repository).
- `model.ipynb`: Jupyter notebook used for training the model.
- `Sleep_Efficiency.csv`: Dataset used for training the model.
- `requirements.txt`: List of Python packages required for the project.

## Model Training (Optional)

The model was trained using the `Sleep_Efficiency.csv` dataset and the `model.ipynb` notebook. If you want to train the model yourself, follow these steps:

1. Open `model.ipynb` in Jupyter Notebook or JupyterLab.
2. Ensure `Sleep_Efficiency.csv` is in the same directory as the notebook.
3. Run all cells in the notebook to preprocess the data, train the model, and save the trained model as `multioutput_gb_model.pkl`.

