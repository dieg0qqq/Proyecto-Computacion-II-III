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
            $table->string('hour');//1 - cambiar a date
            $table->string('forecast');//2
            $table->integer('temp');//3
            $table->double('rain');//5
            $table->integer('cloud');//7
            $table->integer('wind');//8
            $table->integer('gust');//9 rafaga
            $table->string('direction');//10
            $table->integer('humidity');//11
            $table->integer('pressure');//12
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
