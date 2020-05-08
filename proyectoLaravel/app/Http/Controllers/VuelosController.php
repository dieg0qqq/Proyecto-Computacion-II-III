<?php

namespace App\Http\Controllers;

use App\Vuelos;
use App\AeroSiglas;
use App\Aerolinea;
use Illuminate\Http\Request;

/**
 * @group MRC Vuelos
 * Recoge el diccionario y crea un fila para la bbdd
 */

class VuelosController extends Controller
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
     * [Se busca la aerolinea en su tabla y si no se encuentra se crea una entrada, además se busca la sigla del aeropuerto de origen]
     * @response {
     * "IdVuelo": "SWT 112", 
     * "Aerolinea": "Swiftair", 
     * "Estado1": "Unknown", 
     * "Estado2": "", 
     * "SiglasOrigen": "BCN", 
     * "Origen": "Barcelona", 
     * "HoraProgOrigen": "04:30 CEST", 
     * "HoraEstOrigen": "-- ", 
     * "TerminalOrigen": "N/A", 
     * "GateOrigen": "N/A", 
     * "SiglasDestino": "PMI", 
     * "Destino": "Palma Mallorca", 
     * "HoraProgDestino": "05:30 CEST", 
     * "HoraEstDestino": "-- ", 
     * "TerminalDestino": "N/A", 
     * "GateDestino": "N/A"}
     * 
     * @bodyParam id int required El id del vuelo en base de datos.
     * @bodyParam IdVuelo string required El identificador del vuelo.
     * @bodyParam Aerolinea int required El id de la aerolínea asociada por FK.
     * @bodyParam Estado1 string required El estado del vuelo.
     * @bodyParam Estado2 string required El subestado del vuelo.
     * @bodyParam SiglasOrigen int required El id del aeropuerto asociado por FK.
     * @bodyParam Origen string required De donde sale el vuelo.
     * @bodyParam HoraProgOrigen string required La hora programada de salida.
     * @bodyParam HoraEstOrigen string required La hora real de salida.
     * @bodyParam TerminalOrigen string required El terminal asociado al vuelo a la salida.
     * @bodyParam GateOrigen string required La puerta de embarque del vuelo a la salida.
     * @bodyParam SiglasDestino string required Las siglas del destino.
     * @bodyParam Destino string required El nombre del destino.
     * @bodyParam HoraProgDestino string required La hora programada de llegada.
     * @bodyParam HoraEstDestino string required La hora real de llegada.
     * @bodyParam TerminalDestino string required El terminal asociado al vuelo a la llegada.
     * @bodyParam GateDestino string required La puerta de embarque del vuelo a la llegada.
     * 
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $array = $request->json()->all();  
        
        foreach ($array['vuelos'] as $dict => $value) {
            
            $model = new Vuelos();
            error_log($array['vuelos'][$dict]['IdVuelo']);
            $model->IdVuelo = $array['vuelos'][$dict]['IdVuelo'];
            $x = $array['vuelos'][$dict]['Aerolinea'];
            $idx = Aerolinea::where('nombreAerolinea', $x)->first();
            if ($idx == null){
                $tabla = new Aerolinea;
                $tabla->nombreAerolinea = $x;
                $tabla->save();
                error_log("se ha añadido aerolinea");
            }
            else{
                error_log("ya estaba en la tabla");
            }
            $id = Aerolinea::select('id')->where('nombreAerolinea', $x)->get();
            $model->Aerolinea = $id[0]['id'];
            error_log($id);
            // $model->Aerolinea = $array['vuelos'][$dict]['Aerolinea'];
            $model->Estado1 = $array['vuelos'][$dict]['Estado1'];
            $model->Estado2 = $array['vuelos'][$dict]['Estado2'];

            $y = $array['vuelos'][$dict]['SiglasOrigen'];
            $idy = AeroSiglas::select('id')->where('siglas',$y)->get();
            $model->SiglasOrigen = $idy[0]['id'];
            // $model->SiglasOrigen = $array['vuelos'][$dict]['SiglasOrigen'];
            $model->Origen = $array['vuelos'][$dict]['Origen'];
            $model->HoraProgOrigen = $array['vuelos'][$dict]['HoraProgOrigen'];
            $model->HoraEstOrigen = $array['vuelos'][$dict]['HoraEstOrigen'];
            $model->TerminalOrigen = $array['vuelos'][$dict]['TerminalOrigen'];
            $model->GateOrigen = $array['vuelos'][$dict]['GateOrigen'];

            $model->SiglasDestino = $array['vuelos'][$dict]['SiglasDestino'];
            $model->Destino = $array['vuelos'][$dict]['Destino'];
            $model->HoraProgDestino = $array['vuelos'][$dict]['HoraProgDestino'];
            $model->HoraEstDestino = $array['vuelos'][$dict]['HoraEstDestino'];
            $model->TerminalDestino = $array['vuelos'][$dict]['TerminalDestino'];
            $model->GateDestino = $array['vuelos'][$dict]['GateDestino'];

            echo($array['vuelos'][$dict]['SiglasOrigen']);
            echo($array['vuelos'][$dict]['Origen']);
            echo($array['vuelos'][$dict]['HoraProgOrigen']);
            echo($array['vuelos'][$dict]['HoraEstOrigen']);
            echo($array['vuelos'][$dict]['TerminalOrigen']);
            echo($array['vuelos'][$dict]['GateOrigen']);

            echo($array['vuelos'][$dict]['SiglasDestino']);
            echo($array['vuelos'][$dict]['Destino']);
            echo($array['vuelos'][$dict]['HoraProgDestino']);
            echo($array['vuelos'][$dict]['HoraEstDestino']);
            echo($array['vuelos'][$dict]['TerminalDestino']);
            echo($array['vuelos'][$dict]['GateDestino']);

            $model->save();
        }
        return $model;
    }
}
