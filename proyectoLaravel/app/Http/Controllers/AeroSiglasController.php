<?php

namespace App\Http\Controllers;

use App\AeroSiglas;
use Illuminate\Http\Request;

/**
* @group MRC Aerosiglas
* Controlador-Modelo-Tabla
*/

class AeroSiglasController extends Controller
{
    /**
     * Devuelve la lista de aeropuertos junto con sus siglas
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $siglas = AeroSiglas::all();
        // error_log($siglas);
        return($siglas);
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
     * Display the specified resource.
     *
     * @param  \App\AeroSiglas  $twitter
     * @return \Illuminate\Http\Response
     */
    public function show($id)//AeroSiglas $aeroSiglas)
    {

    }

    /**
     * Recoge el diccionario y crea entradas para la bbdd
     * @response{
     * "nombre": "Aeropuerto de Madrid Barajas",
     * "siglas": "MAD",
     * "updated_at": "2020-05-08",
     * "created_at": "2020-05-08",
     * "id": 37
     * }
     *
     * @bodyParam id int required El id de la sigla.
     * @bodyParam name string required El nombre del aeropuerto de la sigla.
     * @bodyParam acronym string required El conjunto de siglas que define el aeropuerto/región.
     * 
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
        $array = $request->json()->all();
        foreach ($array['siglas'] as $dict => $value) {
            $model = new AeroSiglas();
            $model->nombre = $array['siglas'][$dict]['name'];
            $model->siglas = $array['siglas'][$dict]['acronym'];
            echo($array['siglas'][$dict]['name']);
            echo($array['siglas'][$dict]['acronym']);
            $model->save();
        }
        return $model;
    }

    
}
