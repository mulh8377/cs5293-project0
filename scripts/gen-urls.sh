sed -i -e 's/dir=/normanpd.normanok.gov/g' data/txt/urls.txt
sed -i -e 's/name=//g' data/txt/urls.txt
sed -i -e 's/,ext=.pdf/.pdf/g' data/txt/urls.txt
sed -i -e 's/,/\//g' data/txt/urls.txt
sed -i -e 's/normanpd/http:\/\/normanpd/g' data/txt/urls.txt