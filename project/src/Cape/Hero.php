<?php

namespace project\Cape;

/**
 * Class Hero
 * @package project\Cape
 */
class Hero {
    /**
     * Hero constructor.
     * @param $name
     */
    public function __construct($name) {
        $this->name = $name;
    }

    /**
     * @return string
     */
    public function __toString() {
        // TODO: Implement __toString() method.
        return "this hero called {$this->name} uses cape";
    }
}