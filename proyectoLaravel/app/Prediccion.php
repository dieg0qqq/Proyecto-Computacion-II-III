<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Prediccion extends Model
{
    protected $fillable = ["identificador_vuelo", "id_vuelo", "origen", "destino", 
    "fecha_vuelo", "hora_programada", "retraso"];
}
