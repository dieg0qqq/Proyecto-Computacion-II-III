# MRC Vuelos
Recoge el diccionario y crea un fila para la bbdd

## [Se busca la aerolinea en su tabla y si no se encuentra se crea una entrada, además se busca la sigla del aeropuerto de origen]



> Example request:

```bash
curl -X POST \
    "http://localhost/api/vuelos/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":9,"IdVuelo":"natus","Aerolinea":3,"Estado1":"voluptas","Estado2":"commodi","SiglasOrigen":10,"Origen":"ducimus","HoraProgOrigen":"similique","HoraEstOrigen":"vel","TerminalOrigen":"temporibus","GateOrigen":"incidunt","SiglasDestino":"beatae","Destino":"dicta","HoraProgDestino":"voluptatem","HoraEstDestino":"eos","TerminalDestino":"enim","GateDestino":"nihil"}'

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
    "id": 9,
    "IdVuelo": "natus",
    "Aerolinea": 3,
    "Estado1": "voluptas",
    "Estado2": "commodi",
    "SiglasOrigen": 10,
    "Origen": "ducimus",
    "HoraProgOrigen": "similique",
    "HoraEstOrigen": "vel",
    "TerminalOrigen": "temporibus",
    "GateOrigen": "incidunt",
    "SiglasDestino": "beatae",
    "Destino": "dicta",
    "HoraProgDestino": "voluptatem",
    "HoraEstDestino": "eos",
    "TerminalDestino": "enim",
    "GateDestino": "nihil"
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



