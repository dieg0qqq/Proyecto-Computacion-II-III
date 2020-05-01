<?php

namespace App\Http\Controllers;

use App\AeroSiglas;
use Illuminate\Http\Request;

class AeroSiglasController extends Controller
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
