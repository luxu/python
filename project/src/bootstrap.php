<?php

namespace project\Functions;


if (!function_exists(' project\Functions\echoIt')) {
    /**
     * @param $it
     */
    function echoThis($it)
    {
        echo $it;
        echo PHP_EOL;
    }
}