from flask import Flask, render_template, request

app = Flask(__name__)

user_balance = 1000  # Initial balance

@app.route('/')
def index():
    return render_template('index.html', balance=user_balance)

@app.route('/transfer', methods=['GET'])
def transfer():
    global user_balance
    recipient = request.args.get('recipient')
    amount = request.args.get('amount')

    # Validate and process the transfer
    try:
        amount = float(amount)
        if amount <= 0 or amount > user_balance:
            raise ValueError("Invalid amount")
        user_balance -= amount
    except ValueError:
        return "Invalid transfer amount", 400

    return render_template('transfer.html', recipient=recipient, amount=amount)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
