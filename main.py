import glob
import os
import sys
import shutil


def file_creation(my_file_name, current_directory, destination_directory, my_counter, my_file_type, my_osu_flag, my_folder_name):

    file_exists = os.path.exists(destination_directory+'/'+my_file_name)
    # do whatever here to include counter in between file name and .
    my_index = current_directory.rfind('.')
    my_file_index = my_file_name.rfind(my_file_type)
    my_directory_only_index = current_directory.rfind('\\')
    new_file_name = my_file_name
    if file_exists:
        my_counter = my_counter+1
        if my_counter > 1:
            # print('removing previous')
            last_counter_index = my_file_name.rfind('-' + str(my_counter-1) + my_file_type)
            # print('my last index: ' + str(last_counter_index))
            print('duplicate files, incrementing to next value')
            new_file_name = my_file_name[0:last_counter_index] + '-' + str(my_counter) + my_file_type
            file_creation(new_file_name, current_directory, destination_directory, my_counter, my_file_type)
        else:
            new_file_name = my_file_name[0:my_file_index] + '-' + str(my_counter) + my_file_type
            file_creation(new_file_name, current_directory, destination_directory, my_counter, my_file_type)
    else:
        print(current_directory)
        my_new_destination = destination_directory+'/'+new_file_name
        print(my_new_destination)
        if(my_osu_flag==False):
            print('the file copied over is: ' + new_file_name)
        else:
            print('the file copied over is: ' + my_folder_name+'.mp3')
        shutil.copy(current_directory, my_new_destination)
        if my_osu_flag == True:
            os.rename(my_new_destination, destination_directory+'/'+my_folder_name+'.mp3')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prompt user to enter from path
    print('Enter the full path that you want to transfer from. ex: C:\Users\MyUserName\AppData\Local\osu!\Songs')

    dir_name = input()
    if dir_name.endswith('/'):
        # nothing
        print()
    else:
        # something
        dir_name = dir_name+"/"

    if os.path.isdir(dir_name):
        # nothing
        print('this directory exists')
    else:
        print('the directory does not exist, exiting')
        sys.exit(0)

    dir_name = dir_name.replace('\\', '/')

    print('The full path of the initial directory is: ' + dir_name)
    # Prompt user to enter destination path
    print('Enter the full destination path. ex: C:\Users\MyUserName\OneDrive\Desktop\New Folder')

    dir_target_location = input()

    if os.path.isdir(dir_target_location):
        # nothing
        print('this directory exists')
    else:
        print('the directory does not exist, exiting')
        sys.exit(0)

    dir_target_location = dir_target_location.replace('\\', '/')

    print('The full path of the destination directory is: ' + dir_target_location)

    print('Are you copying over mp3 files from Osu? y/n')
    is_osu = input()
    osu_flag = False
    if is_osu.lower() == 'y' or is_osu.lower() == 'yes':
        osu_flag = True
    print(osu_flag)
    file_type = '.mp3'

    if osu_flag == False:
        print('What file type do you want? ex: .txt, .mp3')
        file_type = input()

    my_list_dir = os.listdir(dir_name)

    for sub_dir in my_list_dir:
        my_sub_dir = (dir_name+sub_dir+'/')

        # folder path input
        path = os.path.abspath(my_sub_dir)

        # for storing size of each
        # file
        size = 0

        # for storing the size of
        # the largest file
        max_size = 0

        # for storing the path to the
        # largest file
        max_file = ""
        file_name = ""

        # walking through the entire folder
        # os.walk is divided into 3 tuples (dirpath, dirnames, filenames)
        for folder, sub_folders, files in os.walk(path):

            # checking the size of each file
            for file in files:
                if file.endswith(file_type):
                    size = os.stat(os.path.join(folder, file)).st_size

                    # updating maximum size
                    if size > max_size:
                        max_size = size
                        max_file = os.path.join(folder, file)
                        file_name = file

        if max_file == "":
            # don't do anything here
            print('not found')
        else:
            # start moving largest file from each subdirectory
            print(file_name + ' found')
            # function(file_name, dir_target_location) that checks if file exists and changes the name if necessary
            print("The largest file is: " + max_file)
            print('Size: ' + str(max_size) + ' bytes')
            counter = 0;
            file_creation(file_name, max_file, dir_target_location, counter, file_type, osu_flag, sub_dir)
