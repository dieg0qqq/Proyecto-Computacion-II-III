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

Route::apiResource("clima","ClimaController");
Route::apiResource("twitters", "TwitterController");
Route::apiResource("siglas", "AeroSiglasController");

Route::post('/comentarios/twitter', 'TwitterController@store');
Route::post('/clima/datos','ClimaController@store');
Route::post('/tienda/datos','TiendasController@store');
Route::post('/siglas/datos','AeroSiglasController@store');

Route::get('/twitter/opinionG','TwitterController@index');