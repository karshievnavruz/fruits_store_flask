from flask import Flask, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    fruits = db.all()
    html = '<html>'
    html += '<head><title>Fruit</title><style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style></head>'
    html += '<body>'
    html += '<h1>Fruits</h1>'
    html += '<table>'
    html += '<tr><th>name</th> <th>quantity</th> <th>price</th> <th>type</th></tr>'
    for fruit in fruits:
        html += f'<tr><th>{fruit["name"]}</th><th>{fruit["quantity"]}</th><th>{fruit["price"]}$</th><th>{fruit["type"]}</th></tr>'
    html += '</table>'
    html += '</body>'
    html += "</html>"
    return html


    fruits = db.add(fruit)
    return fruits


@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    pass


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    pass


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    pass


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    pass



if __name__ == '__main__':
    app.run(debug=True)