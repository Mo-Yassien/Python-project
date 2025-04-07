import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.reservation_id = None
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main container
        main_container = ttk.Frame(self, padding=20)
        main_container.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title_label = ttk.Label(main_container,
                              text="Edit Reservation",
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
        
        # Update button
        update_button = ttk.Button(buttons_frame,
                                 text="Update Reservation",
                                 command=self.update_reservation)
        update_button.grid(row=0, column=0, padx=10, ipadx=20, ipady=10)
        
        # Back button
        back_button = ttk.Button(buttons_frame,
                               text="Back to Reservations",
                               command=lambda: controller.show_frame("ReservationsPage"))
        back_button.grid(row=0, column=1, padx=10, ipadx=20, ipady=10)
    
    def load_reservation(self, reservation_id):
        self.reservation_id = reservation_id
        conn = database.create_connection()
        if conn is not None:
            reservation = database.get_reservation(conn, reservation_id)
            conn.close()
            
            if reservation:
                self.entries["name_entry"].delete(0, tk.END)
                self.entries["name_entry"].insert(0, reservation[1])
                
                self.entries["flight_entry"].delete(0, tk.END)
                self.entries["flight_entry"].insert(0, reservation[2])
                
                self.entries["departure_entry"].delete(0, tk.END)
                self.entries["departure_entry"].insert(0, reservation[3])
                
                self.entries["destination_entry"].delete(0, tk.END)
                self.entries["destination_entry"].insert(0, reservation[4])
                
                self.entries["date_entry"].delete(0, tk.END)
                self.entries["date_entry"].insert(0, reservation[5])
                
                self.entries["seat_entry"].delete(0, tk.END)
                self.entries["seat_entry"].insert(0, reservation[6])
    
    def update_reservation(self):
        try:
            if self.reservation_id is None:
                messagebox.showerror("Error", "No reservation selected")
                return
            
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
            
            # Create reservation tuple with ID
            reservation = (name, flight_number, departure, destination, date, seat_number, self.reservation_id)
            
            # Update in database
            conn = database.create_connection()
            if conn is not None:
                database.update_reservation(conn, reservation)
                conn.close()
                messagebox.showinfo("Success", "Reservation updated successfully!")
                self.controller.show_frame("ReservationsPage")
            else:
                messagebox.showerror("Error", "Could not connect to database")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}") 