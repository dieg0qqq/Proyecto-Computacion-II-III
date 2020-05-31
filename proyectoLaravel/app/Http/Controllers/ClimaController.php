<?php

namespace App\Http\Controllers;

use App\Clima;
use App\AeroSiglas;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

/**
 * @group MRC Clima
 * Controlador-Modelo-Tabla
 */

class ClimaController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $climas = DB::table('climas')
        ->join('aero_siglas', 'climas.siglas', 'aero_siglas.id')
        ->select('aero_siglas.nombre','fecha','hora')
        ->get();
        return($climas);
    }

    /**
     * Devuelve todos los datos del clima de Weather-Airports
     * 
     */

    public function botonWeather()
    {
        set_time_limit(180);
        $cmd = "python ".storage_path("Weather-Airports.py"." 2>&1");
        error_log (shell_exec($cmd));
        
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
     * Recoge el diccionario y lo procesa para buscar el fk del aeropuerto antes de insertarlo en la bbdd
     * @response {
     * "id": 5,
     * "idaeropuerto": "LCG\n",
     * "fecha": "2020-05-08",
     * "hora": "14:00", 
     * "prevision": "Patchy rain possible", 
     * "temperatura": "18", 
     * "lluvia": "0.1", 
     * "nubes": "38", 
     * "viento": "11", 
     * "rafagas": "13", 
     * "direccion": "NW", 
     * "humedad": "78", 
     * "presion": "1013"
     * }
     *
     * @bodyParam id int required El id del clima.
     * @bodyParam idaeropuerto int required El id del aeropuerto asociado por FK.
     * @bodyParam fecha date required La fecha del día que se recogen los datos.
     * @bodyParam hora string required La hora y minutos del clima.
     * @bodyParam prevision double required Descripción del clima (nublado, soleado...).
     * @bodyParam temperatura double required La temperatura que había en °C.
     * @bodyParam lluvia double required La cantidad de lluvia en mm.
     * @bodyParam nubes double required El porcentaje de nubes que cubre el cielo.
     * @bodyParam viento double required La velocidad del viento en km/h.
     * @bodyParam rafagas double required La velocidad de las ráfagas en km/h.
     * @bodyParam direccion double required La dirección del viento en sistema cardinal.
     * @bodyParam humedad double required La cantidad de humedad en porcentaje.
     * @bodyParam presion double required La cantidad de presión en milibars (mb).
     * 
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $array = $request->json()->all();  
        foreach ($array['clima'] as $dict => $value) {
            $model = new Clima();
            $x = $array['clima'][$dict]['idaeropuerto'];
            $id = AeroSiglas::select('id')->where('siglas',$x)->get();
            $model->siglas = $id[0]['id'];
            $model->fecha = $array['clima'][$dict]['fecha'];
            $model->hora = $array['clima'][$dict]['hora'];
            $model->prevision = $array['clima'][$dict]['prevision'];
            $model->temperatura = $array['clima'][$dict]['temperatura'];
            $model->lluvia = $array['clima'][$dict]['lluvia'];
            $model->nubes = $array['clima'][$dict]['nubes'];
            $model->viento = $array['clima'][$dict]['viento'];
            $model->rafagas = $array['clima'][$dict]['rafagas'];
            $model->direccion = "";
            $model->humedad = $array['clima'][$dict]['humedad'];
            $model->presion = $array['clima'][$dict]['presion'];

            echo($array['clima'][$dict]['idaeropuerto']);
            echo($array['clima'][$dict]['fecha']);
            echo($array['clima'][$dict]['hora']);
            echo($array['clima'][$dict]['prevision']);
            echo($array['clima'][$dict]['temperatura']);
            echo($array['clima'][$dict]['lluvia']);
            echo($array['clima'][$dict]['nubes']);
            echo($array['clima'][$dict]['viento']);
            echo($array['clima'][$dict]['rafagas']);
            echo($array['clima'][$dict]['humedad']);
            echo($array['clima'][$dict]['presion']);
            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Clima  $clima
     * @return \Illuminate\Http\Response
     */
    public function show(Clima $clima)
    {
        //
    }

     /**
     * Muestra la lista de climas en un específico aeropuerto
     *
     * @param  \App\Clima  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function showXclima($id_aeropuerto, $fecha)
    {
        $lista_climas = DB::table('climas')
        ->join('aero_siglas', 'climas.siglas', 'aero_siglas.id')
        ->select('climas.created_at','aero_siglas.nombre','fecha','hora','prevision','temperatura','lluvia','nubes',
        'viento','rafagas','direccion','humedad','presion')
        ->where('climas.siglas', $id_aeropuerto)
        ->where(DB::raw("DATE(climas.created_at)"), $fecha)
        ->get();

        return $lista_climas;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Clima  $clima
     * @return \Illuminate\Http\Response
     */
    public function edit(Clima $clima)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Clima  $clima
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Clima $clima)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Clima  $clima
     * @return \Illuminate\Http\Response
     */
    public function destroy(Clima $clima)
    {
        //
    }
}
