# Blog_app

## Project Overview

**Blog_app** is a simple and powerful blogging platform built using Django and PostgreSQL. The app allows users to create, edit, and delete blog posts and provides a seamless user experience with Tailwind CSS. This project also demonstrates API integration using Django Rest Framework (DRF) and includes Docker setup for easy deployment.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
  - [Pre-requisites](#pre-requisites)
  - [Installation Steps](#installation-steps)
- [Running the Application](#running-the-application)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)
- [API Documentation](#api-documentation)
## Setup and Installation

### Pre-requisites

Make sure you have the following installed on your machine:

- Python 3.10+
- PostgreSQL
- Docker (for containerized deployment)
- Git

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Blog_app.git
   cd Blog_app/blog_project
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv virt
   source virt/bin/activate   # For Linux/Mac
   virt\Scripts\activate      # For Windows
   ```

3. **Install dependencies:**

   Install required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the project root directory and add the following:

   ```bash
   DJANGO_SECRET_KEY='your_secret_key'
   POSTGRES_DB=blog_application_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=hclpd
   ```

5. **Setup the database:**

   Ensure PostgreSQL is running, then create the database:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for the admin panel:**

   ```bash
   python manage.py createsuperuser
   ```

---

## Running the Application

### Running Locally

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the application:**

   Open a browser and navigate to: `http://127.0.0.1:8000`

3. **Admin Panel:**

   The Django admin panel is available at: `http://127.0.0.1:8000/admin`

---

### Running with Docker

1. **Build the Docker containers:**

   Make sure Docker is installed, then run:

   ```bash
   docker-compose build
   ```

2. **Run the containers:**

   Start the app and database containers:

   ```bash
   docker-compose up
   ```

3. **Access the application:**

   Visit `http://localhost:8000` in your browser.

---

## API Documentation

This project provides a REST API using Django Rest Framework (DRF). Below are the key endpoints:

### Blog Post Endpoints

1. **List all blog posts:**

   - URL: `/api/posts/`
   - Method: `GET`

2. **Create a new blog post:**

   - URL: `/api/posts/`
   - Method: `POST`
   - Request Body:

     ```json
     {
       "title": "New Blog Post",
       "content": "This is the content of the blog post."
     }
     ```

3. **Retrieve a specific blog post:**

   - URL: `/api/posts/<id>/`
   - Method: `GET`

4. **Update a specific blog post:**

   - URL: `/api/posts/<id>/`
   - Method: `PUT`
   - Request Body:

     ```json
     {
       "title": "Updated Title",
       "content": "Updated content."
     }
     ```

5. **Delete a blog post:**

   - URL: `/api/posts/<id>/`
   - Method: `DELETE`

---

## Delployment 

url - https://blogproject-omega.vercel.app/
# Note - The tailwind is not being rendered due to some issues 


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.



