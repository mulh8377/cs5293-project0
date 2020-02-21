sed -i -e 's/-//g' data/csv/arrest/Summary.txt ## gets rid of dashes
sed -i -e 's/ /\n/g' data/csv/arrest/Summary.txt ## gets rid of new lines
sed -i -e 's/Daily//g' data/csv/arrest/Summary.txt ## gets rid of Daily
sed -i -e 's/Arrest//g' data/csv/arrest/Summary.txt
sed -i -e 's/Activity//g' data/csv/arrest/Summary.txt
sed -i -e 's/(Public).nNORMAN//g' data/csv/arrest/Summary.txt
sed -i -e 's/POLICE//g' data/csv/arrest/Summary.txt
sed -i -e 's/DEPARTMENT.n//g' data/csv/arrest/Summary.txt
sed -i -e 's/;.n/;{"/g' data/csv/arrest/Summary.txt
sed -i -e 's/\/D.n/ D/g' data/csv/arrest/Summary.txt ##fixes the Docket Citation
sed -i -e 's/^.n//g' data/csv/arrest/Summary.txt ## clean beginning new lines
sed -i -e "s/^''//g" data/csv/arrest/Summary.txt  ##clean single quotes
sed -i -e 's/[0-9][0-9]:[0-9][0-9].n.$//g' data/csv/arrest/Summary.txt