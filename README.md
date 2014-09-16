Word Count Validator
===

### Demo

The service is hosted [online](http://192.241.186.225/) for you to play.

### Build
To run the app on your own machine, you must have `Python 2.7.x` and `pip` installed.

```shell
$ git clone https://github.com/prakhar1989/WordCounter.git
$ cd WordCounter
$ make install
$ chmod +x run
$ ./run
* Running on http://127.0.0.1:8000/
```

### Routes

| Route        | Description    |
| ------------- |:-------------:|
| GET /     | Return random text |
| GET /?random?true | Create and return random text |
| POST /validate     | Validate request|
| GET /admin | Add new data |

#### Data Format

`GET /` and `GET /?random=true` return a JSON object of the following schema
```javascript
{
  "text": "she sells sea shells at the seashore he sells sea seals at the seashore",
  "token": 846764,
  "words": [ "seashore", "he", "she", "at"]
}
```
where `words` is an array of excluded words.

`POST /validate` accepts data in `JSON` in the following format
```javascript
{
  "text": "the quick brown fox jumped over the lazy dog", 
  "token": "620770",
  "words": {
    "the": "2",
    "quick": "1",
    "jumped": "1",
    "over": "1",
    "dog": "1"
  }
}
```
and returns a status `200 OK` only iff all the following hold true
- `token` matches the response given to the client 
- `text` matches the response given to the client
- Word count in the `words` object is correct and **excludes** the words returned in the response to the client

In all other cases, a status of `400 Bad Request` is returned.

Below is a sample cURL request to `/validate'
```shell
curl -X POST -H "Content-Type:application/json" -d '{
  "text": "the quick brown fox jumped over the lazy dog", 
  "token": "620770",
  "words": {
    "the": "2",
    "quick": "1",
    "jumped": "1",
    "over": "1",
    "dog": "1"
  }
}' http://127.0.0.1:8000/validate
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

### Tests
The app contains both unit tests and integrations tests. To run simply type the following
```shell
$ ./run -test
```
An additional [Postman](http://getpostman.com) collection has been bundled in `tests/postman-test.json` which can be run the [Newman](https://www.npmjs.org/package/newman) - a node.js test runner that I built for postman. Here's the screenshot below of the output - 
![image](newman_results.png)
