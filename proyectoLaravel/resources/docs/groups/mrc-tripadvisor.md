# MRC TripAdvisor


## Se recoge el diccionario, se busca el FK del nombre de aerolinea para coger su id y se crea una fila para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/tripadvisor/comentarios" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/tripadvisor/comentarios"
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



### Request
<small class="badge badge-black">POST</small>
 **`api/tripadvisor/comentarios`**




