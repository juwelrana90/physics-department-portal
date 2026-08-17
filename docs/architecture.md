# System Architecture

## Initial architecture

```text
                    Physics Department Portal
                              |
                +-------------+-------------+
                |                           |
             Frontend                    Backend
                |                           |
        +-------+-------+              FastAPI
        |               |                  |
       Web           Flutter               |
                                      SQLAlchemy
                                           |
                                       PostgreSQL
```

## User roles

### Student
- View own profile
- View enrolled courses
- View own attendance
- View assignments
- Submit assignments
- View events
- View announcements

### Teacher
- View assigned courses
- Record attendance
- Create assignments
- Review submissions
- Publish course announcements

### Admin
- Manage users
- Manage students and teachers
- Manage courses and enrollments
- Manage department-wide events and announcements
- Reset accounts

## Security principles

1. Passwords are stored only as secure hashes.
2. JWTs are used for API authentication.
3. Authorization must be enforced server-side.
4. Students must never be able to modify their own attendance.
5. Students must only access resources they are authorized to access.
6. Production CORS origins must be restricted.
7. Secrets must live outside Git.
8. Real student data must never be committed to the repository.

## Future architecture

Chat, notifications, file storage, audit logs, and analytics will be added as separate modules so the initial system remains maintainable.
