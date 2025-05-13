# imports
from flask import Flask
from flask_graphql import GraphQLView
import graphene



# products data
products_data = [
    {'id': 1, 'name' : 'Caran D`Ache Neocolor - Tonos Fríos', 'price' : 21.05, 'stock' : 5, 'availeability' : True},
    {'id': 2, 'name' : 'Caran D`Ache Neocolor - Tonos Cálidos', 'price' : 21.05, 'stock' : 5, 'availeability' : True},
    {'id': 3, 'name' : 'Silver Bristol Pincel Redondo', 'price' : 9.20, 'stock' : 15, 'availeability' : True},
    {'id': 4, 'name' : 'Etchr The Perfect Sketchbook 300G', 'price' : 35.33, 'stock' : 6, 'availeability' : True},
    {'id': 5, 'name' : 'Rembrandt Caja Óleo Master 24 Tubos', 'price' : 330.00, 'stock' : 8, 'availeability' : True}
]

# models
class Product(graphene.ObjectType):
    id = graphene.Int(required = True)
    name = graphene.String(required = True)
    price = graphene.Float(required = True)
    stock = graphene.Int()
    availeability = graphene.Boolean()

# query
class Query(graphene.ObjectType):
    products = graphene.List(Product)

    def return_products(self, info):
        return products_data
       
# app initialization
app = Flask(__name__)

# configs
app.add_url_rule('/graphql', view_func = GraphQLView.as_view('graphql', schema = schema, graphiql = True))

if __name__ == '__main__':
    app.run(debug = True)


