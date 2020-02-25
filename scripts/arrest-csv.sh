sed -i -e 's/Released,/Released-/g' data/csv/arrest/clean.csv ##fixes the Docket Citation
sed -i -e 's/, k$/k/g' data/csv/arrest/clean.csv
sed -i -e 's/, h$/h/g' data/csv/arrest/clean.csv
sed -i -e 's/, 2020, /, 2020-/g' data/csv/arrest/clean.csv
sed -i -e 's/, OKLAHO, /, OKLAHO/g' data/csv/arrest/clean.csv
sed -i -e 's/, WEATHE, /, WEATHE/g' data/csv/arrest/clean.csv
sed -i -e 's/ WOODLA, / WOODLA/g' data/csv/arrest/clean.csv
sed -i -e 's/, RICHMO, /, RICHMO/g' data/csv/arrest/clean.csv
sed -i -e 's/, <UNKNOWN>,/, CITY, STATE, ZIP,/g' data/csv/arrest/clean.csv
sed -i -e 's/, UNKOWN,/, CITY, STATE, ZIP,/g' data/csv/arrest/clean.csv
sed -i -e 's/, HOMELESS, /, HOMELESS, OK, ZIP,/g' data/csv/arrest/clean.csv
#sed -i -e 's/^[0-9]/, t[0-9]/g' data/csv/arrest/clean.csv