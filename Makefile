deps:
	bash scripts/update-deps.sh
reqs:
	bash scripts/update-reqs.sh
send-update:
	bash scripts/update-git.sh
grab-update:
	git pull origin master
data-crawl:
	bash scripts/crawl-website.sh
jah-db:
	bash scripts/jad-db.sh
clean-db:
	bash scipts/clean-db.sh
csv-db:
	bash scripts/toss-csv.sh
compile-util:
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_hash.so project0/modules/Utility/toss_hash.nim
	nim c --threads:on --app:lib --out:project0/modules/Utility/toss_download.so project0/modules/Utility/toss_download.nim
run:
	pipenv run python3 project0/main.py