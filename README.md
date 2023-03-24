[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10547669&assignment_repo_type=AssignmentRepo)

## Database Query Using JSON

This project is used to query the database using json and duckdb.

## Project Structure

complete_database_project/  
│  
├── firebase_database/    
│  
|── localhost_database/  

## Project Structure Explanation

### localhost_database  

The localhost_database contains the files which performs the following operations

1. data_converter.py is used to read the csv file and create a database using sqlite3

2. main.py is a file which leverages the fastapi to build a server which runs in the local machine.This file loads the database into duckdb and listens at the localhost default port 8080.This file can receive json request at the http://127.0.0.1:8080/query location and it performs query on the database based on the json input and responds with json output  
  
3. example.json contains the json schema for the project.  
  
4. vision.py is used to send request to the server created at the localhost it reads the example.json file and sends it to the local server and prints the output  
  
5. requirements.txt contains all the python modules used in the project  
  
6. datasets folder contains the csv files for the project.data_converter.py uses the csv files in this folder to create the database
  
### Setting Up The Project

#### Prerequisites

You need a python environment with all the modules in the requirements.txt file installed in your system to run the project.The project is developed in linux operating system.Below are the steps to install the project in linux

#### Installation
1. Create a python environment using the command <code>python3 -m venv venv</code>  
2. Activate the python virtual environment with the command <code>source venv/bin/activate</code>  
3. Install all the required python modules using the command <code>pip install -r requirements.txt</code>  

#### Usage

1. To start using the project open the terminal and run <code>python3 data_converter.py</code>  
2. Then start the restapi using the command <code>uvicorn main:app --reload</code> which listens at the local ip address http://127.0.0.1:8080
3. Then run vision.py using the command <code>python3 vision.py</code> to send json request and to receive the response  

#### Built With
1. python
2. JSON
3. Fastapi
4. duckdb
5. sqlite3
6. pandas
7. requests


### firebase_database  

The firebase_database folder contains the files and folder whose uses are defined below  

firebase_database/  
├── app/  
│   ├── __init__.py  
│   ├── example.json  
│   ├── main.py  
│   └── reastapi-firebase-adminsdk-rby00-97aeff0c91.json    
├── datasets/  
├── Dockerfile  
├── firestore_write.py  
└── requirements.txt  
  
1. example.json contains the json schema for the project  
  
2. main.py creates api using fastapi  
  
3. reastapi-firebase-adminsdk-rby00-97aeff0c91.json is a file for firebase authentication.You can add your security key in this file to access your service accont.

4. datasets folder contains .csv files which is used to create database in the cloud  
  
5. Dockerfile contains the code to dockerize the project so that you can host it on cloudplatform easily  
  
6. requirements.txt contains all the python modules used in the project

7. firestore_write.py reads the csv files in the datasets folder and adds the data to the firebase database  
  
#### Prerequisites

You need a python environment with all the modules in the requirements.txt file installed in your system to run the project.The project is developed in linux operating system.Below are the steps to install the project in linux

#### Installation

1. Create a python environment using the command <code>python3 -m venv venv</code>  
2. Activate the python virtual environment with the command <code>source venv/bin/activate</code>  
3. Install all the required python modules using the command <code>pip install -r requirements.txt</code>  

#### Usage

1. To start using the project you need to run <code>python3 firestore_write.py</code> in the terminal which writes data to the firestore database
2. Then run <code>docker build -t myimage .</code> to create the container
3. Then run <code>docker run -d --name mycontainer -p 8080:80 myimage</code> to run the container in your local machine

you can deploy the container on any cloudplatform which supports docker

#### Built With
1. python
2. JSON
3. Fastapi
4. duckdb
5. sqlite3
6. pandas
7. requests
8. firebase-admin
9. Docker

## Houseware

### Company information 

Houseware's vision is to empower the next generation of knowledge workers by putting the data warehouse in their hands, in the language they speak. Houseware is purpose-built for the Data Cloud’s untouched creators, empowering internal apps across organizations. 

### Why participate in an Octernship with Houseware

Houseware is changing the way the data warehouse is leveraged, and we want you to help build Houseware! Our team came together to answer the singular question, "how can we flip the value of the data warehouse to the ones who really need it, to the ones who drive decisions". 

In this role, you'll have the opportunity to work as a Data engineer with the Houseware team on multiple customer-facing projects. You'd be involved with delivering the data platform for the end user, while taking complete ownership of engineering challenges - this would include communicating with the stakeholders, setting the right expectations, and ensuring top quality for the code & the product being shipped.

### Octernship role description

We're looking for data engineers to join the Houseware team. 

We are hell-bent on building a forward-looking product, something that constantly pushes us to think by first principles and question assumptions, building a team that is agile in adapting and ever curious. While fast-paced execution is one of the prerequisites in this role, equally important is the ability to pause and take stock of where product/engineering is heading from a long-term perspective. Your initiative is another thing that we would expect to shine through here, as you continuously navigate through ambiguous waters while working with vigor on open-ended questions - all to solve problems for and empathize with the end users.

| Octernship info  | Timelines and Stipend |
| ------------- | ------------- |
| Assignment Deadline  | 26 March 2023  |
| Octernship Duration  | 3-6 Months  |
| Monthly Stipend  | $600 USD  |

### Recommended qualifications

- You have a solid problem-solving framework.
- You are well-versed with the Modern Data Stack, and have worked with Cloud Data Warehouses before
- You have prior experience writing backend systems, and are proficient in SQL/dbt.

### Eligibility

To participate, you must be:

* A [verified student](https://education.github.com/discount_requests/pack_application) on Global Campus

* 18 years or older

* Active contributor on GitHub (monthly)

# Assignment

## Segment users on DuckMart!

### Task instructions

You have been given a task to segment the user audience for a fictional online service called "DuckMart". You have to design and implement a backend service that allows for segmenting the user audience based on user attributes and user events.

As part of this activity, you'll have to do the following
- Dummy data generation: Create dummy data using tools like Mockaroo
- Data transformation: Write a Python script to transform the data from the CSV files into a format suitable for loading into the database.
- Data loading: You are required to load the transformed data into DuckDB

Database Schema: The following are the requirements for the database schema:

- User Attributes: User ID, Name, Age, Gender, Location, Signup Date, Subscription Plan, Device Type.
- User Events: User ID, Event Name, Timestamp.

A few examples of events are "PURCHASE_MADE" or "ADDED_TO_CART".

Query Requirements: The following are the requirements for the queries:

- Segment users by age groups: Create a segment of users in the age range 25-34 years and list out the user IDs of all such users.
- Segment users by location and events: Create a segment of users whose location="California" and have logged in to the product at least once(event_name='LOGIN') and list out the User IDs of all such users.

You are then required to write out a backend API endpoint that can scale to any kind of "Segmentation usecase" like the two examples mentioned above. Building on top of the mentioned data schema(Users, Events), the consumer of this API should be able to specify the segmentation criteria in a JSON-like format and the backend API should be able to convert it into the relevant SQL. Please specify what the spec for the JSON-like payload looks like.

### Task Expectations

You will be evaluated based on the following criteria:
- Correctness and completeness of the implementation.
- The JSON spec that powers the "Segmentation API"
- Performance and scalability of the implementation.
- Quality of the SQL queries and their optimization.
- Quality of the code and documentation.
- Ability to explain and justify design decisions.

### Task submission

Students are expected to use the [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow) when working on their project. 

1. Please push your final code changes to your main branch
2. Please add your instructions/assumptions/any other remarks in the beginning of the Readme file and the reviewers will take a look
3. The PR created called Feedback will be used for sharing any feedback/asking questions by the reviewers, please make sure you do not close the Feedback PR.
4. The assignment will be automatically submitted on the "Assignment Deadline" date -- you don't need to do anything apart from what is mentioned above.
5. Using GitHub Issues to ask any relevant questions regarding the project


