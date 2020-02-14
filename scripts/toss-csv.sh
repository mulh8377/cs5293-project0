nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/tossers/toss_criminal.nim > data/csv/criminal.csv
echo "generating criminal csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/tossers/toss_officer.nim > data/csv/officer.csv
echo "generating officer csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/tossers/toss_scene.nim > data/csv/scene.csv
echo "generating scene csv file from database"
nim c -r /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/project0/modules/Storage/nim/tossers/toss_report.nim > data/csv/report.csv
echo "generating report csv file from database"