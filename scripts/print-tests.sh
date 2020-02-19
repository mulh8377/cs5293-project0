touch docs/test_results/test_all.txt
cat docs/test_results/test_crime.txt >> docs/test_results/test_all.txt
cat docs/test_results/test_download.txt >> docs/test_results/test_all.txt
cat docs/test_results/test_storage.txt >> docs/test_results/test_all.txt
cat docs/test_results/test_editor.txt >> docs/test_results/test_all.txt
echo ""
cat docs/test_results/test_all.txt
echo "RESULTS FROM ALL TESTS"
echo ""
echo ""
echo ""
echo "Deleting docs/test_results/test_all.txt"
rm -f docs/test_results/test_all.txt
