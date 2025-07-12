from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])

def predict():
    try:
        # Retrieve and validate form data
        
        if request.method == 'GET':
            return "This route is for form submission only. Go to '/' instead."

        data = [
            int(request.form['id']),
            int(request.form['age']),
            int(request.form['experience']),
            float(request.form['income']),
            int(request.form['zipcode']),
            int(request.form['family']),
            float(request.form['ccavg']),
            int(request.form['education']),
            float(request.form['mortgage']),
            int(request.form['securities']),
            int(request.form['cdaccount']),
            int(request.form['online']),
        ]
        
        # Debugging: Print the input data to verify correctness
        print("Received Data: ", data)

        # Ensure data has exactly 12 values
        if len(data) != 12:
            raise ValueError("Expected 12 input fields, but got a different number.")

        # Perform prediction using the loaded model
        prediction = model.predict([data])

        # Return the result
        result = 'Approved' if prediction == 1 else 'Not Approved'
        return f"<script>alert('Your loan application is: {result}');window.location='/'</script>"
    
    except Exception as e:
        # Print the error to the console for debugging
        print("Error during prediction:", str(e))
        # Return a user-friendly error message
        return f"<script>alert('An error occurred: {str(e)}');window.location='/'</script>"

if __name__ == '__main__':
    app.run(debug=True)
