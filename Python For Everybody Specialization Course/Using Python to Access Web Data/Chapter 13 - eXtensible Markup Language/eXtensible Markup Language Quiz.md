# eXtensible Markup Language Quiz

### 1. What is the anme of the Python 2.x library to parse XML data?
- [ ] xml.json
- [ ] xml-misc
- [ ] xml2
- [x] xml.etree.ElementTree

### 2. What is the method to cause Python to parse XML that is stored in a string?  
- [x] fromstring()
- [ ] parse()
- [ ] readall()
- [ ] extract()
- [ ] xpath()

### 3. In this XML, which are the "simple elements"?
```
<people>
    <person>
        <name>Chuck</name>
        <phone>303 4456</phone>
    </person>
    <person>
        <name>Noah</name>
        <phone>622 7421</phone>
    </person>
</people>
```
- [ ] people 
- [ ] person
- [ ] Noah
- [x] name
- [x] phone

### 4. In the following XML, which are attributes?
```
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>
```
- [x] hide 
- [ ] name
- [ ] email
- [ ] person
- [x] type

### 5. In the following XML, which node is the parent node of node e?
```
<a>
    <b>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
</a>
```
- [ ] b 
- [x] c
- [ ] e
- [ ] a

### 6. Looking at the following XML, what text value would we find at path "a/c/e"
```
<a>
    <b>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
</a>
```
- [ ] Y 
- [ ] a
- [ ] e
- [ ] b
- [x] Z

### 7. What is the purpose of XML Schema? 
- [ ] A Python program to transform XML files
- [ ] To complete SHA1 checksums on data to make sure it is not modified in transit
- [ ] To transfer XML data reliably during network outages
- [x] To establish a contract as to what is valid XML

### 8. If you were building an XML Schema and wanted to limit the values allowed in an *xs:string* field to only those in a particular list, what XML tag would you use in your XML Schema definition?  
- [ ] xs:enumeration
- [ ] xs:complexType
- [ ] xs:element
- [x] maxOccurs
- [ ] xs:sequence

### 9. What does the "Z" mean in this representation of a time:
```
2002-05-30T09:30:10Z
```
- [x] This time is in the UTC timezone
- [ ] The hours value is in the range 0-12
- [ ] The local timezone for this time is New Zealand
- [ ] This time is Daylight Savings Time

### 10. Which of the following dates is in ISO8601 format?  
- [ ] 05/30/2002
- [ ] 2002-May-30
- [ ] May 30, 2002
- [x] 2002-05-30T09:30:10Z 
