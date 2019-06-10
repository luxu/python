<?php

require dirname(__DIR__) . '/vendor/autoload.php';

use project\Connection;
use Stringy\Stringy;

$connection = new Connection();

$connection->echoThis('Composer is pretty cool!');

//echo new project\Cape\Hero('Superman');
//echo PHP_EOL;

//echo Stringy::create('foo     bar')->collapseWhitespace()->swapCase();
//echo PHP_EOL;
