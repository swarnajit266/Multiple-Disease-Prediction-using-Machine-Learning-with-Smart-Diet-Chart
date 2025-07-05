from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained models
heart_model = joblib.load('model1.pkl')
diabetes_model = joblib.load('model2.pkl')
dengue_model = joblib.load('model3.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/predict', methods=['POST'])
def predict():
    # print("Received form data:", request.form)
    disease_type = request.form.get('disease_type')
    result_message = ''

    if disease_type == 'heart':
        features = [
            float(request.form.get('age')),
            float(request.form.get('gender')),
            float(request.form.get('chest_pain')),
            float(request.form.get('resting_blood_pressure')),
            float(request.form.get('serum_cholestoral')),
            float(request.form.get('fasting_blood_sugar')),
            float(request.form.get('resting_electrocardiographic')),
            float(request.form.get('max_heart_rate')),
            float(request.form.get('exercise_angina')),
            float(request.form.get('st_depression')),
            float(request.form.get('st_slope')),
            float(request.form.get('major_vessel')),
            float(request.form.get('thal'))
        ]
        input_data = np.array([features])
        prediction = heart_model.predict(input_data)
        # print("Prediction result (diabetes):", prediction)
        result_message = "The person has Heart Disease" if int(prediction[0]) == 1 else "The person does not have Heart Disease"
        
    elif disease_type == 'diabetes':
        features = [
            float(request.form.get('age1')),
            float(request.form.get('gender1')),
            float(request.form.get('bmi')),
            float(request.form.get('blood_pressure')),
            float(request.form.get('fbs')),
            float(request.form.get('hba1c')),
            float(request.form.get('family_history')),
            float(request.form.get('smoking')),
            float(request.form.get('diet')),
            float(request.form.get('exercise'))
        ]
        input_data = np.array([features])
        prediction = diabetes_model.predict(input_data)
        result_message = "The person has Diabetes" if int(prediction[0]) == 1 else "The person does not have Diabetes"

    elif disease_type == 'dengue':
        features = [
            float(request.form.get('fever')),
            float(request.form.get('headache')),
            float(request.form.get('muscle_pain')),
            float(request.form.get('vomiting')),
            float(request.form.get('skin_rash')),
            float(request.form.get('bleeding')),
            float(request.form.get('low_platelet_count')),
            float(request.form.get('joint_pain'))
        ]
        input_data = np.array([features])
        prediction = dengue_model.predict(input_data)
        result_message = "The person has Dengue" if int(prediction[0]) == 1 else "The person does not have Dengue"

    else:
        result_message = "Invalid disease type selected."

    # Render the same page with the prediction result
    return render_template('health.html', result=result_message, disease_type=disease_type)
@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/diet-chart', methods=['POST'])
def diet_chart():
    data = {
        'gender': request.form['gender'],
        'height': int(request.form['height']),
        'weight': int(request.form['weight']),
        'age': int(request.form['age']),
        'diet': request.form['diet'],
        'goal': request.form['goal']
    }

    # Basic logic (can be replaced by ML model or DB)
    if data['goal'] == 'Gain Weight' and data['diet'] == 'Non-Veg':
        meals = ["Fish (like salmon, mackerel, sardines)","Chicken thighs / drumsticks ","Eggs and Prawns / Shrimp ","Red meat (mutton)","Banana Shake", "Paneer Sandwich", "Rice & Dal", "Nuts"]
    elif data['goal'] == 'Gain Weight' and data['diet'] == 'Veg':
        meals = ["Paneer Tikka", "Chickpea Salad", "Vegetable Biryani", "Peanut Butter Toast", "Banana Shake", "Oats with Milk", "Rice & Dal", "Nuts"]
    elif data['goal'] == 'Lose Weight' and data['diet'] == 'Non-Veg':
        meals = ["Oats", "Boiled Eggs", "Salad", "Skinless chicken breast (grilled/boiled)","Eggs (boiled or poached)","Grilled Tofu"]
    elif data['goal'] == 'Lose Weight' and data['diet'] == 'Veg':
        meals = ["Oats", "Salad", "Grilled Tofu"," Greek yogurt", "lentils", "beans", "chickpeas", "sprouts", "quinoa"]
    else:
        meals = ["Roti & Sabzi", "Curd Rice", "Fruit Bowl"]

    return render_template("diet-chart.html", data=data, meals=meals)


if __name__ == '__main__':
    app.run(debug=True)