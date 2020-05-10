# MRC Aerosiglas
Controlador-Modelo-Tabla

## Recoge el diccionario y crea entradas para la bbdd



> Example request:

```bash
curl -X POST \
    "http://localhost/api/siglas/datos" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"id":19,"name":"officiis","acronym":"minus"}'

```

```javascript
const url = new URL(
    "http://localhost/api/siglas/datos"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "id": 19,
    "name": "officiis",
    "acronym": "minus"
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
    "nombre": "Aeropuerto de Madrid Barajas",
    "siglas": "MAD",
    "updated_at": "2020-05-08T19:16:27.000000Z",
    "created_at": "2020-05-08T19:16:27.000000Z",
    "id": 37
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/siglas/datos`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>id</b></code>&nbsp; <small>integer</small>     <br>
    El id de la sigla.
</p>
<p>
    <code><b>name</b></code>&nbsp; <small>string</small>     <br>
    El nombre del aeropuerto de la sigla.
</p>
<p>
    <code><b>acronym</b></code>&nbsp; <small>string</small>     <br>
    El conjunto de siglas que define el aeropuerto/región.
</p>


## Devuelve la lista de aeropuertos junto con sus siglas



> Example request:

```bash
curl -X GET \
    -G "http://localhost/api/siglas/lista" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/siglas/lista"
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


> Example response (200):

```json
[
    {
        "id": 1,
        "created_at": "2020-05-08T21:49:43.000000Z",
        "updated_at": "2020-05-08T21:49:43.000000Z",
        "nombre": "Aeropuerto de Madrid Barajas",
        "siglas": "MAD"
    },
    {
        "id": 2,
        "created_at": "2020-05-08T21:49:43.000000Z",
        "updated_at": "2020-05-08T21:49:43.000000Z",
        "nombre": "Aeropuerto de Barcelona El Prat",
        "siglas": "BCN"
    },
    {
        "id": 3,
        "created_at": "2020-05-08T21:49:43.000000Z",
        "updated_at": "2020-05-08T21:49:43.000000Z",
        "nombre": "Aeropuerto de Bilbao",
        "siglas": "BIO"
    },
    {
        "id": 4,
        "created_at": "2020-05-08T21:49:43.000000Z",
        "updated_at": "2020-05-08T21:49:43.000000Z",
        "nombre": "Aeropuerto de Ibiza",
        "siglas": "IBZ"
    },
    {
        "id": 5,
        "created_at": "2020-05-08T21:49:43.000000Z",
        "updated_at": "2020-05-08T21:49:43.000000Z",
        "nombre": "Aeropuerto de Santiago de Compostela",
        "siglas": "SCQ"
    },
    {
        "id": 6,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de La Coruña",
        "siglas": "LCG"
    },
    {
        "id": 7,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Santander",
        "siglas": "SDR"
    },
    {
        "id": 8,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Málaga",
        "siglas": "AGP"
    },
    {
        "id": 9,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Vigo",
        "siglas": "VGO"
    },
    {
        "id": 10,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Asturias",
        "siglas": "OVD"
    },
    {
        "id": 11,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Valencia",
        "siglas": "VLC"
    },
    {
        "id": 12,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Alicante",
        "siglas": "ALC"
    },
    {
        "id": 13,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Palma de Mallorca",
        "siglas": "PMI"
    },
    {
        "id": 14,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Zaragoza",
        "siglas": "ZAZ"
    },
    {
        "id": 15,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Gran Canaria",
        "siglas": "LPA"
    },
    {
        "id": 16,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Sevilla",
        "siglas": "SVQ"
    },
    {
        "id": 17,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Granada",
        "siglas": "GRX"
    },
    {
        "id": 18,
        "created_at": "2020-05-08T21:49:44.000000Z",
        "updated_at": "2020-05-08T21:49:44.000000Z",
        "nombre": "Aeropuerto de Tenerife Sur",
        "siglas": "TFS"
    },
    {
        "id": 19,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Girona-Costa Brava",
        "siglas": "GRO"
    },
    {
        "id": 20,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Tenerife Norte",
        "siglas": "TFN"
    },
    {
        "id": 21,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Lanzarote",
        "siglas": "ACE"
    },
    {
        "id": 22,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Jerez",
        "siglas": "XRY"
    },
    {
        "id": 23,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Valladolid",
        "siglas": "VLL"
    },
    {
        "id": 24,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Menorca",
        "siglas": "MAH"
    },
    {
        "id": 25,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Almería",
        "siglas": "LEI"
    },
    {
        "id": 26,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Pamplona",
        "siglas": "PNA"
    },
    {
        "id": 27,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de León",
        "siglas": "LEN"
    },
    {
        "id": 28,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Fuerteventura",
        "siglas": "FUE"
    },
    {
        "id": 29,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Melilla",
        "siglas": "MLN"
    },
    {
        "id": 30,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Reus",
        "siglas": "REU"
    },
    {
        "id": 31,
        "created_at": "2020-05-08T21:49:45.000000Z",
        "updated_at": "2020-05-08T21:49:45.000000Z",
        "nombre": "Aeropuerto de Murcia",
        "siglas": "RMU"
    },
    {
        "id": 32,
        "created_at": "2020-05-08T21:49:46.000000Z",
        "updated_at": "2020-05-08T21:49:46.000000Z",
        "nombre": "Aeropuerto de San Sebastián",
        "siglas": "EAS"
    },
    {
        "id": 33,
        "created_at": "2020-05-08T21:49:46.000000Z",
        "updated_at": "2020-05-08T21:49:46.000000Z",
        "nombre": "Aeropuerto de La Palma",
        "siglas": "SPC"
    },
    {
        "id": 34,
        "created_at": "2020-05-08T21:49:46.000000Z",
        "updated_at": "2020-05-08T21:49:46.000000Z",
        "nombre": "Aeropuerto de Lleida",
        "siglas": "ILD"
    },
    {
        "id": 35,
        "created_at": "2020-05-08T21:49:46.000000Z",
        "updated_at": "2020-05-08T21:49:46.000000Z",
        "nombre": "Aeropuerto de Huesca-Pirineos",
        "siglas": "HSK"
    },
    {
        "id": 36,
        "created_at": "2020-05-08T21:49:46.000000Z",
        "updated_at": "2020-05-08T21:49:46.000000Z",
        "nombre": "Aeropuerto de El Hierro",
        "siglas": "VDE"
    }
]
```

### Request
<small class="badge badge-green">GET</small>
 **`api/siglas/lista`**




