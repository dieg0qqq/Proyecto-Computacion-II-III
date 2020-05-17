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

Route::post('/clima/datos','ClimaController@store');
Route::post('/vuelos/datos','VuelosController@store');
Route::post('/tienda/datos','TiendasController@store');
Route::post('/siglas/datos','AeroSiglasController@store');
Route::post('/comentarios/twitter', 'TwitterController@store');
Route::post('/tripadvisor/comentarios', 'TripAdvisorController@store');

Route::get('/twitter/opinionG','TwitterController@index');
Route::get('/siglas/lista', 'AeroSiglasController@index');

Route::get('/aerolineas/lista', 'AerolineaController@show');
Route::get('/aerolineas/{id}', 'AerolineaController@show');

Route::get('/vuelosXaeropuerto/{id}', 'VuelosController@showxAeropuerto');
Route::get('/vueloEspecifico/{id}','VuelosController@showxvueloEspecifico');
Route::get('/vuelo/{id}/{fecha}','VuelosController@showVuelo');

Route::post('login', 'UserController@login');
Route::post('register', 'UserController@register');
Route::group(['middleware' => 'auth:api'], function(){
Route::post('details', 'UserController@details');
Route::post('logout', 'UserController@logout');
});