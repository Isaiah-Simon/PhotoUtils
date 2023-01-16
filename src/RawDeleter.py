import os
from ColorUtils import bcolors

class RawDeleter:
    @staticmethod
    def delete_raws_without_jpg(path = None, raw_type = None):
        if not path:
            path = input(f'{bcolors.WARNING}Please provide a folder path: {bcolors.ENDC}')

        if not raw_type:
            raw_type = input(f'{bcolors.WARNING}Please provide a RAW file type, excluding the \".\" (Ex: RAF, CR3, ARW):  {bcolors.ENDC}')
        
        file_list = os.listdir(path)

        raw_suffix = '.' + raw_type
        raw_set = set()
        jpg_set = set()

        print(f'{bcolors.OKGREEN}Finding all {raw_suffix} files without an associated JPG in {path}\n')

        for file in file_list:
            if ('.jpg' in file):                
                jpg_set.add(file.split('.')[0])
            elif(raw_suffix in file):
                raw_set.add(file.split('.')[0])

        unmatched_raws = set()

        for raw in raw_set:
            if (raw not in jpg_set):
                unmatched_raws.add(raw)

        unmatched_raws_len = len(unmatched_raws)

        print(f'{bcolors.WARNING}Found {unmatched_raws_len} {raw_suffix} files without an associated JPG{bcolors.ENDC}')

        if unmatched_raws_len == 0:
            print(f'{bcolors.FAIL}No unmatched raws found. Cancelling.')
            return

        for i, unmatched_raw in enumerate(unmatched_raws):
            print(f'{i+1}. {unmatched_raw}')

        user_input = input(f'\n{bcolors.BOLD}{bcolors.HEADER}Would you like to delete these files? Type \'YES\' to delete. Type any other key to cancel\n{bcolors.ENDC}')

        if user_input == 'YES':
            for unmatched_raw in unmatched_raws:
                file_name = f'{unmatched_raw}{raw_suffix}'
                unmatched_raw_folder = f'{path}/raw_without_jpg'
                if not os.path.exists(unmatched_raw_folder):
                    os.mkdir(unmatched_raw_folder)
                os.rename(f'{path}/{file_name}', f'{unmatched_raw_folder}/{file_name}')
                print(f'\n{bcolors.OKGREEN}Successfully moved {file_name} to {unmatched_raw_folder}')
        else:
            print(f'{bcolors.FAIL}Deletion has been cancelled')