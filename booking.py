import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main container
        main_container = ttk.Frame(self, padding=20)
        main_container.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title_label = ttk.Label(main_container,
                              text="Book a Flight",
                              font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Form fields
        fields = [
            ("Name", "name_entry"),
            ("Flight Number", "flight_entry"),
            ("Departure", "departure_entry"),
            ("Destination", "destination_entry"),
            ("Date (YYYY-MM-DD)", "date_entry"),
            ("Seat Number", "seat_entry")
        ]
        
        self.entries = {}
        for i, (label, entry_name) in enumerate(fields, start=1):
            ttk.Label(main_container, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(main_container)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries[entry_name] = entry
        
        # Buttons container
        buttons_frame = ttk.Frame(main_container)
        buttons_frame.grid(row=len(fields) + 1, column=0, columnspan=2, pady=20)
        
        # Submit button
        submit_button = ttk.Button(buttons_frame,
                                 text="Submit Reservation",
                                 command=self.submit_reservation)
        submit_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=10)
        
        # Back button
        back_button = ttk.Button(buttons_frame,
                               text="Back to Home",
                               command=lambda: controller.show_frame("HomePage"))
        back_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=10)
    
    def submit_reservation(self):
        try:
            # Get values from entries
            name = self.entries["name_entry"].get()
            flight_number = self.entries["flight_entry"].get()
            departure = self.entries["departure_entry"].get()
            destination = self.entries["destination_entry"].get()
            date = self.entries["date_entry"].get()
            seat_number = self.entries["seat_entry"].get()
            
            # Validate inputs
            if not all([name, flight_number, departure, destination, date, seat_number]):
                messagebox.showerror("Error", "Please fill in all fields")
                return
            
            # Create reservation tuple
            reservation = (name, flight_number, departure, destination, date, seat_number)
            
            # Save to database
            conn = database.create_connection()
            if conn is not None:
                database.create_reservation(conn, reservation)
                conn.close()
                messagebox.showinfo("Success", "Reservation created successfully!")
                self.controller.show_frame("HomePage")
            else:
                messagebox.showerror("Error", "Could not connect to database")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}") 