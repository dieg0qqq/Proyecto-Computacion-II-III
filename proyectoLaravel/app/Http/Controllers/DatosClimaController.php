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
        $array = $request->json()->all();
        // echo($array['clima'][0]['forecast']);
        // return $array ;
        foreach ($array['clima'] as $dict => $value) {
            $climas = new datosClima();
            $climas->hour = $array['clima'][$dict]['hour'];
            $climas->forecast = $array['clima'][$dict]['forecast'];
            $climas->temp = $array['clima'][$dict]['temp'];
            $climas->rain = $array['clima'][$dict]['rain'];
            $climas->cloud = $array['clima'][$dict]['cloud'];
            $climas->wind = $array['clima'][$dict]['wind'];
            $climas->humidity = $array['clima'][$dict]['humidity'];
            $climas->pressure = $array['clima'][$dict]['pressure'];

            echo($array['clima'][$dict]['pressure']);
            $climas->save();
        }
        return $climas;
    }

    public function process_data() {
        /*
        $file = File::find($id);
    
        // Si fichero no existe:
        if ($file == null) {
    
            return redirect('/file')->with('error','No tienes permiso para este fichero.');
        }
    */
        // Se selecciona el fichero raw (sin extension)

            // Se crea el comando con ejecutable y la ruta de la imagen
            $cmd = storage_path("/Web Scrapping/Madrid-Weather.py");
            $path = "python Madrid-Weather.py";
            
            $ans = shell_exec($path);
            //print($ans[2]['forecast']);
            //dd($cmd,$ans);
            $content = json_decode($ans, true);
            return print($ans);  
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
