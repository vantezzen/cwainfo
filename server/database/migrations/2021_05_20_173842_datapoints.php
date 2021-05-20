<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class Datapoints extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('datapoints', function (Blueprint $table) {
            $table->id();
            $table->unsignedInteger('number')->comment('Number of recorded devices');
            $table->timestamp('timestamp')->comment('Time this datapoint was recorded');
            $table->decimal('lat', 10, 6)->comment('Latitude');
            $table->decimal('lon', 10, 6)->comment('Longitude');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('datapoints');
    }
}
