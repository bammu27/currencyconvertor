import requests
from flask import Flask, render_template, request

app = Flask(__name__)

api_key = 'fca_live_tnBXF1af2dWhyloxg7SELEiObmwRfNO0MAdSTDWM'
base_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"

currencies = ['USD', 'EUR', 'INR', 'JPY', 'CNY', 'RUB']


def current_currency(from_curr):
    curr = ",".join(currencies)
    url = f"{base_url}&base_currency={from_curr}&currencies={curr}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except Exception as e:
        print(e)


@app.route('/', methods=['GET', 'POST'])
def currency():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_curr = request.form['from_currency']
        to_curr = request.form['to_currency']

        conversion_data = current_currency(from_curr)
        converted_amount = conversion_data[to_curr] * amount
        return render_template('index.html', curr=converted_amount,to_curr=to_curr,from_curr=from_curr,amount=amount)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
