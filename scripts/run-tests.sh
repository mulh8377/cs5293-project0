pipenv run python -m pytest tests/test_crime.py > docs/test_results/test_crime.txt
echo "tested test_crime file -- results stored in docs/test_results/"
pipenv run python -m pytest tests/test_download.py > docs/test_results/test_download.txt
echo "tested test_download file -- results stored in docs/test_results/"
pipenv run python -m pytest tests/test_storage.py > docs/test_results/test_storage.txt
echo "tested test_storage file -- results stored in docs/test_results/"
pipenv run python -m pytest tests/test_editor.py > docs/test_results/test_editor.txt
echo "tested test_editor file -- results stored in docs/test_results/"
echo "ALL TESTS HAVE BEEN FINISHED"
echo "GO TO docs/test_results/ to see results or run..."
echo "make print-tests to get the results at the command line"