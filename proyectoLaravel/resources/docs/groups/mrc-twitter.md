# MRC Twitter


## Recoge el diccionario y crea un fila pra la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/comentarios/twitter" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/comentarios/twitter"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

fetch(url, {
    method: "POST",
    headers: headers,
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




