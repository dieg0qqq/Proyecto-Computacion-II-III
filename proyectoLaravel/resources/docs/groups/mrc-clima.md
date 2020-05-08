# MRC Clima
Controlador-Modelo-Tabla

## Recoge el diccionario y lo procesa para buscar el fk del aeropuerto antes de insertarlo en la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/clima/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/clima/datos"
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
    "id": 5,
    "idaeropuerto": "LCG\n",
    "fecha": "2020-05-08",
    "hora": "14:00",
    "prevision": "Patchy rain possible",
    "temperatura": "18",
    "lluvia": "0.1",
    "nubes": "38",
    "viento": "11",
    "rafagas": "13",
    "direccion": "NW",
    "humedad": "78",
    "presion": "1013"
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/clima/datos`**




