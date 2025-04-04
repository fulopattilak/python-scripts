import pandas as pd

from IPython.core.magic import register_cell_magic
from IPython import get_ipython
from pandasql import sqldf

# Sets Pandas display settings.

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.float_format = '{:.0f}'.format
# --------------------------------------------------------------------

# Creates the '%%sql' magic for dataframes. Stores the query in 'sql.query' and the result in 'sql.result'.

class sql:
    """
    Retrives the output of the '%%sql' magic.

    sql.result = The result of the query

    sql.query = The query itself
    """
    def __init__(self):
        self.query = None
        self.result = None
    @register_cell_magic
    def sql(self, line, cell):
        self.query = cell
        self.result = sqldf(cell)
sql = sql()
get_ipython().register_magic_function(sql.sql, 'cell', 'sql')
# --------------------------------------------------------------------
