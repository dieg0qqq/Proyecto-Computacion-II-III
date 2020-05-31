# MRC User
Controlador-Modelo-Tabla

## Hace una verificación sobre el email y la contraseña, que lo compara contra los datos del usuario y si es exitoso, crea un token y pasa al estado de success.



> Example request:

```bash
curl -X POST \
    "http://localhost/api/login" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"email":"temporibus","password":"aliquam"}'

```

```javascript
const url = new URL(
    "http://localhost/api/login"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "email": "temporibus",
    "password": "aliquam"
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
    "email": "dfraj.aznarez@gmail.com",
    "password": "12345"
}
```

### Request
<small class="badge badge-black">POST</small>
 **`api/login`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>email</b></code>&nbsp; <small>string</small>     <br>
    El correo electrónico con el que te registraste.
</p>
<p>
    <code><b>password</b></code>&nbsp; <small>string</small>     <br>
    La contraseña para poder acceder a tu cuenta.
</p>


## Llama a un validador que valida los campos necesarios para registrar un usuario (name, email, password, confirm password), si los valores son correctos, registrará al usuario y le creará un token.



> Example request:

```bash
curl -X POST \
    "http://localhost/api/register" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -d '{"name":"harum","email":"tenetur","password":"debitis","c_password":"et"}'

```

```javascript
const url = new URL(
    "http://localhost/api/register"
);

let headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
};

let body = {
    "name": "harum",
    "email": "tenetur",
    "password": "debitis",
    "c_password": "et"
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
null
```

### Request
<small class="badge badge-black">POST</small>
 **`api/register`**

<h4 class="fancy-heading-panel"><b>Body Parameters</b></h4>
<p>
    <code><b>name</b></code>&nbsp; <small>string</small>     <br>
    Tu nombre de usuario.
</p>
<p>
    <code><b>email</b></code>&nbsp; <small>string</small>     <br>
    El correo electrónico con el que te registraste.
</p>
<p>
    <code><b>password</b></code>&nbsp; <small>string</small>     <br>
    La contraseña para poder acceder a tu cuenta.
</p>
<p>
    <code><b>c_password</b></code>&nbsp; <small>string</small>     <br>
    Repite la contraseña.
</p>


## Details api: En Postman para ver los detalles de tu cuenta, no se usa en la web.



> Example request:

```bash
curl -X POST \
    "http://localhost/api/details" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/details"
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
 **`api/details`**



## Borrará el token que se haya activado de la cuenta correspondiente.



> Example request:

```bash
curl -X POST \
    "http://localhost/api/logout" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json"
```

```javascript
const url = new URL(
    "http://localhost/api/logout"
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
 **`api/logout`**




