# JEAMSQL

Python sql client using tsql, isql... drivers.

Connection to database as Sybase(ASE) or Oracle require huge installation, of dependencies and pakacges.
The aim of this project is to have a light library which offer only possibilities to write an SQL query and execute it.


## Requirement

To get started **JEAMSQL** support the following databasies:

* [Sybase](https://en.wikipedia.org/wiki/Sybase) which require installation of [tsql](https://manpages.debian.org/jessie/freetds-bin/tsql.1.en.html)  part of FreeTDS 
* [Oracle](https://en.wikipedia.org/wiki/Oracle_Database) *In progress*


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

This project embed **Tabulate**, a clone of [Astanin/Python-Tabulate](https://bitbucket.org/astanin/python-tabulate.git)
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

    python app.py [-h] -q QUERY -c CONFIG -d DATABASE [-x EXECUTE] [--list-tables]
                  [--description] [--connection] [-n NAME] [--format FORMAT]
    
      -h, --help                     Show this help message and exit
    
      -q QUERY,    --query           SQL query e.g: Insert, Select...
    
      -c CONFIG,   --config          Config file path containing databases properties
    
      -d DATABASE, --database        Database section fron the confiuration file
    
      -x,          --excetuce        Execute query with no results.Use this for Insert, Update... queries
    
      --list-tables                  List all tables in database
    
      --description                  List all tables with description in database
    
      --connection                   Display connection string
    
      -n NAME,     --name            Table name to view.to use with -d and --list-tables
    
    optional arguments:
    
      --format FORMAT                Output format [csv, sql, json]


### Configuration file (-c|--config)

As you can noticed the program need a config file containing database configuration.
you can look at **config.cfg** to see a sample config.

    [DATABASE-CONFIG-NAME]
    type        = sybase
    user        = username
    password    = password
    port        = 5000
    server      = 127.0.0.1
    fmt         = sql

_e.i: python_ **app.py** _-d_ **DATABASE-CONFIG-NAME** _-c_ **config.ini** _--connection_
_This command will print the connection command use for this config_

### Output format (--format)

The project support tree type of output *CSV, SQL and JSON*.

**SQL** format - _python app.py_ **[options]** **--format sql**

    |     ID     |    COLA    |    COLB    |
    |------------+------------+------------|
    |    2533788 | NULL       | NULL       |
    |    2533658 | NULL       | NULL       |
    |    2533866 | NULL       | NULL       |
    |    2533813 | NULL       | NULL       |
    |    2549990 | NULL       | NULL       |

**CSV** format - _python app.py_ **[options]** **--format csv**

    ID,COLA,COLB
    2533788,NULL,NULL
    2533658,NULL,NULL
    2533866,NULL,NULL
    2533813,NULL,NULL
    2549990,NULL,NULL

**JSON** format - _python app.py_ **[options]** **--format json**

    [
        {
            "COLA": "NULL",
            "ID": "2533788",
            "COLB": "NULL"
        },
        {
            "COLA": "NULL",
            "ID": "2533658",
            "COLB": "NULL"
        },
        {
            "COLA": "NULL",
            "ID": "2533866",
            "COLB": "NULL"
        },
        {
            "COLA": "NULL",
            "ID": "2533813",
            "COLB": "NULL"
        },
        {
            "COLA": "NULL",
            "ID": "2549990",
            "COLB": "NULL"
        }
    ]
