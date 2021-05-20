<?php

/** @var \Laravel\Lumen\Routing\Router $router */
use Illuminate\Http\Request;
use App\Models\Datapoint;

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->post('/push', function (Request $request) use ($router) {
    $this->validate($request, [
        'key' => 'required',
        'number' => 'required|integer',
        'lat' => 'required|numeric',
        'lon' => 'required|numeric',
        'timestamp' => 'required|numeric',
    ]);

    $dp = new Datapoint();
    $dp->number = $request->input('number');
    $dp->timestamp = $request->input('timestamp');
    $dp->lat = $request->input('lat');
    $dp->lon = $request->input('lon');
    $dp->save();

    return 1;
});

$router->get('/ping', function () use ($router) {
    return "pong";
});

$router->get('/', function () use ($router) {
    return $router->app->version();
});
