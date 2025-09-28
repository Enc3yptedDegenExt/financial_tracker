from flask import Flask, render_template, request
from sample_data import get_city_tier_benchmark

app = Flask(__name__)

@app.route('/')
def user_details():
    return render_template('user_details.html')

@app.route('/financial-input', methods=['POST'])
def financial_input():
    user_info = request.form
    return render_template('financial_input.html', user=user_info)

@app.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.form
    income = float(data.get('income', 0))
    expenses = sum([
        float(data.get('housing', 0)),
        float(data.get('food', 0)),
        float(data.get('shopping', 0)),
        float(data.get('groceries', 0)),
        float(data.get('transport', 0)),
        float(data.get('entertainment', 0)),
        float(data.get('medical', 0)),
        float(data.get('home_loan', 0)),
        float(data.get('house_loan', 0)),
        float(data.get('car_loan', 0))
    ])
    investments = float(data.get('sip', 0)) + float(data.get('stocks', 0))
    ratio = round((expenses / income) * 100, 2) if income else 0
    tier = data.get('tier')
    benchmark = get_city_tier_benchmark(tier)

    if ratio < benchmark['healthy']:
        status = "Healthy"
        advice = "Your financial health looks good. Keep investing wisely!"
    elif ratio < benchmark['moderate']:
        status = "Moderate Risk"
        advice = "Consider reducing discretionary expenses like entertainment and shopping."
    else:
        status = "High Risk"
        advice = "Your expenses are high for your city tier. Reevaluate your budget."

    return {
        "income": income,
        "expenses": expenses,
        "investments": investments,
        "ratio": ratio,
        "status": status,
        "advice": advice
    }

if __name__ == '__main__':
app.run(debug=True)
