# DynamoDB Dockerized CRUD Application

![Project Image](<link to project image>)

A Dockerized CRUD application utilizing Amazon DynamoDB and Python Flask.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This repository hosts a Dockerized application built with Python Flask, demonstrating CRUD functionalities using Amazon DynamoDB as the database. This project aims to provide an easy-to-deploy solution for managing data with DynamoDB in a containerized environment.

![Demo Gif](<link to demo gif>)

---

## Features

- **Dockerized Environment**: Utilize Docker to ensure consistency and portability across different environments.
- **Python Flask**: Implement a RESTful API framework to interact with DynamoDB.
- **Amazon DynamoDB**: Use DynamoDB for storing and managing data.
- **CRUD Operations**: Implement Create, Read, Update, and Delete functionalities.
- **Scalability**: Leverage DynamoDB's scalability for efficient data handling.

---

## Prerequisites

Make sure you have the following installed before setting up the project:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Python](https://www.python.org/downloads/) (if not included in your system)

---

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository link>
   cd <project directory>
Environment Variables:

Create a .env file with the necessary environment variables:

bash
Copy code
# DynamoDB Configuration
DYNAMODB_ACCESS_KEY_ID=<Your Access Key ID>
DYNAMODB_SECRET_ACCESS_KEY=<Your Secret Access Key>
DYNAMODB_REGION=<Your DynamoDB Region>
Build and Run the Docker Container:

bash
Copy code
docker-compose up --build
Usage
Access the Flask application at http://localhost:5000 to perform CRUD operations on DynamoDB.

Available Endpoints:
GET /items: Retrieve all items.
GET /items/<id>: Retrieve a specific item.
POST /items: Create a new item.
PUT /items/<id>: Update an existing item.
DELETE /items/<id>: Delete an item.
Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or feature additions.

