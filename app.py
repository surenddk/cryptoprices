import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Function to fetch live cryptocurrency prices
def fetch_crypto_prices():
    # Get top 10 coins by market cap from CoinGecko
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Return a dict with coin name as key and price as value
        return {coin['name']: {'usd': coin['current_price']} for coin in data}
    else:
        return {"error": "Error fetching prices"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/prices')
def get_prices():
    return jsonify(fetch_crypto_prices())

if __name__ == '__main__':
    app.run(debug=True)