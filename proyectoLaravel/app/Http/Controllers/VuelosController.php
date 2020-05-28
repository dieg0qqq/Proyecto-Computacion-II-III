<?php

namespace App\Http\Controllers;

use App\Vuelos;
use App\AeroSiglas;
use App\Aerolinea;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

/**
 * @group MRC Vuelos
 * Recoge el diccionario y crea un fila para la bbdd
 */

class VuelosController extends Controller
{
    /**
     * Devuelve todos los vuelos que hayan en la BBDD
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
        $vuelo = DB::table('vuelos')
            ->join('aerolineas','vuelos.Aerolinea','aerolineas.id')
            ->join('aero_siglas', 'vuelos.SiglasOrigen', 'aero_siglas.id')  
            ->select('IdVuelo','aerolineas.nombreAerolinea', 'aero_siglas.nombre')        
            ->get();
        return($vuelo);
    }

    /**
     * Cantidad de vuelos totales en la base de datos
     * 
     * 
     */
    public function countAll()
    {
        $num_vuelos = DB::table('vuelos')
            ->count();
        return $num_vuelos;
    }

    /**
     * Cantidad de vuelos por dia
     * 
     */
    public function countEachDay()
    {
        $num_vuelos = DB::table('vuelos')
            ->select(DB::raw('DATE(created_at) as date'), DB::raw('count(*) as views'))
            ->groupBy('date')
            ->get();
        return $num_vuelos;
    }

/**
 * numero de vuelos por aeropuerto
 * numero de comentarios por aerolinea
 * numero de retrasos por aeropuerto
 * porcentaje de comenatarios positivos y los negativos
 * 
 */

    /**
     * Numero de vuelos por Aeropuerto
     * 
     */
    public function countFlightAriport(){
        $num_vuelos = DB::table('vuelos')
            ->join('aero_siglas', 'vuelos.SiglasOrigen', 'aero_siglas.id')  
            ->select(DB::raw('count(*) as num_vuelos'), DB::raw('aero_siglas.nombre as aeropuertos'))
            ->groupBy('aeropuertos')
            ->get();
        return $num_vuelos;
    }

    /**
     * Numero de vuelos por Aerolinea
     * 
     * 
     */
    public function countFlightAirline(){
        $num_vuelos = DB::table('vuelos')
        ->join('aero_siglas', 'vuelos.SiglasOrigen', 'aero_siglas.id')
        ->join('aerolineas','vuelos.Aerolinea','aerolineas.id')
        ->select(DB::raw('count(*) as numero_vuelos'), DB::raw('aerolineas.nombreAerolinea as Aerolineas'), 'aero_siglas.nombre')
        ->groupBy(['Aerolineas', 'aero_siglas.nombre'])
        ->get();
        return $num_vuelos;
    }

    /**
     * 
     */
    public function commentsAirline(){
        
    }
    /**
     * 
     */
    public function prediccion()
    {
        $filas_vuelos = DB::select(DB::raw('select * from vuelos
        join aero_siglas on vuelos.SiglasOrigen = aero_siglas.id
        inner join climas on vuelos.SiglasOrigen = climas.siglas AND DATE(vuelos.created_at)= climas.fecha 
            and substr(vuelos.HoraProgOrigen, 1, 2) = substr(climas.hora, 1 ,2 )'));
        return $filas_vuelos;
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
     * Muestra la lista de vuelos en un específico aeropuerto
     *
     * @param  \App\Vuelos  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function showxAeropuerto($id_aeropuerto)
    {
        $lista_aeropuertos = DB::table('vuelos')
            ->join('aerolineas','vuelos.Aerolinea','aerolineas.id')
            ->join('aero_siglas', 'vuelos.SiglasOrigen', 'aero_siglas.id')
            ->select('IdVuelo','aerolineas.nombreAerolinea','Estado1','Estado2',
            'aero_siglas.nombre','Origen','HoraProgOrigen','HoraEstOrigen','TerminalOrigen',
            'GateOrigen','SiglasDestino','Destino','HoraProgDestino','HoraEstDestino',
            'TerminalDestino','GateDestino')
            ->where('siglasOrigen', $id_aeropuerto)
            ->get();
        return $lista_aeropuertos;
    }

    // /**
    //  * Display the specified resource.
    //  *
    //  * @param  \App\Vuelos  $aerolinea
    //  * @return \Illuminate\Http\Response
    //  */
    // public function showxvueloEspecifico($id_vuelo)
    // {
    //     $vuelo = Vuelos::select('*')->join('aerolineas', 'aerolineas.id', '=', 'vuelos.Aerolinea')->where('IdVuelo',$id_vuelo)->get();

    //     return $vuelo;
    // }

    /**
     * Muestra los detalles del vuelo 
     * 
     * @param  \App\Vuelos  $aerolinea
     * @return \Illuminate\Http\Response
     */
    public function showVuelo($id_vuelo, $fecha){
        $vuelo = DB::table('vuelos')
            ->join('aerolineas','vuelos.Aerolinea','aerolineas.id')
            ->join('aero_siglas', 'vuelos.SiglasOrigen', 'aero_siglas.id')
            ->select('*')
            ->where('IdVuelo',$id_vuelo)
            ->whereDate('vuelos.created_at',$fecha)
            ->get();
        return $vuelo;
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
