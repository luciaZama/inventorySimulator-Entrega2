## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
Las principales ventajas de GraphQL frente a REST son las siguientes:
- El cliente pide exactamente lo que necesita.
- Puede hacer varias consultas o mutaciones en una sola llamada HTTP.
- Tiene un esquema fuertemente tipado, que facilita el desarrollo y la validación de datos.
- Funciona bien para interfaces dinámicas que dependen de actualizaciones reactivas.

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
Los tipos en GraphQL se definen de la siguiente forma:
```python
type Person {
    id: ID!
    name: String!
    age: Int!
}
```
Por otro lado, los resolvers se definen de esta manera:
```python
const resolvers = {
    Query: {
        getUser(parent, args, context, info) {
            return {
                &quot;id&quot;: &quot;1&quot;,
                &quot;name: &quot;GFG
            }
        }
    }
}
```

Si por el contrario estuvieramos utilizando graphene, como es el caso en este backend, los tipos y resolvers se definirían de la siguiente manera:
```python
# tipo
class Person(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    age = graphene.Int(required=True)

# resolver
class Query(graphene.ObjectType):
    get_user = graphene.Field(Person)

    def resolve_get_user(self, info):
        return Person(id="1", name="GFG", age=30)
```

## ¿Por qué es importante que el backend también actualize disponible y no depender solo del frontend?
Es importante que el backend también actualice el campo disponible (o availability) porque la lógica de negocio no debe depender exclusivamente del frontend. Si solo el frontend actualiza la disponibilidad, existe el riesgo de inconsistencias en los datos cuando otros clientes, servicios o aplicaciones accedan al backend. Centralizar esta lógica garantiza que las reglas de negocio se apliquen de forma uniforme y confiable, sin importar desde dónde se realice la petición.

## ¿Cómo garantizas que la lógica de actualización del stock y disponibilidad sea coherente?
Para garantizar que la lógica de actualización del stock y la disponibilidad sea coherente, se implementa directamente en la mutación del backend. Cada vez que se modifica el stock, se evalúa su nuevo valor: si es cero o menor, la disponibilidad se pone en false; si el stock vuelve a ser mayor que cero, la disponibilidad cambia a true. Esto asegura que no pueda haber un producto con stock cero marcado como disponible, y viceversa, manteniendo la integridad del sistema.