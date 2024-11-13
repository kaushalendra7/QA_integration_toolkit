from behave import *
import pandas as pd
from pathlib import Path
from pandas.testing import assert_frame_equal

import subprocess


@given('User sets get universe script python at "{path_script}"')
def step_set_universe_script(context, path_script: str):
    for row in context.table:
        with open(Path(path_script)) as script_template:
            script = script_template.read().format(row["connector"], row["symbol"], row["ccy"], row["cal"], row["cut_off"], row["composition_date"],
                [item.strip() for item in row["fields"].split(",")], [item.strip() for item in row["vendor_items"].split(",")], row["out_file"])
        with open(Path(row["save_script"]), mode="w+") as py_script:
            py_script.write(script)
    
@given('User executes python file with virtual env')
def run_bat_file(context):
    for row in context.table:
        a=subprocess.run(rf"""{row["path"]} & python {row["trigger"]}""",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        
        
@given('validate the data of {First_csv_file} with {second_csv_file}')
def validate_data(context,First_csv_file:str,second_csv_file:str):
    context.first_csv = pd.read_csv(Path(First_csv_file),na_filter=False,sep=',')
    context.second_csv = pd.read_csv(Path(second_csv_file),na_filter=False,sep=',')