<?php

namespace Hero;

/**
 * Class QueryBuilder
 * @package Hero
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
     * @param string $table
     * @param string $fields
     * @param string $values
     */
    public function insert($table, $fields, $values)
    {
        // INSERT INTO {table} ({fields}) VALUES ({values});
    }

    /**
     * @param string $table
     * @param string $fields
     */
    public function select($table, $fields)
    {
        // SELECT {fields} FROM <JOIN> {table} <WHERE> <GROUP> <ORDER> <HAVING> <LIMIT>;
    }

    /**
     * @param string $table
     * @param string $set
     */
    public function update($table, $set)
    {
        // UPDATE {table} SET {set} <WHERE>
    }

    /**
     * @param string $table
     */
    public function delete($table)
    {
        // DELETE FROM {table} <JOIN> <USING> <WHERE>
    }
}