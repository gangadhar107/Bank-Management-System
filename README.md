# BANK-MANAGEMENT-SYSTEM

## Overview

This project is a simple bank management system implemented in Python using MySQL as the database. The system allows users to sign up, sign in, and perform banking operations such as balance enquiry, deposit, withdrawal, and fund transfer. Each user has a unique account number and can perform transactions securely.

## Features

- **Database Operations**: Utilizes MySQL for data storage and retrieval.
- **Transaction Management**: Supports various banking operations.
- **Input Validation**: Ensures valid inputs and protects against SQL injection attacks.
- **Logging**: Tracks important events and debug information.
- **Efficient Processing**: Handles transactions in under 1 second, enhancing operational efficiency and customer satisfaction.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/gangadhar107/bank-management-system.git
   ```
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the MySQL database:
- Create a new MySQL database named `bms`.
- Update the `database.py` file with your database credentials or set the environment variables:
   ```sh
    export DB_HOST="your_host"
    export DB_USER="your_user"
    export DB_PASS="your_password"
    export DB_NAME="bms"
   ```

 ## USAGE
1. Run `main.py` to start the bank management system:
   ```sh
   python main.py
   ```
2. Choose the option to sign up or sign in.
3. Follow the on-screen instructions to perform banking operations.

 ## CONTRIBUTING
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature/new-feature
   ```
5. Submit a pull request.
