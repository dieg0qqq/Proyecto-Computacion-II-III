# MRC Vuelos
Recoge el diccionario y crea un fila para la bbdd

## [Se busca la aerolinea en su tabla y si no se encuentra se crea una entrada, además se busca la sigla del aeropuerto de origen]



> Example request:

```bash
curl -X POST \
    "http://localhost/api/vuelos/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":13,"IdVuelo":"aut","Aerolinea":2,"Estado1":"qui","Estado2":"porro","SiglasOrigen":7,"Origen":"placeat","HoraProgOrigen":"laborum","HoraEstOrigen":"cum","TerminalOrigen":"labore","GateOrigen":"officiis","SiglasDestino":"quo","Destino":"velit","HoraProgDestino":"ut","HoraEstDestino":"quidem","TerminalDestino":"sed","GateDestino":"culpa"}'

```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/datos"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 13,
    "IdVuelo": "aut",
    "Aerolinea": 2,
    "Estado1": "qui",
    "Estado2": "porro",
    "SiglasOrigen": 7,
    "Origen": "placeat",
    "HoraProgOrigen": "laborum",
    "HoraEstOrigen": "cum",
    "TerminalOrigen": "labore",
    "GateOrigen": "officiis",
    "SiglasDestino": "quo",
    "Destino": "velit",
    "HoraProgDestino": "ut",
    "HoraEstDestino": "quidem",
    "TerminalDestino": "sed",
    "GateDestino": "culpa"
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
    "IdVuelo": "SWT 112",
    "Aerolinea": "Swiftair",
    "Estado1": "Unknown",
    "Estado2": "",
    "SiglasOrigen": "BCN",
    "Origen": "Barcelona",
    "HoraProgOrigen": "04:30 CEST",
    "HoraEstOrigen": "-- ",
    "TerminalOrigen": "N\/A",
    "GateOrigen": "N\/A",
    "SiglasDestino": "PMI",
    "Destino": "Palma Mallorca",
    "HoraProgDestino": "05:30 CEST",
    "HoraEstDestino": "-- ",
    "TerminalDestino": "N\/A",
    "GateDestino": "N\/A"
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/vuelos/datos`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id del vuelo en base de datos.
</p>
<p>
    <code><b>IdVuelo</b></code>&nbsp; <small>string</small>     <br>
    El identificador del vuelo.
</p>
<p>
    <code><b>Aerolinea</b></code>&nbsp; <small>integer</small>     <br>
    El id de la aerolínea asociada por FK.
</p>
<p>
    <code><b>Estado1</b></code>&nbsp; <small>string</small>     <br>
    El estado del vuelo.
</p>
<p>
    <code><b>Estado2</b></code>&nbsp; <small>string</small>     <br>
    El subestado del vuelo.
</p>
<p>
    <code><b>SiglasOrigen</b></code>&nbsp; <small>integer</small>     <br>
    El id del aeropuerto asociado por FK.
</p>
<p>
    <code><b>Origen</b></code>&nbsp; <small>string</small>     <br>
    De donde sale el vuelo.
</p>
<p>
    <code><b>HoraProgOrigen</b></code>&nbsp; <small>string</small>     <br>
    La hora programada de salida.
</p>
<p>
    <code><b>HoraEstOrigen</b></code>&nbsp; <small>string</small>     <br>
    La hora real de salida.
</p>
<p>
    <code><b>TerminalOrigen</b></code>&nbsp; <small>string</small>     <br>
    El terminal asociado al vuelo a la salida.
</p>
<p>
    <code><b>GateOrigen</b></code>&nbsp; <small>string</small>     <br>
    La puerta de embarque del vuelo a la salida.
</p>
<p>
    <code><b>SiglasDestino</b></code>&nbsp; <small>string</small>     <br>
    Las siglas del destino.
</p>
<p>
    <code><b>Destino</b></code>&nbsp; <small>string</small>     <br>
    El nombre del destino.
</p>
<p>
    <code><b>HoraProgDestino</b></code>&nbsp; <small>string</small>     <br>
    La hora programada de llegada.
</p>
<p>
    <code><b>HoraEstDestino</b></code>&nbsp; <small>string</small>     <br>
    La hora real de llegada.
</p>
<p>
    <code><b>TerminalDestino</b></code>&nbsp; <small>string</small>     <br>
    El terminal asociado al vuelo a la llegada.
</p>
<p>
    <code><b>GateDestino</b></code>&nbsp; <small>string</small>     <br>
    La puerta de embarque del vuelo a la llegada.
</p>


## Muestra la lista de vuelos en un específico aeropuerto



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelosXaeropuerto/1/1" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelosXaeropuerto/1/1"
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
 **`api/vuelosXaeropuerto/{id}/{fecha}`**



## Muestra los detalles del vuelo



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelo/1/1" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelo/1/1"
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
 **`api/vuelo/{id}/{fecha}`**



## Devuelve todos los vuelos que hayan en la BBDD



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/listaVuelos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/listaVuelos"
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
 **`api/listaVuelos`**



## Cantidad de vuelos totales en la base de datos



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelos/contador" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/contador"
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
 **`api/vuelos/contador`**



## Cantidad de vuelos por dia



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelos/contadorDia" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/contadorDia"
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
 **`api/vuelos/contadorDia`**



## Numero de vuelos por Aeropuerto



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelos/contadorAeropuerto" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/contadorAeropuerto"
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
 **`api/vuelos/contadorAeropuerto`**



## Numero de vuelos por Aerolinea



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/vuelos/contadorAerolineasVuelos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/contadorAerolineasVuelos"
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
 **`api/vuelos/contadorAerolineasVuelos`**



## Devuelve los vuelos con sus climas juntandolos por los dos primeros digitos de la hora siempre que no sean los vuelos de hoy ni que su estado sea ni cancelado o desconocido



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/prediccion" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/prediccion"
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
 **`api/prediccion`**



## Devuelve los vuelos con sus climas juntandolos por los dos primeros digitos de la hora que sean de la fecha actual



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/clasificador" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/clasificador"
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
 **`api/clasificador`**




