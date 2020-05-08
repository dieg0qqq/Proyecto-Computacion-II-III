<?php

namespace App\Http\Controllers;

use App\TripAdvisor;
use App\Aerolinea;
use Illuminate\Http\Request;

/**
 * @group MRC TripAdvisor
 */

class TripAdvisorController extends Controller
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
     * Se recoge el diccionario, se busca el FK del nombre de aerolinea para coger su id y se crea una fila para la bbdd
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $array = $request->json()->all();  
        
        foreach ($array['comentarios'] as $dict => $value) {

            $model = new TripAdvisor();
            $x = $array['comentarios'][$dict]['id_aerolinea'];
            $idx = Aerolinea::select('id')->where('nombreAerolinea', $x)->get();
            $model->IdAerolinea = $idx[0]['id'];
            $model->Comentario = $array['comentarios'][$dict]['cuerpo'];
            $model->Valoracion = $array['comentarios'][$dict]['valoracion'];

            echo($array['comentarios'][$dict]['id_aerolinea']);
            echo($array['comentarios'][$dict]['cuerpo']);
            echo($array['comentarios'][$dict]['valoracion']);

            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\TripAdvisor  $tripAdvisor
     * @return \Illuminate\Http\Response
     */
    public function show(TripAdvisor $tripAdvisor)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\TripAdvisor  $tripAdvisor
     * @return \Illuminate\Http\Response
     */
    public function edit(TripAdvisor $tripAdvisor)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\TripAdvisor  $tripAdvisor
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, TripAdvisor $tripAdvisor)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\TripAdvisor  $tripAdvisor
     * @return \Illuminate\Http\Response
     */
    public function destroy(TripAdvisor $tripAdvisor)
    {
        //
    }
}
