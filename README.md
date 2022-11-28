# Parse shop products example
Labaratory work for "Extragerea datelor din Web"

### How to install
```
pip3 install virtualenv
git clone https://github.com/vasflam/edw-lab01.git
cd edw-lab01
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Fetch data
To fetch data run command in activated venv
```
scrapy crawl atehno -O data.json
```

### Run web server
To start web server run command in activated venv and navigate to http://127.0.0.1:5000
```
flask --app main run
```
