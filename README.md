
# Instrucciones para ejecutar y probar la API GraphQL con Flask y Graphene

Este proyecto contiene una API creada con Flask y Graphene para gestionar productos y sus stocks. A continuación se detallan todos los pasos necesarios para ejecutar la aplicación desde cero utilizando un entorno virtual llamado `flaskenv`.

##  1. Crear y activar entorno virtual

Si aún no hay un entorno virtual creado, se puede hacer con:

```bash
python -m venv flaskenv
```

Luego, actívalo:

### En Linux/macOS:
```bash
source flaskenv/bin/activate
```

### En Windows (CMD):
```cmd
flaskenv\Scripts\activate
```

### En Windows (PowerShell):
```powershell
.\flaskenv\Scripts\Activate.ps1
```

## 2. Instalar dependencias necesarias

Instala Flask, Graphene y Flask-GraphQL ejecutando:

```bash
pip install flask graphene flask-graphql
```

## 3. Ejecutar la aplicación
```bash
python app.py
```
Aparecerá un mensaje similar a este:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## 4. Acceder al explorador GraphQL

Abre el navegador y visita:
```
http://127.0.0.1:5000/graphql
```
Esto cargará GraphiQL, una interfaz visual para enviar consultas y mutaciones a la API.

## 5. Probar consultas y mutaciones

### Consulta para obtener todos los productos

```graphql
query {
  products {
    id
    name
    price
    stock
    availability
  }
}
```

### Mutación para modificar el stock de un producto

```graphql
mutation {
  modifyStock(id: 1, amount: -5) {
    product {
      id
      name
      stock
      availability
    }
  }
}
```

Se puede probar diferentes combinaciones de `id` y `amount` para observar cómo cambian los datos en tiempo real.

## 6. Finalizar la sesión

Se puede desactivar el entorno virtual con:
```bash
deactivate
```
