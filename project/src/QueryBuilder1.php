<?php

namespace project;

/**
 * Class QueryBuilder
 * @package project
 */
class QueryBuilder
{
    /**
     * QueryBuilder constructor.
     */
    public function __construct()
    {
        // configure
    }

    /**
     *
     */
    public function insert()
    {
        // INSERT INTO users (nome, login, password) VALUES (?, ?, ?);
    }

    /**
     *
     */
    public function select()
    {
        // SELECT id, nome, login, password FROM <JOIN> users <WHERE> <GROUP> <ORDER> <HAVING> <LIMIT>;
    }

    /**
     *
     */
    public function update()
    {
        // UPDATE users SET nome = ?, login = ?, password = ? WHERE id = ?
    }

    /**
     *
     */
    public function delete()
    {
        // DELETE FROM users <JOIN> <USING> WHERE id = ?
    }
}