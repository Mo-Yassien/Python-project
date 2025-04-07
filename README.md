# Flight Reservation System

A desktop application for managing flight reservations, built with Python and Tkinter.

## Features

- Create new flight reservations
- View all existing reservations
- Edit existing reservations
- Delete reservations
- Simple and intuitive user interface
- SQLite database for data storage

## Requirements

- Python 3.8 or higher
- Required Python packages (automatically installed via requirements.txt):
  - tkinter (usually comes with Python)
  - sqlite3 (usually comes with Python)

## Installation

### Option 1: Using the Executable (Recommended for End Users)

1. Download the `FlightReservationSystem.zip` file
2. Extract the contents to your desired location
3. Navigate to the `dist` folder
4. Run `FlightReservationSystem.exe`

### Option 2: Running from Source Code

1. Clone or download the repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Home Page
- Click "Book a Flight" to create a new reservation
- Click "View Reservations" to see all existing reservations

### Booking a Flight
1. Fill in all required fields:
   - Name
   - Flight Number
   - Departure
   - Destination
   - Date (YYYY-MM-DD format)
   - Seat Number
2. Click "Submit Reservation"
3. You'll receive a confirmation message upon success

### Managing Reservations
- View all your reservations in a table format
- Select a reservation to edit or delete
- Use the "Refresh" button to update the list
- Click "Back to Home" to return to the main menu

### Editing a Reservation
1. Select a reservation from the list
2. Click "Edit"
3. Modify the desired fields
4. Click "Update Reservation" to save changes

### Deleting a Reservation
1. Select a reservation from the list
2. Click "Delete"
3. Confirm the deletion when prompted

## Database

The application uses SQLite for data storage. The database file (`reservations.db`) is automatically created in the same directory as the application when you first run it.

## Troubleshooting

If you encounter any issues:

1. Make sure all required Python packages are installed
2. Check that you have write permissions in the application directory
3. Verify that the database file is not corrupted
4. Try running the application with administrator privileges if needed

## Support

For support or to report issues, please contact the development team.

## License

This project is licensed under the MIT License - see the LICENSE file for details. # Python-project
