
![PyPI](https://img.shields.io/pypi/v/diffcsv.svg) [![Build Status](https://travis-ci.org/ugursogukpinar/diff-csv.svg?branch=master)](https://travis-ci.org/ugursogukpinar/diff-csv)

# diffcsv

It finds differences between two version of a csv file which are built with same structure.

### Requirements
---

- Python 3.x

### Setup
---

```
$ pip install diffcsv
```


### Usage
---

```
diffcsv [-h] [--primary-key PRIMARY_KEY]
               [--based-on BASED_ON [BASED_ON ...]] [--delimiter DELIMITER]
               old_csv new_csv

positional arguments:
  old_csv               Path of old csv file
  new_csv               Path of new csv file

optional arguments:
  -h, --help            show this help message and exit
  --primary-key PRIMARY_KEY
                        Common key of two csv files
  --based-on BASED_ON [BASED_ON ...]
  --delimiter DELIMITER
                        Delimiter of csv files
```

Example: 

- version-1.csv
```
id,key,value,created_at
1,key-1,value-1,2018-01-01
2,key-2,value-2,2018-02-01
```

- version-2.csv
```
id,key,value,created_at
1,key-1,value-1-altered,2018-01-01
3,key-3,value-3,2018-02-02
```


Run:

```bash
$ diffcsv /path/of/version-1.csv /path/of/version-2.csv --primary-key id --based-on key value
```

Output:
```
"id","key","value","created_at","DIFF_STATUS"
"2","key-2","value-2","2018-02-01","DELETED"
"3","key-3","value-3","2018-02-02","INSERTED"
"1","key-1","value-1-altered","2018-01-01","UPDATED"
```


### Contributers
[**Kaan ant**](https://github.com/kaanant)

