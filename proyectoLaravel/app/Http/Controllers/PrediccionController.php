<?php

namespace App\Http\Controllers;

use App\Prediccion;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class PrediccionController extends Controller
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
        DB::table('prediccions')->truncate();
        $array = $request->json()->all();

        foreach ($array['prediccion'] as $dict => $value){
            $model = new Prediccion();
            $model->identificador_vuelo = $array['prediccion'][$dict]['identificador_vuelo'];
            $model->id_vuelo = $array['prediccion'][$dict]['idVuelo'];
            $model->origen = $array['prediccion'][$dict]['origen'];
            $model->destino = $array['prediccion'][$dict]['destino'];
            $model->fecha_vuelo = $array['prediccion'][$dict]['fecha'];
            $model->hora_programada = $array['prediccion'][$dict]['hora_programada'];
            $model->retraso = $array['prediccion'][$dict]['retraso'];

            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Prediccion  $prediccion
     * @return \Illuminate\Http\Response
     */
    public function show(Prediccion $prediccion)
    {
        //
    }

    public function search($id_vuelo, $fecha)
    {
        $vuelo = DB::table('prediccions')
        ->select('retraso')
        ->where('id_vuelo', $id_vuelo)
        ->where('fecha_vuelo', $fecha)
        ->get();

        return $vuelo;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Prediccion  $prediccion
     * @return \Illuminate\Http\Response
     */
    public function edit(Prediccion $prediccion)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Prediccion  $prediccion
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Prediccion $prediccion)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Prediccion  $prediccion
     * @return \Illuminate\Http\Response
     */
    public function destroy(Prediccion $prediccion)
    {
        //
    }
}
