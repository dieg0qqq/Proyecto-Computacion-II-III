<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTripAdvisorsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('trip_advisors', function (Blueprint $table) {
            
            $table->id();
            $table->timestamps();
            $table->integer('IdAerolinea')->unsigned();
            $table->foreign('IdAerolinea')->references('id')->on('aerolineas');
            $table->text('Comentario');
            $table->double('Valoracion');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('trip_advisors');
    }
}
