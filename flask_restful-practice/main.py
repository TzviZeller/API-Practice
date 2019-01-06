from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

order_num = 2
orders = [
    {
        "order_num": "1",
        "name": "Ben the SWE",
        "topings": "Peperoni, Bacon, Pinaple",
        "delivery": "NOW!"
    },
    {
        "order_num": "2",
        "name": "Tzvi the TSC",
        "topings": "Motzerela, Sundried Tomatoes, Garlic",
        "delivery": "Later?"
        }
]

class Order(Resource):
    """Class for querying pizza orders."""

    def get(self,order_num):
        """Gets customer's order by order_num
        Args:
            order_num: UUID for orders
        Return:
            Will return customers order or 404 error if cant be found
        """
        for order in orders:
            if(order_num == order["order_num"]):
                return order, 200
        return "Order Not Found", 404

    def post(self):
        #TODO:implement 400 for bad request
        """Places customer's order
        Return:
            Will return order_num
        """
        order_num += 1
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("topings")
        parser.add_argument("delivery")
        args = parser.parse_args()

        order = {
        "order_num": order_num,
        "name": args["name"],
        "topings": args["topings"],
        "delivery": args["delivery"]
        }

        orders.append(order)
        return order_num, 201

    def delete(self, order_num):
        global orders
        orders = [order for order in orders if orders["order_num"] != order_num]
        return "order is deleted", 200

api.add_resource(Order,"/order/<string:order_num>")

#TODO: this is for testig disable
app.run(debug=True, host='0.0.0.0')
