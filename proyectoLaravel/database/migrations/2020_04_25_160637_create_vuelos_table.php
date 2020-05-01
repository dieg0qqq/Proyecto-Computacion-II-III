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
            $table->string('aerolinea');
            $table->string('estado1');
            $table->string('estado2');

            $table->string('siglas_origen');
            $table->string('origen');
            $table->string('hora_progr_origen');
            $table->string('hora_est_origen');
            $table->string('terminal_origen');
            $table->string('gate_origen');

            $table->string('siglas_destino');
            $table->string('destino');
            $table->string('hora_prog_destino');
            $table->string('hora_est_destino');
            $table->string('terminal_destino');
            $table->string('gate_destino');

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
