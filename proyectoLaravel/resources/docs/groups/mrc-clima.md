# MRC Clima
Controlador-Modelo-Tabla

## Devuelve todos los datos del clima de Weather-Airports



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/boton" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/boton"
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
 **`api/boton`**



## Recoge el diccionario y lo procesa para buscar el fk del aeropuerto antes de insertarlo en la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/clima/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":13,"idaeropuerto":11,"fecha":"numquam","hora":"aut","prevision":16937722.5062,"temperatura":971097.16188,"lluvia":31.86768131,"nubes":148321.805978,"viento":489.9867,"rafagas":2590674.3,"direccion":172.3,"humedad":7862027.3,"presion":530969}'

```

```javascript
const url = new URL(
    "http://localhost/api/clima/datos"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 13,
    "idaeropuerto": 11,
    "fecha": "numquam",
    "hora": "aut",
    "prevision": 16937722.5062,
    "temperatura": 971097.16188,
    "lluvia": 31.86768131,
    "nubes": 148321.805978,
    "viento": 489.9867,
    "rafagas": 2590674.3,
    "direccion": 172.3,
    "humedad": 7862027.3,
    "presion": 530969
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

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id del clima.
</p>
<p>
    <code><b>idaeropuerto</b></code>&nbsp; <small>integer</small>     <br>
    El id del aeropuerto asociado por FK.
</p>
<p>
    <code><b>fecha</b></code>&nbsp; <small>date</small>     <br>
    La fecha del día que se recogen los datos.
</p>
<p>
    <code><b>hora</b></code>&nbsp; <small>string</small>     <br>
    La hora y minutos del clima.
</p>
<p>
    <code><b>prevision</b></code>&nbsp; <small>float</small>     <br>
    Descripción del clima (nublado, soleado...).
</p>
<p>
    <code><b>temperatura</b></code>&nbsp; <small>float</small>     <br>
    La temperatura que había en °C.
</p>
<p>
    <code><b>lluvia</b></code>&nbsp; <small>float</small>     <br>
    La cantidad de lluvia en mm.
</p>
<p>
    <code><b>nubes</b></code>&nbsp; <small>float</small>     <br>
    El porcentaje de nubes que cubre el cielo.
</p>
<p>
    <code><b>viento</b></code>&nbsp; <small>float</small>     <br>
    La velocidad del viento en km/h.
</p>
<p>
    <code><b>rafagas</b></code>&nbsp; <small>float</small>     <br>
    La velocidad de las ráfagas en km/h.
</p>
<p>
    <code><b>direccion</b></code>&nbsp; <small>float</small>     <br>
    La dirección del viento en sistema cardinal.
</p>
<p>
    <code><b>humedad</b></code>&nbsp; <small>float</small>     <br>
    La cantidad de humedad en porcentaje.
</p>
<p>
    <code><b>presion</b></code>&nbsp; <small>float</small>     <br>
    La cantidad de presión en milibars (mb).
</p>


## Display a listing of the resource.



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/clima/lista" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/clima/lista"
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
 **`api/clima/lista`**



## Muestra la lista de climas en un específico aeropuerto



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/climaXaeropuerto/1/1" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/climaXaeropuerto/1/1"
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
 **`api/climaXaeropuerto/{id}/{fecha}`**




