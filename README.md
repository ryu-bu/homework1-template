# homework1-template
A template repository for ECE552 Homework 1

`main.py` has a minimal example of what you need to run the project. 

Extra documentation for the `celloapi2` repository can be found at [this link](https://celloapi2.readthedocs.io/en/latest/celloapi2.html)

## What you need to use this Repository
`python 3.8 or above`

`docker and the associated docker image as specified in the homework and the API documentation`

`poetry package manager`

## How do I run this?
`poetry install`

`poetry run python main.py`

## Additional Information
This repository contains an input directory and an output directory. The
input files are located in the `input` directory and your results will be shown
in the `output` directory

```
├── input
│   ├── and.v
│   ├── Eco1C1G1T1.input.json
│   ├── Eco1C1G1T1.output.json
│   ├── Eco1C1G1T1.UCF.json
│   ├── nand.v
│   ├── options.csv
│   ├── struct.v
│   └── xor.v
├── main.py
├── output
├── poetry.lock
├── pyproject.toml
└── README.md
```

## New Optimization Structure
This is the new structure tree with new optimization scaffolding scripts that modify the input file and output it under `/input/modified/` folder.

```
<omitted>
├── input
│   ├── Eco1C1G1T1.UCF.json
│   ├── Eco1C1G1T1.input.json
│   ├── Eco1C1G1T1.output.json
│   ├── and.v
│   ├── modified
│   │   └── Eco1C1G1T1.input.json
│   ├── nand.v
│   ├── options.csv
│   ├── struct.v
│   └── xor.v
├── main.py
├── optimization.py
├── output
<omitted>
```
