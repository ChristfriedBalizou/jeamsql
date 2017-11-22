# JEAMSQL

Python low level sql client using tsql, isql... drivers.

Connection to database as Sybase(ASE) or Oracle require huge installation, of dependencies and pakacges.
The aim of this project is to have a light library which offer only possibilities to write an SQL query and execute it.

## Structure

The project structure look like:

    jeamsql/
    ├── adapters/
    │   ├── adapter.py
    │   ├── __init__.py
    │   ├── sybase.py
    │   └── tabulate/
    │   
    ├── app.py
    ├── db.py
    ├── __init__.py
    ├── LICENSE
    └── README.md


The **adapters** folder contains database adapters (e.i: sybase.py).
All adapters are inherit from  **Adapter** class and implement exposed functions

This project embed **Tabulate**, a clone of [Astanin/Python-Tabulate]: https://bitbucket.org/astanin/python-tabulate.git 
This make possible to display results as follow choosing a the right format(sql):

    |     ID     |    COLA    |    COLB    |
    |------------+------------+------------|
    |    2533788 | NULL       | NULL       |
    |    2533658 | NULL       | NULL       |
    |    2533866 | NULL       | NULL       |
    |    2533813 | NULL       | NULL       |
    |    2549990 | NULL       | NULL       |

**db.py** is an generic interface to all interface which takes a config file and create the correct database instance.

**app.py** is the entry point to get it start.


## Usage

    python app.py [-h] [-q QUERY] [-c CONFIG] [-d DATABASE] [-x] [--list-tables]
                  [--description] [--connection] [-n NAME] [--format FORMAT]
    
      -h, --help                     Show this help message and exit
    
      -q QUERY,    --query           SQL query e.g: Insert, Select...
    
      -c CONFIG,   --config          Config file path containingdatabases properties
    
      -d DATABASE, --database        Database section fron the confiuration file
    
      -x,          --excetuce        Execute query with no results.Use this for Insert, Update... queries
    
      --list-tables                  List all tables in database
    
      --description                  List all tables with description in database
    
      --connection                   Display connection string
    
      -n NAME,     --name            Table name to view.to use with -d and --list-tables
    
    optional arguments:
    
      --format FORMAT                Output format [csv, sql, json]

