LANG = "python3"
ENV = "pipenv"

deps:
	bash scripts/update-deps.sh
reqs:
	bash scripts/update-reqs.sh
update:
	bash scripts/update-git.sh
