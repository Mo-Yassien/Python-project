import os
import shutil
import zipfile

def create_package():
    # Create a temporary directory for packaging
    package_dir = "FlightReservationSystem_Package"
    os.makedirs(package_dir, exist_ok=True)
    
    # Copy source files
    source_files = [
        "main.py",
        "database.py",
        "home.py",
        "booking.py",
        "reservations.py",
        "edit_reservation.py",
        "requirements.txt",
        "README.md"
    ]
    
    for file in source_files:
        if os.path.exists(file):
            shutil.copy2(file, os.path.join(package_dir, file))
    
    # Copy executable
    if os.path.exists("dist/FlightReservationSystem.exe"):
        os.makedirs(os.path.join(package_dir, "dist"), exist_ok=True)
        shutil.copy2("dist/FlightReservationSystem.exe", 
                    os.path.join(package_dir, "dist/FlightReservationSystem.exe"))
    
    # Create zip file
    with zipfile.ZipFile("FlightReservationSystem.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arcname)
    
    # Clean up temporary directory
    shutil.rmtree(package_dir)
    print("Package created successfully: FlightReservationSystem.zip")

if __name__ == "__main__":
    create_package() 