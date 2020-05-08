# MRC Clima
Controlador-Modelo-Tabla

## Recoge el diccionario y lo procesa para buscar el fk del aeropuerto antes de insertarlo en la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/clima/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":19,"idaeropuerto":1,"fecha":"est","hora":"fugiat","prevision":5536378.58474,"temperatura":125222.8,"lluvia":40513.2,"nubes":9533.6,"viento":6,"rafagas":4899949.0764784,"direccion":5211397.1,"humedad":323168.85,"presion":9997.0072}'

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
    "id": 19,
    "idaeropuerto": 1,
    "fecha": "est",
    "hora": "fugiat",
    "prevision": 5536378.58474,
    "temperatura": 125222.8,
    "lluvia": 40513.2,
    "nubes": 9533.6,
    "viento": 6,
    "rafagas": 4899949.0764784,
    "direccion": 5211397.1,
    "humedad": 323168.85,
    "presion": 9997.0072
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



