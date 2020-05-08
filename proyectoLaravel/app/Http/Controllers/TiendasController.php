<?php

namespace App\Http\Controllers;

use App\Tiendas;
use Illuminate\Http\Request;

/**
* @group MRC Tiendas
* Controlador-Modelo-Tabla
*/

class TiendasController extends Controller
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
     * Recoge el diccionario y crea las filas para la bbdd
     * 
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
        $array = $request->json()->all();
        foreach ($array['tiendas'] as $dict => $value) {
            $model = new Tiendas();
            $model->nombre_tienda = $array['tiendas'][$dict]['tienda'];
            $model->direccion = $array['tiendas'][$dict]['direccion'];
            echo($array['tiendas'][$dict]['tienda']);
            echo($array['tiendas'][$dict]['direccion']);
            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Tiendas  $tiendas
     * @return \Illuminate\Http\Response
     */
    public function show(Tiendas $tiendas)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Tiendas  $tiendas
     * @return \Illuminate\Http\Response
     */
    public function edit(Tiendas $tiendas)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Tiendas  $tiendas
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Tiendas $tiendas)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Tiendas  $tiendas
     * @return \Illuminate\Http\Response
     */
    public function destroy(Tiendas $tiendas)
    {
        //
    }
}
