# AniTalk

A Anime Discussion Forum Web Application built using Django. The app allows users to create accounts, log in, create posts, and engage in discussions about anime. It also provides a set of REST APIs for third-party developers to extract information about animes, users, and messages.

## Live

The Web Application is hosted on Vercel and the postgres database is hosted on Railway.

[Live Website](ani-talk-phi.vercel.app)

## Demo Video


https://github.com/Nithin1729S/AniTalk/assets/78496667/520e17e7-670e-47c8-b7b8-519bed52cd01



[Watch the Demo Video on YouTube](https://www.youtube.com/watch?v=6c5A9ZEjpB8)


## Features

### Web Application
- **User Authentication**: Users can create accounts, log in, and log out using Django's built-in authentication system.
- **Forums and Topics**: Users can create topics and posts within forums. Only logged-in users can create, edit, or delete their posts and replies. CRUD Functions implemented.
- **User Engagement**: Other users can view and engage in discussions on various topics.
- **Models**: The app used 4 models ( Users, Forums, Topics, Message ) to support CRUD operations.
- **Frontend**: The frontend is designed using CSS.
- **Database**: The application uses PostgreSQL, hosted online by Railway.
- **Hosting**: The web application is hosted on Vercel.

### REST APIs
The application exposes several REST APIs that allow third-party developers to extract information from the system. These APIs provide information about animes, users, forums, topics, and messages.

#### Available Endpoints
- **GET /api**: Base endpoint.
- **GET /api/forums**: List all forums.
- **GET /api/forums/:id**: Retrieve a specific forum by ID.
- **GET /api/topics**: List all topics.
- **GET /api/topics/:id**: Retrieve a specific topic by ID.
- **GET /api/users**: List all users.
- **GET /api/users/:id**: Retrieve a specific user by ID.
- **GET /api/messages**: List all messages.
- **GET /api/messages/:id**: Retrieve a specific message by ID.


## Setup and Installation

1. **Clone the Repository**:
    ```bash
    https://github.com/Nithin1729S/AniTalk.git
    cd AniTalk
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Database**:
    - Set up PostgreSQL and update the `DATABASES` setting in `settings.py` with your database credentials. For better security use a .env file.
    - Or Use the local sqlite3 database by commenting out the above instruction related code in `settings.py` and uncomment sqlite3 related code.
4. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Using APIs

- **Access the Web App**: Open your web browser and go to `http://127.0.0.1:8000/` after installing the application.
- Or visit the live website.
- **Use the APIs**: Use the endpoints listed above to access the REST APIs.
- Ex: Use `http://127.0.0.1:8000/api/topics` to get a json data of all topics currently in the webapp.
    ```



