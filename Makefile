install-deps:
	bash scripts/install-deps.sh

update-deps:
	bash scripts/update-deps.sh

update-reqs:
	bash scripts/update-reqs.sh

wipe-data:
	bash scripts/wipe-data.sh

build:
	bash scripts/install-deps.sh
	bash scripts/clean-db.sh
	rm -f data/csv/arrest/*.txt
	rm -f data/csv/case/*.txt
	rm -f data/csv/incident/*.txt
#################### installation build commands above.###############
send-update:
	bash scripts/update-git.sh
grab-update:
	git pull origin master
################### helpful version control build commands above. ###
data-crawl:
	bash scripts/crawl-website.sh
	nim c -r htmlparsetest.nim > data/txt/urls.txt
	rm -f data/html/crawl_test.html
	rm -f data/html/output.html
	bash scripts/clean-data.sh
	bash scripts/gen-urls.sh
################## a nice make command to mine data from our target website. #####
jah-db:
	bash scripts/jad-db.sh
clean-db:
	bash scipts/clean-db.sh
csv-db:
	bash scripts/toss-csv.sh
################ some useful make commands to create/clean/export our db ########
compile-util:
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_hash.so project0/modules/Utility/toss_hash
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_download.so project0/modules/Utility/toss_download
############### builds our nim files and creates a .so file ####################
test-crime:
	pipenv run python -m pytest tests/test_crime.py > docs/test_results/test_crime.txt
	echo "tested test_crime file -- results stored in docs/test_results/"
test-download:
	pipenv run python -m pytest tests/test_download.py > docs/test_results/test_download.txt
	echo "tested test_download file -- results stored in docs/test_results/"
test-storage:
	pipenv run python -m pytest tests/test_storage.py > docs/test_results/test_storage.txt
	echo "tested test_storage file -- results stored in docs/test_results/"
test-editor:
	pipenv run python -m pytest tests/test_editor.py > docs/test_results/test_editor.txt
	echo "tested test_editor file -- results stored in docs/test_results/"
run-tests:
	bash scripts/run-tests.sh
print-tests:
	bash scripts/print-tests.sh
run-project: data-crawl
	pipenv run python project0/main.py --arrests all
run-inc: data-crawl
	pipenv run python project0/main.py --incidents all
############## builds the project and runs the main function ##################
