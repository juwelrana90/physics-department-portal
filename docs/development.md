# Development Workflow

## Branches

Recommended:

```text
main
develop
feature/<feature-name>
```

Examples:

```text
feature/authentication
feature/student-dashboard
feature/attendance
feature/assignments
```

## Milestones

1. Project foundation
2. Authentication and roles
3. Student dashboard
4. Teacher dashboard
5. Admin dashboard
6. Attendance
7. Assignments
8. Events and announcements
9. Notifications
10. Chat
11. Deployment and security review

## Before real deployment

The project must add:

- Alembic migrations
- Production secrets management
- Restricted CORS
- Rate limiting
- Audit logging
- Automated backups
- HTTPS
- Strong password policy
- Account recovery
- Comprehensive authorization tests
- Privacy/data retention policy
