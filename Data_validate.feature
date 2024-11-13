Feature: validate the data

    Scenario Outline: Test and validate the data
        Given User sets get universe script python at "Steps\\Get_Universe.txt"
            | connector | symbol | ccy | cal      | cut_off    | composition_date | fields | vendor_items          | out_file                | save_script     |
            | TEST      | SXW1E  | EUR | STOXXCAL | 2021,12,20 | 2021,12,20       |        | RBICS,RBICS_FOCUS,ISS | get_universe_output.csv | Get_Universe.py |


        Given User executes python file with virtual env
            | path                      | trigger         |
            | venv3.12\Scripts\activate | Get_Universe.py |

        When validate the data of <First_csv_file> with <second_csv_file>

        Examples:
            | First_csv_file          | second_csv_file         |
            | get_universe_output.csv | get_universe_output.csv |