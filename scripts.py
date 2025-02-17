# Imports Pandas and sets display settings.
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.float_format = '{:.0f}'.format


# Enables the %%sql magic for cells in a notebook. The output of a SQL cell can be referenced by [VARIABLE] = _ (underscore).
from IPython.core.magic import register_cell_magic
from pandasql import sqldf

@register_cell_magic
def sql(line, cell):
    query = sqldf(cell)
    return query.head()
