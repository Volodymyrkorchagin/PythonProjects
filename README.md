This is a web application built with Django that allows users to view, upload, like, and manage memes. The project demonstrates the use of Django models, views, templates, authentication, file uploads, and pagination.

## Features

- View a list of memes
- Pagination for meme browsing
- Upload new memes
- Like and unlike memes
- Delete memes
- User authentication (login/logout)
- Image upload and storage

## Technologies Used

- Python 3
- Django
- SQLite
- HTML/CSS
- Bootstrap (if used)

## Project Structure

project/
│
├── meme/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
│ └── templates/
│
├── media/
├── db.sqlite3
└── manage.py


## Database Model

| Field | Description |
|---------|------------|
| title | Meme title |
| image | Uploaded image |
| likes | Users who liked the meme |
| created_at | Creation date |
| created_by | Meme author |

## Installation

git clone <https://github.com/Volodymyrkorchagin/PythonProjects.git>

cd memes_project

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

## Future Improvements

User profiles
Comment system
Meme categories
Search functionality
REST API support
AJAX-based likes
