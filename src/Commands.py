from RawDeleter import RawDeleter
from FileSorter import FileSorter

class Command:
    def __init__(self, description, command):
        self.description = description
        self.command = command

class Commands:
    @staticmethod
    def get_commands():
        return [
            Command('Move all specified RAW files that do not have an associated JPG', RawDeleter.delete_raws_without_jpg),
            Command('Sort all files by file type into specific folders', FileSorter.sort_files_by_type)
        ]
