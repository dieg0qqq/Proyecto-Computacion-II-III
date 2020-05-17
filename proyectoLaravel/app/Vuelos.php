<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Vuelos extends Model
{
    protected $fillable = ["IdVuelo","Aerolinea","Estado1","Estado2",
    "SiglasOrigen","Origen","HoraProgOrigen","HoraEstOrigen","TerminalOrigen","GateOrigen",
    "SiglasDestino","Destino","HoraProgDestino","HoraEstDestino","TerminalDestino","GateDestino"];
    protected $casts = [
        'created_at' => 'datetime:Y-m-d',
        'updated_at' => 'datetime:Y-m-d'
    ];
    protected $table = 'vuelos';
}
