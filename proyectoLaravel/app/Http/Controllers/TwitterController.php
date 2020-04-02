<?php

namespace App\Http\Controllers;

use App\Twitter;
use Illuminate\Http\Request;

class TwitterController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $twitters = Twitter::all();
        return $twitters;
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
        foreach ($array['opiniones'] as $dict => $value) {
            $model = new Twitter();
            $model->nombreAerolinea = $array['opiniones'][$dict]['aerolinea'];
            $model->opinionExtraida = $array['opiniones'][$dict]['texto'];
            echo($array['opiniones'][$dict]['aerolinea']);
            echo($array['opiniones'][$dict]['texto']);
            $model->save();
        }
        return $model;
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Twitter  $twitter
     * @return \Illuminate\Http\Response
     */
    public function show(Twitter $twitter)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Twitter  $twitter
     * @return \Illuminate\Http\Response
     */
    public function edit(Twitter $twitter)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Twitter  $twitter
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Twitter $twitter)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Twitter  $twitter
     * @return \Illuminate\Http\Response
     */
    public function destroy(Twitter $twitter)
    {
        //
    }
}
