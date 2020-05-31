<?php

namespace App\Http\Controllers;

use App\Aerolinea;
use Illuminate\Http\Request;

class AerolineaController extends Controller
{
    /**
     * [Devuelve todas las aerolineas que tengamos asociados a los vuelos]
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $aerolineas = Aerolinea::all();
        return($aerolineas);
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
        //
        
    }

    /**
     * [Devuelve la lista de vuelos de un aeropuerto en especifico]
     *
     * @param  \App\Aerolinea  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function show($idAeropuerto)
    {
        $aero = Aerolinea::select("nombreAerolinea")->where('id',$idAeropuerto)->get();
        return $aero;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Aerolinea  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function edit(Aerolinea $aerolinea)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Aerolinea  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Aerolinea $aerolinea)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Aerolinea  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function destroy(Aerolinea $aerolinea)
    {
        //
    }
}
