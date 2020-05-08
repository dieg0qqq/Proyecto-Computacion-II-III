# MRC Vuelos
Recoge el diccionario y crea un fila para la bbdd

## [Se busca la aerolinea en su tabla y si no se encuentra se crea una entrada, además se busca la sigla del aeropuerto de origen]



> Example request:

```bash
curl -X POST \
    "http://localhost/api/vuelos/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/vuelos/datos"
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




