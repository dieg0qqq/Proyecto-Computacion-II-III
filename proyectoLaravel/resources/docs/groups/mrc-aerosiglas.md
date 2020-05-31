# MRC Aerosiglas
Controlador-Modelo-Tabla

## Recoge el diccionario y crea entradas para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/siglas/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":7,"name":"qui","acronym":"libero"}'

```

```javascript
const url = new URL(
    "http://localhost/api/siglas/datos"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 7,
    "name": "qui",
    "acronym": "libero"
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
    "nombre": "Aeropuerto de Madrid Barajas",
    "siglas": "MAD",
    "updated_at": "2020-05-08",
    "created_at": "2020-05-08",
    "id": 37
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/siglas/datos`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id de la sigla.
</p>
<p>
    <code><b>name</b></code>&nbsp; <small>string</small>     <br>
    El nombre del aeropuerto de la sigla.
</p>
<p>
    <code><b>acronym</b></code>&nbsp; <small>string</small>     <br>
    El conjunto de siglas que define el aeropuerto/región.
</p>


## Devuelve la lista de aeropuertos junto con sus siglas



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/siglas/lista" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/siglas/lista"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

fetch(url, {
    method: "GET",
    headers: headers,
})
    .then(response => response.json())
    .then(json => console.log(json));
```


> Example response (500):

```json
{
    "message": "Server Error"
}
```

### Request
<small class="badge badge-green">GET</small>
 **`api/siglas/lista`**




