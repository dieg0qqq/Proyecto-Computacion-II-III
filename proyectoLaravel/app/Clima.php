<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Clima extends Model
{
    protected $fillable = ["siglas","hora","prevision","temperatura","lluvia","nubes","viento","rafagas","direccion","humedad","presion"];

}
