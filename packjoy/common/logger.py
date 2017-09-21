from logging import FileHandler, WARNING

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)