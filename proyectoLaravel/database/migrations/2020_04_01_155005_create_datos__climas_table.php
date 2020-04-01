<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateDatosClimasTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('datos_climas', function (Blueprint $table) {
            
            $table->id();
            $table->timestamps();
        
            $table->string('hour')->nullable();
            $table->string('forecast')->nullable();
            $table->string('temp')->nullable();
            $table->string('rain')->nullable();
            $table->string('cloud')->nullable();
            $table->string('wind')->nullable();
            $table->string('humidity')->nullable();
            $table->string('pressure')->nullable();
           
            //$table->json('climas');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('datos_climas');
    }
}
