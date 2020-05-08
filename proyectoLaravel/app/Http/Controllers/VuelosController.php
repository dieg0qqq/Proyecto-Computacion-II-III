<?php

namespace App\Http\Controllers;

use App\Vuelos;
use App\AeroSiglas;
use App\Aerolinea;
use Illuminate\Http\Request;

class VuelosController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $array = $request->json()->all();  
        
        foreach ($array['vuelos'] as $dict => $value) {
            
            $model = new Vuelos();
            error_log($array['vuelos'][$dict]['IdVuelo']);
            $model->IdVuelo = $array['vuelos'][$dict]['IdVuelo'];
            $x = $array['vuelos'][$dict]['Aerolinea'];
            $idx = Aerolinea::where('nombreAerolinea', $x)->first();
            if ($idx == null){
                $tabla = new Aerolinea;
                $tabla->nombreAerolinea = $x;
                $tabla->save();
                error_log("se ha añadido aerolinea");
            }
            else{
                error_log("ya estaba en la tabla");
            }
            $id = Aerolinea::select('id')->where('nombreAerolinea', $x)->get();
            $model->Aerolinea = $id[0]['id'];
            error_log($id);
            // $model->Aerolinea = $array['vuelos'][$dict]['Aerolinea'];
            $model->Estado1 = $array['vuelos'][$dict]['Estado1'];
            $model->Estado2 = $array['vuelos'][$dict]['Estado2'];

            $y = $array['vuelos'][$dict]['SiglasOrigen'];
            $idy = AeroSiglas::select('id')->where('siglas',$y)->get();
            $model->SiglasOrigen = $idy[0]['id'];
            // $model->SiglasOrigen = $array['vuelos'][$dict]['SiglasOrigen'];
            $model->Origen = $array['vuelos'][$dict]['Origen'];
            $model->HoraProgOrigen = $array['vuelos'][$dict]['HoraProgOrigen'];
            $model->HoraEstOrigen = $array['vuelos'][$dict]['HoraEstOrigen'];
            $model->TerminalOrigen = $array['vuelos'][$dict]['TerminalOrigen'];
            $model->GateOrigen = $array['vuelos'][$dict]['GateOrigen'];

            $model->SiglasDestino = $array['vuelos'][$dict]['SiglasDestino'];
            $model->Destino = $array['vuelos'][$dict]['Destino'];
            $model->HoraProgDestino = $array['vuelos'][$dict]['HoraProgDestino'];
            $model->HoraEstDestino = $array['vuelos'][$dict]['HoraEstDestino'];
            $model->TerminalDestino = $array['vuelos'][$dict]['TerminalDestino'];
            $model->GateDestino = $array['vuelos'][$dict]['GateDestino'];

            echo($array['vuelos'][$dict]['SiglasOrigen']);
            echo($array['vuelos'][$dict]['Origen']);
            echo($array['vuelos'][$dict]['HoraProgOrigen']);
            echo($array['vuelos'][$dict]['HoraEstOrigen']);
            echo($array['vuelos'][$dict]['TerminalOrigen']);
            echo($array['vuelos'][$dict]['GateOrigen']);

            echo($array['vuelos'][$dict]['SiglasDestino']);
            echo($array['vuelos'][$dict]['Destino']);
            echo($array['vuelos'][$dict]['HoraProgDestino']);
            echo($array['vuelos'][$dict]['HoraEstDestino']);
            echo($array['vuelos'][$dict]['TerminalDestino']);
            echo($array['vuelos'][$dict]['GateDestino']);

            $model->save();
        }
        return $model;
    }
}
