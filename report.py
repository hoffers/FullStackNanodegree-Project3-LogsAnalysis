#!/usr/bin/env python2.7
import psycopg2

conn = psycopg2.connect("dbname=news")
cur = conn.cursor()

print "What are the most popular three articles of all time?"
top_articles = "select r.title, count(*) as views from \
               (select substring(l.path from '/([^/]+$)') as slug, l.* from \
               log l) as v join articles as r on r.slug = v.slug \
               join authors as a on r.author = a.id \
               where length(v.path) > 1 group by r.title order by views desc;"
cur.execute(top_articles)
results = cur.fetchmany(3)
for result in results:
    print " - \"" + str(result[0]) + "\" - " + str(result[1]) + " views"

print "Who are the most popular article authors of all time?"
top_authors = "select a.name, count(*) as views from \
              (select substring(l.path from '/([^/]+$)') as slug, l.* \
              from log l) as v join articles as r on r.slug = v.slug \
              join authors as a on r.author = a.id where length(v.path) > 1 \
              group by a.name order by views desc;"
cur.execute(top_authors)
results = cur.fetchall()
for result in results:
    print " - " + str(result[0]) + " - " + str(result[1]) + " views"

print "On which days did more than 1% of requests lead to errors?"
bad_days = "select day, percent from \
           (select err_tbl.day, err_tbl.errors, all_tbl.all, \
           round(((err_tbl.errors/all_tbl.all::float)*100.0)::numeric, 2) \
           as percent from (select count(*) as errors, \
           to_char(time, 'YYYY-MM-DD') as day from log \
           where status = '404 NOT FOUND' group by day) as err_tbl \
           join (select count(*) as all, to_char(time, 'YYYY-MM-DD') as day \
           from log group by day) as all_tbl on err_tbl.day = all_tbl.day) \
           as data where percent > 1;"
cur.execute(bad_days)
results = cur.fetchall()
for result in results:
    print " - " + str(result[0]) + " - " + str(result[1]) + "% errors"

cur.close()
conn.close()
