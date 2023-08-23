import os, pygame

def find_path_to_file(name_file):
    try:
        path_file = __file__.split("/")
        del path_file[-1]
        del path_file[-1]
    except IndexError:
        path_file = __file__.split("\\")
        del path_file[-1]
        del path_file[-1]
    path_file = "/".join(path_file)
    path_file = os.path.join(path_file, name_file)
    return path_file

# a = pygame.transform.scale().path.abspath("")