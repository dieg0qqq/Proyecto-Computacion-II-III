<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class datosClima extends Model
{
    protected $fillable = ["id","timestamp","hour","forecast","temp","rain","cloud","wind","humidity","pressure"];
    //protected $casts = ['climas' => 'array'];
}
