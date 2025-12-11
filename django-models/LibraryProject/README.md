# Introduction to Django
This project is about Django, one of the most popular web frameworks for building robust web applications. It involves: setting up a Django development environment, learning about Django models and ORM, and exploring the Django admin interface.

**Objectives**

- Set Up Django Development Environment.
- Implementing and Interacting with Django Models.
- Utilizing the Django Admin Interface.

### [Task 0](https://github.com/MaryanneMuthoni/Alx_DjangoLearnLab/tree/main/Introduction_to_Django/LibraryProject): Introduction to Django Development Environment Setup

<ins>Objective:</ins>

Gain familiarity with Django by setting up a Django development environment and creating a basic Django project. This task aims to introduce you to the workflow of Django projects, including project creation and running the development server.

<ins>Task Description:</ins>

Install Django and create a new Django project named LibraryProject. This initial setup will serve as the foundation for developing Django applications. You’ll also explore the project’s default structure to understand the roles of various components.

<ins>Steps:</ins>

1. Install Django:
2. Ensure Python is installed on your system.
3. Install Django using pip: ```pip install django```.
4. Create Your Django Project: Create a new Django project by running: ```django-admin startproject LibraryProject```.
5. Run the Development Server: Navigate into your project directory (cd LibraryProject). Create a README.md file inside the LibraryProject. Start the development server using: ```python manage.py runserver```. Open a web browser and go to http://127.0.0.1:8000/ to view the default Django welcome page.
6. Explore the Project Structure: Familiarize yourself with the created project structure. Pay particular attention to: settings.py: Configuration for the Django project. urls.py: The URL declarations for the project; a “table of contents” of your Django-powered site. manage.py: A command-line utility that lets you interact with this Django project

**Repo:**

- GitHub repository: Alx_DjangoLearnLab
- Directory: Introduction_to_Django

### [Task1](https://github.com/MaryanneMuthoni/Alx_DjangoLearnLab/tree/main/Introduction_to_Django/LibraryProject/bookshelf): Implementing and Interacting with Django Models

<ins>Objective:</ins>

Demonstrate proficiency in Django by creating a Book model within a Django app, implementing it according to specified attributes, and using Django’s ORM to perform database operations.

<ins>Task Description:</ins>

For this task, you will develop a Django app named bookshelf within your existing Django project. You will define a Book model with specific attributes and demonstrate basic CRUD operations through the Django shell. This task is structured to ensure consistent implementations suitable for automated checking.

<ins>Steps:</ins>

1. Create the bookshelf App: In your Django project directory, use Django’s command-line utility to generate a new app: ```python manage.py startapp bookshelf```.
2. Define the Book Model: Navigate to bookshelf/models.py. Create a Book class with the following fields:
- title: CharField with a maximum length of 200 characters.
- author: CharField with a maximum length of 100 characters.
- publication_year: IntegerField.
Ensure the model is correctly set up for migrations.
3. Model Migration: Prepare your model for database integration by running ```python manage.py makemigrations``` bookshelf to create migration files. Apply migrations to update the database with ```python manage.py migrate```.
4. Interact with the Model via Django Shell: Open the Django shell with ```python manage.py shell``` and execute CRUD operations:
- Create a Book instance.
- Retrieve the book you created.
- Update the title of the created book.
- Delete the book instance.
5. Perform Specific CRUD Operations in the Django Shell: - Document each operation in separate Markdown files (create.md, retrieve.md, update.md, delete.md) detailing both the Python command used and its output.

<ins>Detailed CRUD Operations and Documentation:</ins>

- Create:

1. Command: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
2. Document in: create.md
3. Expected Documentation: Include the Python command and a comment with the expected output noting the successful creation. Retrieve:

- Retrieve:

1. Command: Retrieve and display all attributes of the book you just created.
2. Document in: retrieve.md
3. Expected Documentation: Include the Python command and a comment with the expected output showing the details of the book. Update:

- Update:

1. Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
2. Document in: update.md
3. Expected Documentation: Include the Python command and a comment with the expected output showing the updated title. Delete:

- Delete:

1. Command: Delete the book you created and confirm the deletion by trying to retrieve all books again.
2. Document in: delete.md
3. Expected Documentation: Include the Python command and a comment with the expected output confirming the deletion.

<ins>Implementation and Submission Instructions:</ins>

- Code Implementation: Your models.py file should correctly define the Book model as specified. Ensure that all field types and options are accurately implemented.

- Database Operations: Perform and document each CRUD operation in the Django shell. Save your commands and their outputs in a file named CRUD_operations.md.

**Repo:**

- GitHub repository: Alx_DjangoLearnLab
- Directory: Introduction_to_Django

### [Task 2](https://github.com/MaryanneMuthoni/Alx_DjangoLearnLab/blob/main/Introduction_to_Django/LibraryProject/bookshelf/admin.py): Utilizing the Django Admin Interface

<ins>Objective:</ins>

Gain practical experience with the Django admin interface by configuring the admin to manage the Book model. This task will demonstrate how to use Django’s built-in admin interface to perform data management tasks efficiently.

<ins>Task Description:</ins>

Enhance your bookshelf app by integrating the Book model with the Django admin interface. Customize the admin display to improve the management and visibility of book data, and document the process to ensure consistent setup and configuration.

<ins>Steps:</ins>

1. Register the Book Model with the Django Admin:
2. Modify bookshelf/admin.py to include the Book model, enabling admin functionalities for it.

<ins>Customize the Admin Interface:</ins>

- Implement custom configurations to display title, author, and publication_year in the admin list view.
- Configure list filters and search capabilities to enhance the admin’s usability for Book entries.

**Repo:**

- GitHub repository: Alx_DjangoLearnLab
- Directory: Introduction_to_Django
