# homework1
Our projects contain the optimization algorithms and interactive web GUI. 
***Note*** 
dockerfile is not working yet.

## Installation
```
pipenv install
```

## Deploy Development Server
```
$ pipenv shell
(pipenv_environment) $ cd source
(pipenv_environment) $ flask run
```

If above doesn't work:
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ cd source/
(env) $ flask run
```

It runs on localhost:5000

## New Optimization Structure
This is the new structure tree with new optimization scaffolding scripts that modify the input file and output it under `/input/modified/` folder.
Note: some folders are ommitted for simplicity. 

```
.
├── dockerfile
├── source
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── README.md
│   ├── app.py
│   ├── input
│   │   ├── Eco1C1G1T1.UCF.json
│   │   ├── Eco1C1G1T1.input.json
│   │   ├── Eco1C1G1T1.output.json
│   │   ├── and.v
│   │   ├── modified
│   │   │   └── Eco1C1G1T1.input.json
│   │   ├── nand.v
│   │   ├── options.csv
│   │   ├── struct.v
│   │   └── xor.v
│   ├── main.py
│   ├── optimization.py
│   ├── output
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── static
│   │   └── loading.GIF
│   └── templates
│       ├── about.html
│       ├── base.html
│       ├── index.html
│       └── score.html
└── tree.txt
```
