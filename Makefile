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
run:
	pipenv run python3 project0/main.py