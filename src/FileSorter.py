import os
from ColorUtils import bcolors

class FileSorter:
    ignored_file_types = {'DS_Store'}

    @staticmethod
    def sort_files_by_type(path = None):
        if not path:
            path = input(f'{bcolors.WARNING}Please provide a folder path: {bcolors.ENDC}')

        file_list = os.listdir(path)

        file_type_dict = dict()

        for file in file_list:
            file_split = file.split('.')

            if len(file_split) < 2:
                continue

            file_name = file_split[0]
            file_type = file_split[1]

            if file_type in FileSorter.ignored_file_types:
                continue

            if not file_type in file_type_dict.keys():
                file_type_dict[file_type] = set()

            file_type_set = file_type_dict[file_type]
            file_type_set.add(file_name)

        if len(file_type_dict.keys()) < 1:
            print(f'{bcolors.FAIL}No files to sort. Aborting.')
            return


        for file_type in file_type_dict.keys():
            file_folder = f'{path}/{file_type}'

            if not os.path.exists(file_folder):
                os.mkdir(file_folder)

            for file_name in file_type_dict[file_type]:
                os.rename(f'{path}/{file_name}.{file_type}', f'{file_folder}/{file_name}.{file_type}')

        print(f'{bcolors.OKGREEN}All files successfully sorted')




FileSorter.sort_files_by_type('/Users/isaiah/Downloads/Fuji Film Simulations/test')