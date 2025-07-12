from flask import Flask, render_template, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stock')
def get_stock():
    symbol = request.args.get('symbol', 'AAPL')
    # Para ações brasileiras, use o .SA no final, ex: PETR4.SA, VALE3.SA
    data = yf.Ticker(symbol).history(period="1d", interval="5m")
    if data.empty:
        return jsonify({'error': 'Dados não encontrados'})
    chart_data = [
        {'time': idx.strftime('%H:%M'), 'price': row['Close']}
        for idx, row in data.iterrows()
    ]
    return jsonify({'data': chart_data})

if __name__ == '__main__':
    app.run(debug=True)