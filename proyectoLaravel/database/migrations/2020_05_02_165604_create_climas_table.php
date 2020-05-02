<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateClimasTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('climas', function (Blueprint $table) {

            $table->id();
            $table->timestamps();
            $table->integer('siglas')->unsigned();
            $table->foreign('siglas')->references('id')->on('aero_siglas');
            $table->date('fecha');
            $table->string('hora');//1 - cambiar a date
            $table->string('prevision');//2
            $table->double('temperatura');//3
            $table->double('lluvia');//5
            $table->double('nubes');//7
            $table->double('viento');//8
            $table->double('rafagas');//9 rafaga
            $table->string('direccion');//10
            $table->double('humedad');//11
            $table->double('presion');//12
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('climas');
    }
}
