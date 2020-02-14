nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/toss_criminal.nim > data/csv/criminal.csv
echo "generating criminal csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/toss_officer.nim > data/csv/officer.csv
echo "generating officer csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/toss_scene.nim > data/csv/scene.csv
echo "generating scene csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/toss_report.nim > data/csv/report.csv
echo "generating report csv file from database"
rm -f nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/*.o
echo "removing exectuable files from the nim directory"
