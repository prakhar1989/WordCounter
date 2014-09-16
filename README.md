Word Count Validator
===

### Building
To run the app, you must have `Python 2.7.x` and `pip` installed. To install `pip` for OSX, please see [this](ihttp://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x).

```shell
$ git clone https://github.com/prakhar1989/WordCounter.git
$ cd WordCounter
$ make install
$ chmod +x run
$ ./run
```

### Usage
```shell
./run -h
usage: run [-h] [-setup] [-test]

Run WordCount Validator

optional arguments:
  -h, --help  show this help message and exit
  -setup      Initialize database
  -test       Run testcases
```

### ToDo
- [x] Generate random text 
- [x] Think of a way to arbitrarily select a few words to omit in the text
- [x] Persist data
- [x] Persist admin data
- [x] Generate a token that the user sends to verify against
- [x] Setup some seed data
- [x] Add tests
- [x] Setup a build script
- [ ] Create a client
- [ ] Postman collection file
- [x] Deploy on DigitalOcean
- [ ] Detailed Readme
