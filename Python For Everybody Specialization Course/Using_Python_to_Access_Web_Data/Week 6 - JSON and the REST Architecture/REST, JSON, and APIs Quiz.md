# REST, JSON, and APIs Quiz PY4E

### 1. Who is credited with getting the JSON movement started?
- [ ] Bjarne Stroustrup
- [ ] Mitchell Baker
- [ ] Pooja Sankar
- [x] Douglas Crockford

### 2. What Python library do you have to import to parse and handle JSON?
- [ ] BeautifulSoup
- [ ] import re
- [ ] ElementTree
- [x] import json

### 3. Which of the following is a web services approach used by the Twitter API?   
- [ ] json.read() 
- [ ] json.loads()
- [ ] json.parse()
- [ ] json.connect()


### 4. What kind of variable will you get in Python when the following JSON is parsed:
```
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}
```  
- [x] A list with three items
- [ ] A dictionary with three key / value pairs
- [ ] A dictionary with one key / value pair
- [ ] Three tuples
- [ ] One tuple

### 5. Which of the following is not true about the service-oriented approach?
- [ ] An application makes use of the services provided by other applications
- [ ] Web services and APIs are used to transfer data between applications
- [ ] Standards are developed where many pairs of applications must work together
- [ ] An application runs together all in one place 

### 6. Which of these two web service approaches is preferred in most modern service-oriented applications?
- [ ] SOAP - Simple Object Access Protocol
- [x] REST - Representational state transfer


### 7. What library call do you make to append properly encoded parameters to the end of a URL like the following:
```
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
```
- [ ] re.match()
- [ ] urllib.parse.urlencode()
- [ ] re.encode()
- [ ] urllib.urlcat()

### 8. What happens when you exceed the Google geocoding API rate limit? 
- [ ] You cannot use the API until you respond to an email that contains a survey question
- [ ] Your application starts to perform very slowly
- [x] You cannot use the API for 24 hours
- [ ] The API starts to perform very slowly

### 9. What protocol does Twitter use to protect its API?
- [ ] PKI-HMAC
- [ ] Java Web Tokens
- [ ] SHA1-MD5
- [ ] SOAP
- [x] OAuth
- [ ] WS*Security

### 10. What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?
- [ ] content-type
- [ ] x-max-requests
- [ ] x-request-count-down
- [x] x-rate-limit-remaining
