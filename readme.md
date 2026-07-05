# Healthcare Backend API

A RESTful healthcare backend built using Django, Django REST Framework, PostgreSQL, and JWT authentication.

The application allows users to register, log in, manage patient and doctor records, and assign doctors to patients through patient-doctor mappings.

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* djangorestframework-simplejwt
* python-dotenv

## Project Structure

```text
healthcare_backend/
│
├── healthcare/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── user/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── patient/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── doctor/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── appointment/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Environment Configuration

Create a `.env` file in the project root directory.

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=your-database-name
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=127.0.0.1
DB_PORT=5432
```

## Database Setup

Make sure PostgreSQL is running and create a database for the application.

Then generate and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Authentication

The application uses JWT authentication.

After a successful login, the API returns a JWT token. Protected endpoints require the token in the request header.

```text
Authorization: Bearer <your-jwt-token>
```

## API Endpoints

### Authentication APIs

| Method | Endpoint                | Authentication | Description                   |
| ------ | ----------------------- | -------------- | ----------------------------- |
| POST   | `/api/auth/register/` | Public         | Register a new user           |
| POST   | `/api/auth/login/`    | Public         | Login and receive a JWT token |

### Patient APIs

| Method | Endpoint                | Authentication | Description                                    |
| ------ | ----------------------- | -------------- | ---------------------------------------------- |
| POST   | `/api/patients/`      | Required       | Create a new patient                           |
| GET    | `/api/patients/`      | Required       | Get patients created by the authenticated user |
| GET    | `/api/patients/<id>/` | Required       | Get a specific patient                         |
| PUT    | `/api/patients/<id>/` | Required       | Update a patient                               |
| DELETE | `/api/patients/<id>/` | Required       | Delete a patient                               |

### Doctor APIs

| Method | Endpoint               | Authentication | Description           |
| ------ | ---------------------- | -------------- | --------------------- |
| POST   | `/api/doctors/`      | Required       | Create a new doctor   |
| GET    | `/api/doctors/`      | Required       | Get all doctors       |
| GET    | `/api/doctors/<id>/` | Required       | Get a specific doctor |
| PUT    | `/api/doctors/<id>/` | Required       | Update a doctor       |
| DELETE | `/api/doctors/<id>/` | Required       | Delete a doctor       |

### Patient-Doctor Mapping APIs

| Method | Endpoint                        | Authentication | Description                                |
| ------ | ------------------------------- | -------------- | ------------------------------------------ |
| POST   | `/api/mappings/`              | Required       | Assign a doctor to a patient               |
| GET    | `/api/mappings/`              | Required       | Retrieve all patient-doctor mappings       |
| GET    | `/api/mappings/<patient_id>/` | Required       | Get doctors assigned to a specific patient |
| DELETE | `/api/mappings/<id>/`         | Required       | Remove a doctor from a patient             |

## Example API Requests

### Register User

```http
POST /api/auth/register/
Content-Type: application/json
```

```json
{
  "name": "Vinod Kumar",
  "email": "vinod@example.com",
  "password": "securepassword123"
}
```

### Login User

```http
POST /api/auth/login/
Content-Type: application/json
```

```json
{
  "email": "vinod@example.com",
  "password": "securepassword123"
}
```

Example response:

```json
{
  "message": "Login successful",
  "token": "your-jwt-token"
}
```

### Create Patient

```http
POST /api/patients/
Authorization: Bearer <your-jwt-token>
Content-Type: application/json
```

```json
{
  "name": "Rahul Kumar",
  "age": 25,
  "gender": "M",
  "address": "Bangalore",
  "phone": "9876543210"
}
```

### Create Doctor

```http
POST /api/doctors/
Authorization: Bearer <your-jwt-token>
Content-Type: application/json
```

```json
{
  "name": "Dr. Ravi Kumar",
  "email": "ravi.kumar@hospital.com",
  "phone": "9876543211",
  "specialization": "C"
}
```

### Assign Doctor to Patient

```http
POST /api/mappings/
Authorization: Bearer <your-jwt-token>
Content-Type: application/json
```

```json
{
  "patient": 1,
  "doctor": 2,
  "note": "Regular consultation"
}
```

## Data Relationships

The application follows these relationships:

```text
User
 ├── creates many Patients
 └── creates many Doctors

Patient
 └── has many Mappings/Appointments

Doctor
 └── has many Mappings/Appointments

Patient
   └── Mapping / Appointment
              └── Doctor
```

The `Appointment` model acts as the patient-doctor mapping entity required by the assignment.

## Author

Vinod Kumar
