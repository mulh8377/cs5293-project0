sed -i -e '/CC: [a-z]*/ d' data/txt/urls.txt
sed -i -e '/node/ d' data/txt/urls.txt
sed -i -e 's/(dir:/dir=/g' data/txt/urls.txt
echo "cleaned the directory"
sed -i -e 's/name:/name=/g' data/txt/urls.txt
echo "cleaned the name"
sed -i -e 's/ext:.*/ext=.pdf/g' data/txt/urls.txt
echo "cleaned the extension"
sed -i -e "s/ //g" data/txt/urls.txt
