# Database Design

The database separates authentication (`users`) from academic identity (`students` and `teachers`).

A student has:

- Internal database ID
- National University registration number
- Class roll
- Name
- Batch
- Year level
- Section

The class roll is used as the student-facing login username in the planned production workflow, while the NU registration number is retained as official academic identification.

## Core relationships

```text
users
  |
  +--- students
  |
  +--- teachers

students --- enrollments --- courses
teachers --- course_teachers --- courses

students --- attendance --- courses
teachers --------------------^

courses --- assignments --- submissions --- students

users --- announcements
users --- events
```

## Important design decision

The internal `id` is the primary database identity. Roll numbers and NU registration numbers are unique business identifiers, but they should not be used as database foreign keys.

This makes future changes to class rolls safer.
