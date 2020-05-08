# MRC Twitter


## Recoge el diccionario y crea un fila pra la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/comentarios/twitter" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":3,"nombreAerolinea":17,"comentario":"tempore","analisis":"eius"}'

```

```javascript
const url = new URL(
    "http://localhost/api/comentarios/twitter"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 3,
    "nombreAerolinea": 17,
    "comentario": "tempore",
    "analisis": "eius"
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
    "nombreAerolinea": "Iberia",
    "comentario": "Todo muy bien ha llegado a tiempo",
    "analisis": "Positivo"
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/comentarios/twitter`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id del tweet
</p>
<p>
    <code><b>nombreAerolinea</b></code>&nbsp; <small>integer</small>     <br>
    El id de la aerolínea asociada por FK.
</p>
<p>
    <code><b>comentario</b></code>&nbsp; <small>text</small>     <br>
    La información extraída del comentario.
</p>
<p>
    <code><b>analisis</b></code>&nbsp; <small>string</small>     <br>
    El resultado del análisis de sentimientos sobre el comentario.
</p>


## Display a listing of the resource.



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/twitter/opinionG" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/twitter/opinionG"
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



### Request
<small class="badge badge-green">GET</small>
 **`api/twitter/opinionG`**




