# Reservation System API

A backend REST API for a multi-purpose reservation platform where users can book a wide range of spaces, including hotels, villas, inns, sports fields, game halls, meeting rooms, event venues, and amphitheaters.

This project is still under active development. Features listed in the Roadmap section are planned but not yet implemented.

## Tech Stack

- Django and Django REST Framework (DRF)
- PostgreSQL
- Django Cache Framework
- OAuth 2.0 (Google) with JWT
- Python 3.x

## Features

- Google OAuth login implemented using database and admin-based configuration (credentials are stored in the database and managed through the Django admin panel, so no sensitive keys are exposed in the public repository)
- JWT-based authentication for API access
- Multi-category reservations supporting different space types (hotel, villa, inn, sports field, game hall, meeting room, event venue, amphitheater, and more)
- Double booking prevention using database transactions to avoid overlapping reservations
- Transactional operations with transaction.atomic to ensure data integrity
- View caching using Django cache framework to improve performance
- Ordering, searching, filtering, and pagination on list endpoints using django-filter and DRF built-in tools

## Roadmap

- Google OAuth authentication
- JWT authentication
- Multi-category space reservation
- Double booking prevention with transactions
- View-level caching
- Ordering, searching, filtering, and pagination
- Payment integration
- Reviews and ratings
- Messaging system between users and hosts

## Contributing

This is a personal project, but suggestions and feedback are welcome. Feel free to open an issue.

## Author

Amirhossein Ranjbar

GitHub: https://github.com/Amirhossein-Ranjbar007