from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load your trained model using pickle
with open('D:\BIA\Captron_Project\Captron_Project\logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define label encoding for 'type'
label_mapping = {'CASH_IN': 0, 'CASH_OUT': 1, 'DEBIT': 2, 'PAYMENT': 3, 'TRANSFER': 4}

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        step = int(request.form['step'])
        type_transaction = request.form['type']  # this will be a string, e.g., 'CASH_IN'
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        # Convert the 'type' to the encoded value using label mapping
        if type_transaction not in label_mapping:
            raise ValueError(f"Invalid transaction type: {type_transaction}")
        type_encoded = label_mapping[type_transaction]

        # Prepare input for the model (ensuring 'type' is a number)
        input_data = pd.DataFrame({
            'step': [step],
            'type': [type_encoded],  # 'type' is now the encoded number
            'amount': [amount],
            'oldbalanceOrg': [oldbalanceOrg],
            'newbalanceOrig': [newbalanceOrig],
            'oldbalanceDest': [oldbalanceDest],
            'newbalanceDest': [newbalanceDest]
        })

        # Perform prediction
        prediction = model.predict(input_data)[0]

        # Return result to the frontend
        if prediction == 1:
            result = 'This transaction is fraud.'
        else:
            result = 'This transaction is NOT fraud.'
        
        return render_template('index.html', prediction_text=result)
    
    except Exception as e:
        # Handle any errors that occur during processing
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
