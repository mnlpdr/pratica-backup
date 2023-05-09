from datetime import datetime
import os

def backup_full_directory():
    print("Backup full directory")
    source = input("Enter the directory you want to backup: ")
    target = input("Enter the directory you want to backup to: ")
    if os.path.exists(source) and os.path.exists(target):
        for file in os.listdir(source):
            if os.path.isfile(os.path.join(source, file)):
                os.system("cp " + os.path.join(source, file) + " " + target)
        with open(os.path.join(target, "backup_log.txt"), "w") as log:
            log.write(f"""Backup completed successfully!
            Backup time: {datetime.now()}
            Backup source: {source}
            Files backed up: {os.listdir(source)}
            """)
        print("Backup completed successfully!")
    else:
        print ("Invalid directory.")

def backup_single_file():
    print("Backup single file")
    source = input("Enter the file you want to backup: ")
    target = input("Enter the directory you want to backup to: ")
    if os.path.exists(source) and os.path.exists(target):
        os.system("cp " + source + " " + target)
        with open(os.path.join(target, "backup_log.txt"), "w") as log:
            log.write(f"""Backup completed successfully!
            Backup time: {datetime.now()}
            Backup source: {source}
            """)
        print("Backup completed successfully!")
    else:
        print ("Invalid directory.")

def backup_files_by_extension():
    print("Backup files by extension")
    source = input("Enter the directory you want to backup: ")
    target = input("Enter the directory you want to backup to: ")
    extension = input("Enter the file extension you want to backup: ")
    if os.path.exists(source) and os.path.exists(target):
        for file in os.listdir(source):
            if os.path.isfile(os.path.join(source, file)) and file.endswith(extension):
                os.system("cp " + os.path.join(source, file) + " " + target)
        with open(os.path.join(target, "backup_log.txt"), "w") as log:
            log.write(f"""Backup completed successfully!
            Backup time: {datetime.now()}
            Backup source: {source}
            Files backed up: {os.listdir(source)}
            """)
        print("Backup completed successfully!")
    else:
        print ("Invalid directory.")

def main():
    options_methods = {
        "1": backup_full_directory,
        "2": backup_single_file,
        "3": backup_files_by_extension
    }
    options = [
        "Backup full directory",
        "Backup single file",
        "Backup files by extension"
    ]

    print("Welcome to the backup program!")
    print("Please choose an option:")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    choice = input("Enter your choice: ")
    if choice in options_methods:
        options_methods[choice]()

if __name__ == "__main__":
    main()
