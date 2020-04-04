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

Route::apiResource("climas","DatosClimaController");
Route::apiResource("twitters", "TwitterController");

Route::post('/twitter/opinion', 'TwitterController@store');
Route::post('/clima/datos','DatosClimaController@store');
Route::post('/tienda/datos','TiendasController@store');

Route::get('/twitter/opinionG','TwitterController@index');