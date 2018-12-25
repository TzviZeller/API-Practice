from flask import flask
from flask_restfull import Api, Resource,

app = Flask(__name__)
api = Api(app)

order_num = 00003
orders = [
    {
        "order_num": "0001",
        "name": "Ben the SWE",
        "topings": "Peperoni, Bacon, Pinaple",
        "Delivery": "NOW!"
    },
    {
        "order_num": "0002",
        "name": "Tzvi the TSC",
        "topings": "Motzerela, Sundried Tomatoes, Garlic",
        "Delivery": "Later?"
        }
]

class orders(PizzaOrders):
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

    def post(self, order_num):
        """Places customer's order by order_num
        Args:
            order_num: UUID for orders
        Return:
            Will return customers order or 404 error if cant be found
        """
    def put(self, order_num):
    def delete(self, order_num):
