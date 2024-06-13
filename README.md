# AniTalk

A Anime Discussion Forum Web Application built using Django. The app allows users to create accounts, log in, create posts, and engage in discussions about anime. It also provides a set of REST APIs for third-party developers to extract information about animes, users, and messages.

## Live

The Web Application is hosted on Vercel and the postgres database is hosted on Railway.

[Live Website](https://ani-talk-phi.vercel.app)

## Demo Video





https://github.com/Nithin1729S/AniTalk/assets/78496667/6702e584-7210-46fc-bc78-24c231c574ae








[Watch the Demo Video on YouTube](https://youtu.be/uQ2E7DPgc2U)

## Screenshots

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/c4c5d09f-8b40-4fea-9d92-501c6cae3743)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/6033879f-9c89-4124-9167-c9c5cec8021d)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/36690997-acc9-48c2-9d3d-361ff372b989)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/9856a720-cf0d-4a8a-ba2e-0ef8a315682c)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/0fc58cdd-a8a9-4dd3-93d3-c389c9eb8a1f)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/f6983077-be4c-4ac6-9bb1-ee641b326f82)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/b7ba454d-5f05-47d9-9a5f-1d86955f6a02)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/63aa4342-18f2-4b43-b39a-8a1d3f9a4ed3)


![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/330b3d99-ba9e-4139-ad94-0491612848a3)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/016f723b-8304-4747-b72c-f438b7b097e3)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/24b7ed6d-04e6-4438-a7ad-7f3480582d51)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/b409634f-58a4-4d86-8f1c-ebf6a94904fe)

![image](https://github.com/Nithin1729S/AniTalk/assets/78496667/cbf4801e-a1d2-4929-94f3-ea3bfafaf25e)


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
- Ex: Use `http://127.0.0.1:8000/api/topics` if installed on a local machine to get a json data of all topics currently in the webapp.



