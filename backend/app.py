# imports
from flask import Flask
from flask_graphql import GraphQLView
import graphene



# products list
products_data = [
    {'id': 1, 'name' : 'Caran D`Ache Neocolor - Tonos Fríos', 'price' : 21.05, 'stock' : 5, 'availability' : True},
    {'id': 2, 'name' : 'Caran D`Ache Neocolor - Tonos Cálidos', 'price' : 21.05, 'stock' : 5, 'availability' : True},
    {'id': 3, 'name' : 'Silver Bristol Pincel Redondo', 'price' : 9.20, 'stock' : 15, 'availability' : True},
    {'id': 4, 'name' : 'Etchr The Perfect Sketchbook 300G', 'price' : 35.33, 'stock' : 6, 'availability' : True},
    {'id': 5, 'name' : 'Rembrandt Caja Óleo Master 24 Tubos', 'price' : 330.00, 'stock' : 8, 'availability' : True}
]

# models
class Product(graphene.ObjectType):
    id = graphene.Int(required = True)
    name = graphene.String(required = True)
    price = graphene.Float(required = True)
    stock = graphene.Int()
    availability = graphene.Boolean()

# query
class Query(graphene.ObjectType):
    products = graphene.List(Product)

    def resolve_products(self, info):
        return [Product(**p) for p in products_data]

    
# mutations
class ModifyStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        amount = graphene.Int()

    product = graphene.Field(lambda: Product)
    def mutate(root, info, id, amount):
        for p in products_data:
            if p['id'] == id:
                p['stock'] += amount

                if p['stock'] <= 0:
                    p['stock'] = 0
                    p['availability'] = False
                else:
                    p['availability'] = True

                return ModifyStock(product = Product(**p))
        raise Exception ('Producto no encontrado')
                    
class Mutation(graphene.ObjectType):
    modify_stock = ModifyStock.Field()

       
# app initialization
app = Flask(__name__)
schema = graphene.Schema(query=Query, mutation = Mutation)

# configs
app.add_url_rule('/graphql', view_func = GraphQLView.as_view('graphql', schema = schema, graphiql = True))

if __name__ == '__main__':
    app.run(debug = True)


