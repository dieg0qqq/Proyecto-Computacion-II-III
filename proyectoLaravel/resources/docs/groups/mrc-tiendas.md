# MRC Tiendas
Controlador-Modelo-Tabla

## Recoge el diccionario y crea las filas para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/tienda/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":10,"tienda":"quibusdam","direccion":10}'

```

```javascript
const url = new URL(
    "http://localhost/api/tienda/datos"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 10,
    "tienda": "quibusdam",
    "direccion": 10
}

fetch(url, {
    method: "POST",
    headers: headers,
    body: body
})
    .then(response => response.json())
    .then(json => console.log(json));
```


> Example response (200):

```json
{
    "nombre_tienda": "Accessorize",
    "direccion": "Terminal T3. Planta 1. Salidas. Zona de embarque E",
    "updated_at": "2020-05-08T19:19:03.000000Z",
    "created_at": "2020-05-08T19:19:03.000000Z",
    "id": 137
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/tienda/datos`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id de la tienda.
</p>
<p>
    <code><b>tienda</b></code>&nbsp; <small>string</small>     <br>
    El nombre de la tienda.
</p>
<p>
    <code><b>direccion</b></code>&nbsp; <small>integer</small>     <br>
    La dirección donde se encuentra la tienda.
</p>



