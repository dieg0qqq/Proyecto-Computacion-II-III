<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class AeroSiglas extends Model
{
    protected $fillable = ["nombre","siglas"];

    protected $casts = [
        'created_at' => 'datetime:Y-m-d',
        'updated_at' => 'datetime:Y-m-d'
    ];
    protected $table = 'aero_siglas';

}
