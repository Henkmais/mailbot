import subprocess

def run_getymal_script():
    subprocess.run(["python3", "getymal.py"])

def run_mail_script():
    subprocess.run(["python3", "mail.py"])

def run_delete_files_script():
    subprocess.run(["python3", "deletefiles.py"])

if __name__ == "__main__":
    try:
        # Run the getymal script
        getymal_process = subprocess.Popen(["python3", "getymal.py"])
        getymal_process.wait()  # Wacht tot getymal-script is voltooid

        # Run the mail script
        mail_process = subprocess.Popen(["python3", "mail.py"])
        mail_process.wait()  # Wacht tot mail-script is voltooid
        
        # Run the delete files script
        delete_files_process = subprocess.Popen(["python3", "deletefiles.py"])
        delete_files_process.wait()  # Wacht tot deletefiles-script is voltooid

    except FileNotFoundError:
        print("Error: Een of beide scripts (getymal.py of mail.py) niet gevonden.")
    except Exception as e:
        print(f"Fout: {e}")
