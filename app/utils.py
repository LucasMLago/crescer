import os

# Mapeia os caminhos relativos
def get_path(folder, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(script_dir, folder)
    return os.path.join(directory, filename)