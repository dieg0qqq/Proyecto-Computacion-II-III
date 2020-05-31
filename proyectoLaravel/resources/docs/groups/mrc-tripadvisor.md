# MRC TripAdvisor


## Se recoge el diccionario, se busca el FK del nombre de aerolinea para coger su id y se crea una fila para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/tripadvisor/comentarios" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":11,"id_aerolinea":19,"cuerpo":"debitis","valoracion":7949.41527}'

```

```javascript
const url = new URL(
    "http://localhost/api/tripadvisor/comentarios"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 11,
    "id_aerolinea": 19,
    "cuerpo": "debitis",
    "valoracion": 7949.41527
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
    "IdAerolinea": 24,
    "Comentario": "CORRECTA Y PROFESIONAL Espacio adecuado , el personal atento y agradable . La comida correcta, la limpieza buena . Los labavos limpios y suficientes",
    "Valoracion": "4",
    "updated_at": "2020-05-08T18:48:05.000000Z",
    "created_at": "2020-05-08T18:48:05.000000Z",
    "id": 856
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/tripadvisor/comentarios`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id del comentario.
</p>
<p>
    <code><b>id_aerolinea</b></code>&nbsp; <small>integer</small>     <br>
    El id del aeropuerto asociado por FK.
</p>
<p>
    <code><b>cuerpo</b></code>&nbsp; <small>string</small>     <br>
    La información que contiene el cuerpo (comentario).
</p>
<p>
    <code><b>valoracion</b></code>&nbsp; <small>float</small>     <br>
    La valoración de 1 a 5 sobre la aerolínea.
</p>


## Devuelve todos los comentarios que se tengan en la BBDD



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/tripadvisor/lista" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/tripadvisor/lista"
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
 **`api/tripadvisor/lista`**



## Devuelve los comentarios de un aeropuerto en especifico



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/tripadvisorXaerolinea/1" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/tripadvisorXaerolinea/1"
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
 **`api/tripadvisorXaerolinea/{id}`**




