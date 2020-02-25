pipenv run python project0/modules/Editor/tosspdf.py && echo "pdf has been converted to txt"
pipenv run python project0/modules/Editor/tosstxt.py && echo "txt has been transformed"
cat data/txt/arrest/*.txt >> data/txt/arrest/ArrestSummary.txt
cat data/txt/case/*.txt >> data/txt/case/CaseSummary.txt
cat data/txt/incident/*.txt >> data/txt/incident/IncidentSummary.txt
rm -f data/csv/arrest/clean.csv
touch data/csv/arrest/clean.csv && echo "blank csv file made for arrest"
rm -f data/csv/case/clean.csv
touch data/csv/case/clean.csv && echo "blank csv file made for case"
rm -f data/csv/incident/clean.csv
touch data/csv/incident/clean.csv && echo "blank csv file made for incident"
pipenv run python project0/modules/Editor/tosscsv.py && echo "csv file has been created"
