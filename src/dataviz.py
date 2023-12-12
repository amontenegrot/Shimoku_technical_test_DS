import os

import pandas as pd

from os import getenv
import shimoku_api_python as Shimoku


# Get PATH folder from previous directorys
def get_path(prev_folders:int=0):
    for i in range(prev_folders-1): os.chdir('../')  # Change to previous folder
    PATH = os.path.dirname(os.getcwd()) + '/'
    PATH = PATH.replace('\\', '/')
    return PATH

def to_shimoku_structure(columns, dataframe):
    dataframe = dataframe[columns].copy()
    list_columns = list(dataframe.columns)
    dataframe['index'] = dataframe.index
    list_columns.insert(0, 'index')

    data_as_dictionary = dataframe.set_index('index').T.to_dict('dict').values()
    return list(data_as_dictionary)

def get_percentage(value:str, column:str, dataframe):
    result_general = dataframe[column].value_counts(normalize=True)
    result_specific = result_general[value] * 100
    result_specific = str(round(result_specific, 2))+' %'
    return result_specific

def value_counts_to_dataframe(column:str, dataframe):
    dataframe_prov = dataframe[column].value_counts()
    dataframe_prov = dataframe_prov.rename_axis(column)
    dataframe_prov = dataframe_prov.reset_index(name='value')

    return dataframe_prov


# # Environment settings
pd.options.display.max_columns = None  # Remove "dots" from display when printing dataframes
PATH = get_path(prev_folders=1)

ACCESS_TOKEN = getenv('SHIMOKU_TOKEN')
UNIVERSE_ID: str = getenv('UNIVERSE_ID')
WORKSPACE_ID: str = getenv('WORKSPACE_ID')


# # Read data
df = pd.read_csv(PATH + 'data/output_preprocesing.csv')

df['Created Date'] = pd.to_datetime(df['Created Date'], format='%Y-%m-%d')
df['Close Date'] = pd.to_datetime(df['Close Date'], format='%Y-%m-%d')

df['Year created'] = df['Created Date'].dt.strftime('%Y')
df['Year close'] = df['Close Date'].dt.strftime('%Y')


# # Data visualization
s = Shimoku.Client(
    access_token = ACCESS_TOKEN,
    universe_id = UNIVERSE_ID,
)
s.set_workspace(uuid = WORKSPACE_ID)
s.set_board('Data Scientist')
s.set_menu_path('Technical Test', 'Alejandro M.')

# ------------------- Title: Indicators chart ------------------#
s.plt.html(
    order=0,
    html=s.html_components.panel(
        href='https://www.linkedin.com/in/amontenegrot/',
        text='Alejandro Montenegro Taborda',
        button_panel='LinkedIn',
        symbol_name='insights'
    )
)

per_closed_won = get_percentage('Closed Won', 'Status', df)
per_closed_lost = get_percentage('Closed Lost', 'Status', df)
per_negotiation = get_percentage('Negotiation', 'Status', df)
per_checkbox = get_percentage('Checkbox', 'Status', df)
per_demo_1 = get_percentage('Demo 1', 'Status', df)
per_demo_2 = get_percentage('Demo 2', 'Status', df)

indicators_groups = [
    [
        {
            "description": "Successful sales.",
            "title": "Closed won",
            "value": per_closed_won,
            "align": "left",
            "color": "success",
            "variant": "contained"
        },
        {
            "description": "Lost sales",
            "title": "Closed Lost",
            "value": per_closed_lost,
            "align": "left",
            "color": "error"
        },
        {
            "description": "Sales",
            "title": "Negotiation",
            "value": per_negotiation,
            "align": "left",
            "color": "success",
        },
        {
            "description": "Verified customers",
            "title": "Checkbox",
            "value": per_checkbox,
            "align": "left",
            "color": "",
        },
        {
            "description": "First presentation",
            "title": "Demo 1",
            "value": per_demo_1,
            "align": "left",
            "color": "",
        },
        {
            "description": "Second presentation",
            "title": "Demo 2",
            "value": per_demo_2,
            "align": "left",
            "color": "",
        }
    ]
]

s.plt.indicators_with_header(
    order=1, title='Status', subtitle='Product purchase by the customer.',
    indicators_groups=indicators_groups,
    indicators_parameters=dict(
        cols_size=19,
    )
)

# ----------------------- Title: Pie chart ----------------------#
df_discount = value_counts_to_dataframe('Has discount', df)

list_columns = ['Has discount', 'value']
data = to_shimoku_structure(list_columns, df_discount)
data

s.plt.pie(
    data=data,
    names='Has discount',
    values='value',
    order=2,
    rows_size=2,
    cols_size=12,
    title='LE pie'
    )

# ----------------------- Title: Bar chart ----------------------#

list_columns = ['Year created', 'Price', 'Days in process']
data = to_shimoku_structure(list_columns, df)
data

s.plt.bar(
    order=3, title='Language expressiveness',
    data=data, x='Year created',
    y=['Price', 'Days in process'],
)
