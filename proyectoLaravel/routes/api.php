<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

// Route::apiResource("siglas", "AeroSiglasController");
// Route::apiResource("clima","ClimaController");
// Route::apiResource("vuelos","VuelosController");
// Route::apiResource("twitters", "TwitterController");
// Route::apiResource("tripadvisor", "TripAdvisorController");
Route::get('/boton','ClimaController@boton');

Route::post('/clima/datos','ClimaController@store');
Route::post('/vuelos/datos','VuelosController@store');
Route::post('/tienda/datos','TiendasController@store');
Route::post('/siglas/datos','AeroSiglasController@store');
Route::post('/comentarios/twitter', 'TwitterController@store');
Route::post('/tripadvisor/comentarios', 'TripAdvisorController@store');

Route::post('/modelos_prediccion', 'ModeloPrediccionController@store');
Route::post('/prediccion', 'PrediccionController@store');

Route::get('/twitter/opinionG','TwitterController@index');
Route::get('/siglas/lista', 'AeroSiglasController@index');
Route::get('/clima/lista', 'ClimaController@index');
Route::get('/tripadvisor/lista', 'TripAdvisorController@index');
Route::get('/aerolinea/lista', 'AerolineaController@index');

Route::get('/tripadvisorXaerolinea/{id}','TripAdvisorController@showXaerolinea');

Route::get('/climaXaeropuerto/{id}/{fecha}', 'ClimaController@showXclima');

Route::get('/aerolineas/lista', 'AerolineaController@show');
Route::get('/aerolineas/{id}', 'AerolineaController@show');

Route::get('/vuelosXaeropuerto/{id}/{fecha}', 'VuelosController@showxAeropuerto');
// Route::get('/vueloEspecifico/{id}','VuelosController@showxvueloEspecifico');
Route::get('/vuelo/{id}/{fecha}','VuelosController@showVuelo');
Route::get('/listaVuelos','VuelosController@index');

Route::post('login', 'UserController@login');
Route::post('register', 'UserController@register');
Route::group(['middleware' => 'auth:api'], function(){
Route::post('details', 'UserController@details');
Route::post('logout', 'UserController@logout');
});
Route::get('/vuelos/contador','VuelosController@countAll');//total de vuelos
Route::get('/vuelos/contadorDia', 'VuelosController@countEachDay');//vuelos por cada dia
Route::get('/vuelos/contadorAeropuerto', 'VuelosController@countFlightAriport');//vuelos totales de cada aeropuerto
Route::get('/vuelos/contadorAerolineasVuelos', 'VuelosController@countFlightAirline');
Route::get('/prediccion', 'VuelosController@prediccion');
Route::get('/clasificador', 'VuelosController@clasificar');

