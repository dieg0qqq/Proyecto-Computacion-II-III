<?php

namespace App\Http\Controllers;

use App\Clima;
use App\AeroSiglas;
use Illuminate\Http\Request;

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
            $model->direccion = $array['clima'][$dict]['direccion'];
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
            echo($array['clima'][$dict]['direccion']);
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
