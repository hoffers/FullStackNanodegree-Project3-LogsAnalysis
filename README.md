##Logs Analysis Project

###How to run it?

First, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
You will need to unzip this file after downloading it. The file inside is called newsdata.sql.

To load the data in your PostgreSQL database server, use the command `psql -d news -f newsdata.sql`.

Lastly, simply run `python report.py`.

###What's it do?

The Python script will connect to the news database, which contains 3 tables: authors, articles, and log. It will execute SQL 
queries to answer the following 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Sample output is in Output.txt.