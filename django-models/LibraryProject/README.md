# Deep Dive into Django Models and Views

This project is designed to solidify their understanding of Django’s ORM capabilities, view configurations, and user authentication features. Through a series of hands-on tasks, you will implement complex model relationships, develop both function-based and class-based views, and manage user authentication and permissions. 

**Objectives**

- Implement Advanced Model Relationships in Django.
- Develop Django Views and URL Configuration.
- Manage User Authentication in Django.
- Implement Role-Based Access Control in Django.
- Implement Custom Permissions in Django.

### [Task 0](https://github.com/MaryanneMuthoni/Alx_DjangoLearnLab/tree/main/django-models/LibraryProject/relationship_app): Implementing Advanced Model Relationships in Django

<ins>Objective:</ins>

Master Django’s ORM capabilities by creating a set of models that demonstrate the use of ForeignKey, ManyToMany, and OneToOne relationships.

<ins>Task Description:</ins>

Duplicate the previous project directory Introduction_ to_ Django, rename it to django-models and add a new app named relationship_app where you’ll define models that showcase complex relationships between entities using ForeignKey, ManyToMany, and OneToOne fields.

<ins>Steps:</ins>

1. Create the relationship_app App: Within your Django project directory, generate a new app: ```python3 manage.py startapp relationship_app```.
2. Define Complex Models in relationship_app/models.py:

- Author Model:
1. name: CharField.
- Book Model:
1. title: CharField.
2. author: ForeignKey to Author.
- Library Model:
1. name: CharField.
2. books: ManyToManyField to Book.
- Librarian Model:
1. name: CharField.
2. library: OneToOneField to Library.

3. Apply Database Migrations: Run migrations to create your model tables: ```python3 manage.py makemigrations relationship_app``` followed by ```python3 manage.py migrate```.
4. Implement Sample Queries: Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
- Query all books by a specific author.
- List all books in a library.
- Retrieve the librarian for a library.

**Repo:**

- GitHub repository: Alx_DjangoLearnLab
- Directory: django-models
- File: models.py, query_samples.py

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
