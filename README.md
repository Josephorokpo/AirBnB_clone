#AirBnB Clone Command Interpreter
***ALX Software Engineering Team Project***

#Background Context
Welcome to the AirBnB clone project!

#Project Description
The goal of this project is to build a command interpreter for managing AirBnB objects. This is the initial step towards creating a full web application, involving subsequent tasks such as HTML/CSS templating, database storage, API, and front-end integration.

#Key Objectives:
- Implement a parent class (BaseModel) for the initialization, serialization, and deserialization of future instances.
- Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
- Create classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
- Develop the first abstracted storage engine: File storage.
- Create unit tests to validate all classes and the storage engine.

#Command Interpreter
Command Interpreter allows us to manage the objects in our AirBnB project. The command interpreter enables the following actions:

- Create: Generate a new object (e.g., a User or a Place).
- Retrieve: Obtain an object from a file, a database, etc.
- Operations: Perform operations on objects, such as counting, computing stats, etc.
- Update: Modify attributes of an object.
- Destroy: Delete an object.

#How to Start

1. Clone the repository: 
	- git clone https://github.com/your-username/AirBnB-Clone.git
	- cd AirBnB-Clone

2. Run the command interpreter:
	- ./console.py

#How to Use

The command interpreter provides a set of commands to interact with the AirBnB objects. Here are some examples:

> Create a new User:
	create User

> Retrieve an object:
	show User 1234-5678

> Perform operations:
	all Place

> Update attributes:
	update User 1234-5678 email "new.email@example.com"

> Destroy an object:
	destroy Place 8765-4321

#Examples

> Creating a User:	
	(hbnb) create User

> Retrieving an object:	
	(hbnb) show Place 9876-5432

> Listing all objects of a specific type:	
	(hbnb) all State

> Updating an attribute:	
	(hbnb) update User 1234-5678 first_name "John"

> eleting an object:
	(hbnb) destroy Place 8765-4321

#For a complete list of commands, type help within the command interpreter.

#File Structure

Repo: AirBnB_clone
	- README.md
	- AUTHORS
	- tests/test_models
		- test_...
		- test_console.py
	- models/
		- base_model.py
		- __init__.py
		- user.py
		- state.py
		- city.py
		- amenity.py
		- place.py
		- review.py
		- engine/
			- __init__.py
			- file_storage.py
	- console.py

#Contributors:

- Joseph Orokpo

- Salah Eddine Ait Si Ahmad
