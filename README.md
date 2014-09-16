Word Count Validator
===

### Build
To run the app, you must have `Python 2.7.x` and `pip` installed.

```shell
$ git clone https://github.com/prakhar1989/WordCounter.git
$ cd WordCounter
$ make install
$ chmod +x run
$ ./run
* Running on http://127.0.0.1:8000/
```

### Usage
```shell
$ ./run -h
usage: run [-h] [-setup] [-test]

Run WordCount Validator

optional arguments:
  -h, --help  show this help message and exit
  -setup      Initialize database
  -test       Run testcases
```

![image](newman_results.png)
