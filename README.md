# phase-3-project
# Project Name

# Task Management CLI

This is a Command Line Interface (CLI) application for managing tasks. It allows users to create, delete, and view tasks.

## Installation

Before running the application, make sure you have Python installed on your system. You'll also need to install the following dependencies:

1. Click: 
   ```bash
   pip install Click
SQLAlchemy:

bash
Copy code
pip install sqlalchemy
Alembic:

bash
Copy code
pip install Alembic
Usage
Clone this repository to your local machine.

Navigate to the project directory.

Run the CLI application by executing the following command:

bash
Copy code
python src/cli.py
Follow the on-screen prompts to interact with the application.

Features
Create a Task: Allows users to create a new task.

Delete a Task: Allows users to delete an existing task.

Show All Tasks: Displays all tasks stored in the database.

Show a Specific Task: Shows details of a specific task.

Project Structure
src/: Contains the source code for the CLI application.
cli.py: Main entry point for the CLI application.
db.py: Database configuration and session management.
helpers.py: Helper functions for the CLI application.
models/: Directory containing database models.
__init__.py: Initialization file for the models package.
task.py: Defines the Task model.
Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

