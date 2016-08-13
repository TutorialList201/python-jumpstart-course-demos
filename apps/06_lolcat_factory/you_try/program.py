import os
import cat_service
import subprocess
import platform


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)
    print('Hello from main')


def print_header():
    print('-----------------------------------------')
    print('              CAT FACTORY')
    print('-----------------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name))
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cats in OS window')
    system = platform.system()
    if system == 'Darwin':
        subprocess.call(['open', folder])
    elif system == 'Windows':
        subprocess.call(['explorer', folder])
    elif system == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your OS:" + system)

if __name__ == '__main__':
    main()
