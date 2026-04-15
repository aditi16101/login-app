# Login-Register Application

A full-stack web application for user authentication with login and registration features.

## Project Structure

```
login-app/
├── backend/           # FastAPI backend server
├── frontend/          # HTML/CSS/JavaScript frontend
└── README.md          # This file
```

## Backend Setup

The backend is built with FastAPI and uses SQLite for data storage.

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Backend

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

- **POST** `/api/register` - Register a new user
- **POST** `/api/login` - Login user
- **GET** `/api/verify-token` - Verify JWT token

## Frontend Setup

The frontend is a static site with vanilla JavaScript.

### Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Open `index.html` in a web browser or use a local server:
   ```bash
   # Using Python 3
   python -m http.server 8080
   ```

3. Access the application at `http://localhost:8080`

## Features

- User Registration with email validation
- User Login with JWT tokens
- Secure password hashing with bcrypt
- Protected dashboard after login
- Session management with localStorage
- Responsive UI design

## Security Notes

⚠️ **Important**: This is a learning project. For production use:
- Change the `SECRET_KEY` in `app/auth.py`
- Use environment variables for sensitive data
- Enable HTTPS
- Implement rate limiting
- Add CSRF protection
- Use secure cookie settings

## Technologies Used

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- Passlib (password hashing)
- PyJWT (JWT tokens)
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)
- Fetch API

## Future Enhancements

- Email verification
- Password reset functionality
- User profile page
- Two-factor authentication
- Social login (Google, GitHub)
- Database migrations
- Unit testing

## License

MIT
