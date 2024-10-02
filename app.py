from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve and validate form data
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
