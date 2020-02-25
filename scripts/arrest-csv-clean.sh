#sed -i -e 's/-//g' data/csv/arrest/Summary.txt ## gets rid of dashes
#sed -i -e 's/ /\n/g' data/csv/arrest/Summary.txt ## gets rid of new lines

#sed -i -e 's/;.n/;{"/g' data/csv/arrest/Summary.txt
sed -i -e 's/\/D.n/ D/g' data/csv/arrest/Summary.txt ##fixes the Docket Citation
sed -i -e 's/^.n//g' data/csv/arrest/CleanSummary.txt ## clean beginning new lines
sed -i -e "s/^''//g" data/csv/arrest/CleanSummary.txt  ##clean single quotes
sed -i -e 's/^"//g' data/csv/arrest/CleanSummary.txt
sed -i -e 's/-//g' data/csv/arrest/CleanSummary.txt ## gets rid of dashes
#sed -i -e "s/'//g" data/csv/arrest/CleanSummary.txt
sed -i -e 's/^Daily Arrest Activity (Public).nNORMAN POLICE DEPARTMENT.n''//g' data/csv/arrest/CleanSummary.txt ## gets rid of Daily
sed -i -e "s/^''//g" data/csv/arrest/CleanSummary.txt  ##clean single quotes
sed -i -e 's/^"//g' data/csv/arrest/CleanSummary.txt
sed -i -e 's/\/D.n/ D/g' data/csv/arrest/CleanSummary.txt ##fixes the Docket Citation
#sed -i -e "s//\n/,/g"
#sed -i -e "s/^[0-9].[0-9]+.[0-9][0-9][0-9][0-9] [0-9]+:[0-9]//g" data/csv/arrest/CleanSummary.txt
#sed -i -e 's/[0-9][0-9]:[0-9][0-9].n.$//g' data/csv/arrest/Summary.txt