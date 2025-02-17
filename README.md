# Case 1 - SQL

## Answers to the Case - Tableau Dashboard

The Tableau dashboard is published in the Tableau Public. You can access in [THIS LINK](https://public.tableau.com/app/profile/helio.assakura/viz/InternetgrowthinArgentina-MLCase/Growth). There's also a `.twbx` in the Github Repo that can be imported in the Tableau Desktop.

The dashboard consists on 5 Tabs:
1. **Growth**: Explains how was the Growth of the Internet usage in Argentina and compares with other LATAM countries
2. **Enablers**: Explains what made this growth possible, where the investments were made, etc
3. **Impacts**: The results and impacts of this technological development, both for good and for bad
4. **Correlations**: An interactive graph that shows the correlation between the Internet usage growth and other variables
5. **Conclusion**: A summary of all the topics that were explained before

## Code

There's a code that generated the Excel dataset that feeds the Tableau Dashboards.

### Creating a virtual environment

Prepare you environment by creating a virtualenv:

    python3 -m venv venv

Then you can add the environment binaries to you path running:

    source venv/bin/activate

To leave your venv, just run `deactivate`.

### Depedencies

After creating the venv, you should install the dependencies with:

    pip install -r requirements.txt

### Running the script

Run the script with:

    python3 solution_case_tableau.py 

It creates, populates and then generates a Excel file with the dataset from https://data.worldbank.org/country/argentina?view=chart

Then, the dataset is uploaded on Tableau as the main Datasource.

## Files

There are extra files / folders:

1. **Internet Growth in Argentina - ML Case.twbx**: Tableau twbx file with the Dashboard and Datasources
2. **API_Download_DS2_en_csv_v2_69720.csv**: Output from the datawordbank website.
3. **/images**: Contains the images of all the Tabs in the Dashboard
4. **tableau_case_all.xlsx**: Final XLSX file with the data pivoted.