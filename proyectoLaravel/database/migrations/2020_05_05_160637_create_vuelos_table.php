<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateVuelosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('vuelos', function (Blueprint $table) {

            $table->id();
            $table->timestamps();
            $table->string('IdVuelo');
            // $table->string('Aerolinea');
            $table->integer('Aerolinea')->unsigned();
            $table->foreign('Aerolinea')->references('id')->on('aerolineas');
            $table->string('Estado1');
            $table->string('Estado2');

            $table->integer('SiglasOrigen')->unsigned();
            $table->foreign('SiglasOrigen')->references('id')->on('aero_siglas');
            // $table->string('SiglasOrigen');
            $table->string('Origen');
            $table->string('HoraProgOrigen');
            $table->string('HoraEstOrigen');
            $table->string('TerminalOrigen');
            $table->string('GateOrigen');

            $table->string('SiglasDestino');
            $table->string('Destino');
            $table->string('HoraProgDestino');
            $table->string('HoraEstDestino');
            $table->string('TerminalDestino');
            $table->string('GateDestino');

        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('vuelos');
    }
}
