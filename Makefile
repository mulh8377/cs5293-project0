LANG = "python3"
ENV = "pipenv"

deps:
	$(ENV) update
reqs:deps
	$(ENV) run pip freeze > requirements.txt
update:reqs
	bash scripts/update-git.sh
	echo "generic update to version control"
