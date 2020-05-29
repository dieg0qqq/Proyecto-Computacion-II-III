<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePrediccionsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('prediccions', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->integer('identificador_vuelo');
            $table->string('id_vuelo');
            $table->string('origen');
            $table->string('destino');
            $table->date('fecha_vuelo');
            $table->string('hora_programada');
            $table->string('retraso');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('prediccions');
    }
}
