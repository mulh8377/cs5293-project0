pipenv run python project0/modules/Editor/tosspdf.py && echo "pdf has been converted to txt"
pipenv run python project0/modules/Editor/tosstxt.py && echo "txt has been transformed"
cat data/txt/arrest/*.txt >> data/txt/arrest/ArrestSummary.txt
cat data/txt/case/*.txt >> data/txt/case/CaseSummary.txt
cat data/txt/incident/*.txt >> data/txt/incident/IncidentSummary.txt
