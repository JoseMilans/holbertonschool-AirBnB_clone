# AirBnB clone - The console

## Table of Contents
1. [AirBnB Clone Project](#airbnb-clone-project)
2. [Command Interpreter Description](#command-interpreter-description)
3. [How to start it](#how-to-start-it)
4. [File Descriptions](#file-descriptions)
5. [console.py](#consolepy)
6. [Project Requirements](#project-requirements)
7. [Testing](#testing)
8. [AUTHORS](#authors)

## AirBnB Clone Project

This repository contains the implementation of a simplified AirBnB web application. This project serves as a learning platform for the basics of web development, particularly focusing on the backend aspects using Python.

## Command Interpreter Description

The command interpreter is a shell-like interface that allows us to manage the underlying data of the application.

### How to start it:

1. Navigate to the root directory of the repository.
2. Run the file `console.py` using Python:

### File Descriptions

|File|Description|
|---|---|
|[README.md]()|Project details|
|[AUTHORS]()|Contributors|
|[base_model.py]()|Contains the `BaseModel` class which serves as the foundation for all other models in the AirBnB project. It defines common attributes/methods, including saving, converting to dictionary format and generating unique IDs.|
|[__init__.py]()|Initialises the storage engine of the application, loading previously saved data if it exists.|
|[file_storage.py]()|This class, `FileStorage`, manages the serialisation and deserialisation of all instances to and from a JSON formatted file. It stores, retrieves and saves objects.|
|[test_base_model.py]()|Unit tests for the `BaseModel` class to ensure every method and functionality works as expected. The tests ensure that instances are created properly, the `to_dict()` method returns the correct dictionary representation, and so on.|
|[console.py]()|Contains the entry point of the command interpreter|

## console.py
### How to use it:

After starting the command interpreter, you can use the following commands:
- `create`: Create a new object.
- `show`: Show an object based on its ID.
- `update`: Update attributes of an object.
- `destroy`: Destroy an object.
- `all`: Display all objects.
- `quit`: Exit the command interpreter.

### Examples:

$ ./console.py
(hbnb) create User
246c227a-d5c1-403d-9cc7-829839a72403
(hbnb) show User 246c227a-d5c1-403d-9cc7-829839a72403
[User] (246c227a-d5c1-403d-9cc7-829839a72403) {'id': '246c227a-d5c1-403d-9cc7-829839a72403'}
(hbnb) quit
$

### Project Requirements:

- Python3 (version 3.8.5)
- Flask

### Testing

All code is unittest compliant. Run the following command to run tests:
`python3 -m unittest discover tests`

### AUTHORS

This section contains a list of contributors to this repository. For a more detailed list, please refer to the `AUTHORS` file at the root of this repository.

- Jose Milans <6764@holbertonstudents.com>
- Diego Piñeyro <6237@holbertonstudents.com>
