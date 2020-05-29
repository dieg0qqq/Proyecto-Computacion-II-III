<?php

namespace App\Http\Controllers;

use App\ModeloPrediccion;
use Illuminate\Http\Request;

class ModeloPrediccionController extends Controller
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

        foreach ($array['modelos'] as $dict => $value){
            $model = new ModeloPrediccion();
            
            $model->algoritmo = $array['modelos'][$dict]['algoritmo'];
            $model->exactitud = $array['modelos'][$dict]['exactitud'];
            $model->recall = $array['modelos'][$dict]['recall'];
            $model->precision = $array['modelos'][$dict]['precision'];

            echo($array['modelos'][$dict]['algoritmo']);
            echo($array['modelos'][$dict]['exactitud']);
            echo($array['modelos'][$dict]['recall']);
            echo($array['modelos'][$dict]['precision']);

            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\ModeloPrediccion  $modeloPrediccion
     * @return \Illuminate\Http\Response
     */
    public function show(ModeloPrediccion $modeloPrediccion)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\ModeloPrediccion  $modeloPrediccion
     * @return \Illuminate\Http\Response
     */
    public function edit(ModeloPrediccion $modeloPrediccion)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\ModeloPrediccion  $modeloPrediccion
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, ModeloPrediccion $modeloPrediccion)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\ModeloPrediccion  $modeloPrediccion
     * @return \Illuminate\Http\Response
     */
    public function destroy(ModeloPrediccion $modeloPrediccion)
    {
        //
    }
}
