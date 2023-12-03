# Dynamix: Dockerized CRUD with DynamoDB & Flask

Welcome to Dynamix – a dynamic and agile CRUD application leveraging the power of Docker, Python Flask, and Amazon DynamoDB.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Dynamix is your all-in-one solution for building, managing, and deploying containerized applications. This project demonstrates the fusion of cutting-edge technologies – Docker for containerization, Python Flask for the web application, and DynamoDB for scalable NoSQL database operations.

## Features

- **DynamoDB Integration:** Seamlessly interact with DynamoDB using the powerful `boto3` library.
- **RESTful API:** Create, read, update, and delete operations via well-defined Flask endpoints.
- **Containerized Environment:** Utilize Docker to encapsulate the entire application stack.

## Installation

1. **Prerequisites:**
   - Ensure Docker is installed on your system. Download it from the [official website](https://www.docker.com/products/docker-desktop).
   - Obtain DynamoDB Local [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) for local emulation.

2. **Setup:**
   - Clone this repository to your local machine.

## Usage

### Getting Started
1. Navigate to the project directory.
2. Execute Docker Compose:
    ```bash
    docker-compose up --build
    ```
3. Access the application at `http://localhost:5000`.

## Contributing

We welcome contributions to enhance Dynamix! Feel free to fork this repository, make changes, and submit pull requests.


