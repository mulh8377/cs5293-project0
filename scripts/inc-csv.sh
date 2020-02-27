sed -i -e "s/,NORMAN POLICE DEPARTMENT,//g" data/csv/incident/clean.csv
sed -i -e "s/Daily Incident Summary (Public),//g" data/csv/incident/clean.csv
sed -i -e "s/,..$//g" data/csv/incident/clean.csv
sed -i -e "s/^,//g" data/csv/incident/clean.csv  ## clean starting comma
sed -i -e "s/,$//g" data/csv/incident/clean.csv ## clean bad comma
sed -i -e "s/^.-//g" data/csv/incident/clean.csv ## clean weird dash
sed -i -e "s/^,.$//g" data/csv/incident/clean.csv
sed -i -e "s/^$//g" data/csv/incident/clean.csv