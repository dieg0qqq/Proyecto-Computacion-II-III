<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateModeloPrediccionsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('modelo_prediccions', function (Blueprint $table) {
            $table->id();
            $table->timestamps();
            $table->string("algoritmo");
            $table->string("exactitud");
            $table->string("recall");
            $table->string("precision");
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('modelo_prediccions');
    }
}
