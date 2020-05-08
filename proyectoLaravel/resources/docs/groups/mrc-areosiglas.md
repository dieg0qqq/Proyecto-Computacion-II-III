# MRC Areosiglas
Controlador-Modelo-Tabla

## Recoge el diccionario y crea entradas para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/siglas/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/siglas/datos"
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
 **`api/siglas/datos`**




