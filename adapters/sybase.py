from adapter import Adapter

import re


class Sybase(Adapter):

    def __init__(self, *args, **kwargs):

        connection_cmd = "tsql -S%s:%s -U%s -P%s -o fq" % (
                kwargs.get('server'),
                kwargs.get('port'),
                kwargs.get('user'),
                kwargs.get('password'))

        test_query = "sp_tables"

        # To detect error in output
        pattern = re.compile(r"severity\s+\d+")

        super(Sybase, self).__init__(
                cmd=["tsql"],
                connection_cmd=connection_cmd.split(' '),
                test_query=test_query,
                error_regex=pattern,
                *args,
                **kwargs
        )


    def select(self, query=None):

        super(Sybase, self).select(query=query)

        # TODO use sqlparse
        if not query:
            raise SyntaxError("Wrong query %s " % query)

        return self.__runsql__(query)


    def execut(self, query):

        super(Sybase, self).execute(query=query)

        # TODO use sqlparse
        if not query:
            raise SyntaxError("Wrong query %s " % query)

        self.__runsql__(query)


    def tables(self, name):

        super(Sybase, self).tables(name=name)

        req = "sp_tables @table_type=\"'TABLE'\""

        if name:
            req = req + (", @table_name='%s'" % name)

        return self.__runsql__(req)
