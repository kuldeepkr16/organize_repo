import os
import subprocess

DIR_NAME = "<path of the folder>"

folder_name = {
                "images": ["jpg", "jpeg", "png", "gif", "tiff", "raw"],
                "videos": ["mpeg", "mp4", "mpv", "avi", "wmv", "mov", "flv", "mkv"],
                "audio": ["pcm", "wav", "aiff", "mp3", "aac", "ogg", "wma", "flac", "alac", "wma"],
                "zipped": ["rar", "zip", "tar", "gz"],
                "pdfs": ["pdf"],
                "config_files": ["json", "xml", "yaml"],
                "doc_files": ["csv", "xlsx", "tsv", "xls", "txt", "docx"],
                "other_files": ["iso", "srt"]
                }


def get_folder_name(extension):
    for name, ext in folder_name.items():
        for x in ext:
            if extension.lower() == x.lower():
                return name
    else:
        return "others"


def create_dir_if_not_present(returned_folder_name):
    path_to_folder = os.path.join(DIR_NAME, returned_folder_name)
    # check if path is a dir
    is_path_present = os.path.isdir(path_to_folder)

    if is_path_present:
        return True, "path present"
    else:
        try:
            print("Creating dir...")
            os.mkdir(path_to_folder)

        except OSError as error:
            print("Error Occurred: {} while creating the Dir {}".format(error, path_to_folder))
        return False, path_to_folder


def organize():
    for filename in os.listdir(DIR_NAME):
        print("Working on file:", filename)

        extension = filename.split(".")[-1]
        returned_folder_name = get_folder_name(extension)
        if returned_folder_name == "others":
            continue

        is_present, folder_path = create_dir_if_not_present(returned_folder_name)
        if is_present:
            print("Folder present")
        else:
            print("created a folder", folder_path)

        current_file_path = os.path.join(DIR_NAME, filename)
        new_file_path = os.path.join(DIR_NAME, returned_folder_name, filename)

        if not subprocess.check_call(['mv', current_file_path, new_file_path]):
            print("File Moved: ", filename)


organize()
