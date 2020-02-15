install-nim:
	bash scripts/install-nim.sh
install-deps:
	bash scripts/update-deps.sh
install-reqs:
	bash scripts/update-reqs.sh
#################### installation build commands above.###############
send-update:
	bash scripts/update-git.sh
grab-update:
	git pull origin master
################### helpful version control build commands above. ###
data-crawl:
	bash scripts/crawl-website.sh
	nim c -r htmlparsetest.nim > data/html/urls.txt
	rm -f data/html/crawl_test.html
	rm -f data/html/output.html
	bash scripts/clean-data.sh
################## a nice make command to mine data from our target website. #####
jah-db:
	bash scripts/jad-db.sh
clean-db:
	bash scipts/clean-db.sh
csv-db:
	bash scripts/toss-csv.sh
################ some useful make commands to create/clean/export our db ########
compile-util:
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_hash.so project0/modules/Utility/toss_hash.nim
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_download.so project0/modules/Utility/toss_download.nim
############### builds our nim files and creates a .so file ####################
run:
	pipenv run python3 project0/main.py
############## builds the project and runs the main function ##################