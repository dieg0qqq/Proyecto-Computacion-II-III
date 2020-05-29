<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class ModeloPrediccion extends Model
{
    protected $fillable = ["algoritmo", "exactitud", "recall", "precision"];
}
