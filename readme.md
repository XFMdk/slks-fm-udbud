# SLKS Checker

Checks stuff on SLKS' website.

## Run

Create a new virtual envionment and install dependencies. Create a config file and modify. Then execute `check.py`:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

cp config.example.yaml config.yaml
vim config.yaml # Modify to taste

python3 check.py
```

