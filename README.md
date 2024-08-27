# Vehicle and Hotel Booking System

## Overview

This project is a Django-based web application designed to manage vehicle and hotel bookings. It allows users to sign up, log in, book vehicles and hotels, and view their booking history. Admins have additional capabilities to manage vehicles and hotels, including adding, updating, and deleting records. The system also tracks historical changes to vehicles and hotels.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Vehicle Management**: View available vehicles, book vehicles, and manage vehicle records (admin only).
- **Hotel Management**: View available hotels, book hotels, and manage hotel records (admin only).
- **Booking History**: View past vehicle and hotel bookings.
- **Admin Features**: Admins can add, update, and delete vehicles and hotels, and view historical changes.

## Setup

### Prerequisites

- Python 3.x
- Django 3.x or above
- A database (SQLite by default, but you can configure other databases)

### Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application** at `http://127.0.0.1:8000/`.

## Usage

### User Endpoints

- **Home Page**: `/` - Displays the home page.
- **Login Page**: `/login/` - Allows users to log in.
- **Signup Page**: `/signup/` - Allows users to sign up.
- **Vehicle Booking Page**: `/vehicle/` - Lists available vehicles.
- **Hotel Booking Page**: `/hotel/` - Lists available hotels.
- **Booking Logs Page**: `/logs/` - Displays user's booking history.

### Admin Endpoints

- **Add Vehicle**: `/addvehicle/` - Allows admins to add new vehicles.
- **Update Vehicle**: `/vehicle/update/<id>/` - Allows admins to update vehicle details.
- **Delete Vehicle**: `/vehicle/delete/<id>/` - Allows admins to delete vehicles.
- **Add Hotel**: `/addhotel/` - Allows admins to add new hotels.
- **Update Hotel**: `/hotel/update/<id>/` - Allows admins to update hotel details.
- **Delete Hotel**: `/hotel/delete/<id>/` - Allows admins to delete hotels.
- **Vehicle History**: `/vehiclehistory/` - Displays the history of vehicle changes.
- **Hotel History**: `/hotelhistory/` - Displays the history of hotel changes.

## Models

- **User**: Extends the default Django User model with additional fields if necessary.
- **Vehicle**: Represents vehicles available for booking.
- **VehicleBookings**: Represents vehicle booking records.
- **Hotel**: Represents hotels available for booking.
- **HotelBooking**: Represents hotel booking records.
- **VehicleHistory**: Tracks changes to vehicle multipliers.
- **HotelHistory**: Tracks changes to hotel pricing.

## Templates

The application uses the following templates:

- `addhotel.html`
- `addvehicle.html`
- `base.html`
- `bookinglogs.html`
- `hbform.html`
- `home.html`
- `hotel_update.html`
- `hotelbooking.html`
- `hotelhistory.html`
- `index.html`
- `login.html`
- `signup.html`
- `vbform.html`
- `vehicle_update.html`
- `vehiclebooking.html`
- `vehiclehistory.html`


