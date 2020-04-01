<?php

namespace App\Http\Controllers;

use App\datosClima;
use Illuminate\Http\Request;

class DatosClimaController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $climas = datosClima::all();
        return $climas;
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
        $climas == datosClima::create($request->all());

        /*
        $clima = new datosClima();
        $clima->climas = request('climas');
        */
        
        return $climas;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\datosClima  $datosClima
     * @return \Illuminate\Http\Response
     */
    public function show(datosClima $datosClima)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\datosClima  $datosClima
     * @return \Illuminate\Http\Response
     */
    public function edit(datosClima $datosClima)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\datosClima  $datosClima
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, datosClima $datosClima)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\datosClima  $datosClima
     * @return \Illuminate\Http\Response
     */
    public function destroy(datosClima $datosClima)
    {
        //
    }
}
