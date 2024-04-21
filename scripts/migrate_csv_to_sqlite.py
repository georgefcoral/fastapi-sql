# This script contains a logic for migrate CSV data to sqlite,  
# Actually, takes only the entity Restaurant,
# To do: Update the script for get external entity config, and get a general script.

import csv;
import sqlite3;

# Connecting to temporal DB, if db does not exist, creates a new on directory.

connection = sqlite3.connect('mydb.sqlite');

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition for entity Restaurant
create_table = '''CREATE TABLE Restaurant(
                id TEXT PRIMARY KEY,
                rating INTEGER ,
                name TEXT,
                site TEXT,
                email TEXT,
                phone TEXT,
                street TEXT,
                city TEXT,
                state TEXT,
                lat FLOAT,
                lng FLOAT);
                '''

# Creating the table into our 
# database
cursor.execute(create_table);


# Opening the restaurantes.csv file
file = open('restaurantes.csv');


# Reading the contents of the 
# restaurantes.csv file
contents = csv.reader(file)

next(contents)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO Restaurant (id,rating,name,site,email,phone,street,city,state,lat,lng) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

# Importing the contents of the file 
# into our person table
cursor.executemany(insert_records, contents);

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully 
# inserted into the table
select_all = "SELECT * FROM Restaurant";
rows = cursor.execute(select_all).fetchall();

# Output to the console screen
for r in rows:
    print(r);

# Committing the changes
connection.commit()

# closing the database connection
connection.close()


