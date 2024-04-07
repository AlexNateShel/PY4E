### 1. What is the primary added value of relational databases over flat files?
- [ ] Ability to store data in a format that can be sent across a network
- [ ] Ability to execute Python code within the file
- [ ] Ability to execute JavaScript in the file
- [x] Ability to scan large amounts of data quickly
- [ ] Ability to quickly convert data to HTML

### 2. What is the purpose of a primary key?
- [ ] To look up a particular row in a table very quickly
- [x] To point to a particular row in another table
- [ ] To look up a row based on a string that comes from outside the program
- [ ] To track the number of duplicate values in another column

### 3. Which of the following is NOT a good rule to follow when developing a database model?
- [x] Use a person's email address as their primary key
- [ ] Model each "object" in the application as one or more tables
- [ ] Never repeat string data in more than one table in a data model
- [ ] Use integers as primary keys

### 4. If our user interface (i.e., like iTunes) has repeated strings on one column of the user interface, how should we model this properly in a database?
- [ ] Put the string in the first row where it occurs and then put NULL in all of the other rows
- [x] Make a table that maps the strings in the column to numbers and then use those numbers in the column
- [ ] Encode the entire row as JSON and store it in a TEXT column in the database
- [ ] Put the string in the first row where it occurs and then put that row number in the column of all of the rest of the rows where the string occurs
- [ ] Put the string in the last row where it occurs and put the number of that row in the column of all of the rest of the rows where the string occurs

### 5. Which of the following is the label we give a column that the "outside world" uses to look up a particular row?
- [ ] Primary key
- [ ] Remote key
- [x] Logical key
- [ ] Local key
- [ ] Foreign key

### 6. What is the label we give to a column that is an integer and used to point to a row in a different table?
- [ ] Local key
- [ ] Logical key
- [ ] Remote key
- [x] Foreign key
- [ ] Primary key

### 7. What SQLite keyword is added to primary keys in a CREATE TABLE statement to indicate that the database is to provide a value for the column when records are inserted?
- [ ] ASSERT_UNIQUE
- [ ] AUTO_INCREMENT
- [x] AUTOINCREMENT     
- [ ] INSERT_AUTO_PROVIDE

### 8. What is the SQL keyword that reconnects rows that have foreign keys with the corresponding data in the table that the foreign key points to?
- [x] JOIN
- [ ] APPEND
- [ ] COUNT
- [ ] CONNECT
- [ ] CONSTRAINT
 
### 9.What happens when you JOIN two tables together without an ON clause?
- [x] The number of rows you get is the number of rows in the first table times the number of rows in the second table
- [ ] The rows of the left table are connected to the rows in the right table when their primary key matches
- [ ] You get no rows at all
- [ ] Leaving out the ON clause when joining two tables in SQLite is a syntax error
- [ ] You get all of the rows of the left table in the JOIN and NULLs in all of the columns of the right table

### 10. When you are doing a SELECT with a JOIN across multiple tables with identical column names, how do you distinguish the column names?
- [ ] tablename['columnname']
- [x] tablename.columnname
- [ ] tablename/columnname
- [ ] tablename->columnname