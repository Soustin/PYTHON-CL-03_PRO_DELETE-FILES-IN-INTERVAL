import os
import shutil
import time

#main funtion
def main():

    #initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    #specify the path
    path =  "/PATH_TO_DELETE"

    #specify the date
    days = 30

    #converting days to seconds
    #time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    #checking wether file is present in file or not
    if os.path.exists(path):
        #iterating over each and every file in the path
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                #removing the folder
                remove_folder(root_folder)
                deleted_folders_count += 1 # incrementing count

                break

            else:
                #checking folders from the root folder
                for folder in folders:
                    # folder path
                    folder_path = os.path.join(root_folder, folder)
                    #comparing with the days
                    if seconds >= get_file_or_folder_age(folder_path):
                        #invoking the remove folder funtion
                        remove_folder(folder_path)
                        deleted_folders_count += 1 # incrementing count

                #checking the current directory files
                for file in files:
                    #file path
                    file_path = os.path.join(root_folder, file)

                    #comparing the days
                    if seconds >= get_file_or_folder_age(file_path):
                        #invoking the remove folder funtion
                        remove_folder(file_path)
                        deleted_folders_count += 1 # incrementing count

        else:

            #if the path is not a directory
            #comparing with the days
            if seconds >= get_file_or_folder_age(path):

                #invoking the remove folder funtion
                    remove_folder(path)
                    deleted_folders_count += 1 # incrementing count
    else:
        #file folder is not found
        print(f'"{path}" is not found')
        deleted_files_count += 1 #incrementing count

    print(f"Total Folders Deleted: {deleted_folders_count}")
    print(f"Total Files Deleted: {deleted_files_count}")

def remove_folder(path):

    #removing the folder
    if not shutil.remtree(path):
         #print a success message
         print(f"{path} has been removed successfully")
    
    else:
        #failure message
        print(f"Unable to remove"+path)

def remove_file(path):

    #removing the file
    if not os.remove(path):

        #success message
        print(f"{path} is removed successfully")

    else:

        #failure message
        print("Unable to delete the path: "+path)

def get_file_or_folder_age(path):
    #getting ctime of the file or folder
    #time will be in seconds
    ctime = os.stat(path).st_ctime

    #returning the time
    return ctime

if __name__ == "__main__":
    main()
