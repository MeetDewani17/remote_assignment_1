from flask import Flask, request, jsonify

 

app = Flask(__name__)

 


stocks = [

    {"name": "Meet Dewani",

     "ticker symbol": "MD",

     "price": 103.2,

    },

 

    {"name": "Akala Kamana",

     "ticker symbol": "AK",

     "price": 200.4,

    },

   

]

@app.route('/stocks', methods=['GET'])

def get_stocks():

    return jsonify(stocks)


@app.route('/stocks', methods=['POST'])

def add_stock():

    data = request.get_json()

 

    if 'name' not in data or 'ticker symbol' not in data or 'price' not in data:

        return jsonify({"error": "Incomplete data"})

 

    new_stock = {

        "name": data['name'],

        "ticker symbol": data['ticker symbol'],

        "price": data['price'],

       }

    stocks.append(new_stock)

 

    return jsonify({"message": "Stock added successfully"})

 


 

if __name__ == '__main__':

    app.run(debug=True)

 