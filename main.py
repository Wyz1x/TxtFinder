import os
import re

DBpath = './'
name = """
 ▄█     █▄  ▄██   ▄    ▄███████▄   ▄█  ▀████    ▐████▀ 
███     ███ ███   ██▄ ██▀     ▄██ ███    ███▌   ████▀  
███     ███ ███▄▄▄███       ▄███▀ ███▌    ███  ▐███    
███     ███ ▀▀▀▀▀▀███  ▀█▀▄███▀▄▄ ███▌    ▀███▄███▀    
███     ███ ▄██   ███   ▄███▀   ▀ ███▌    ████▀██▄     
███     ███ ███   ███ ▄███▀       ███    ▐███  ▀███    
███ ▄█▄ ███ ███   ███ ███▄     ▄█ ███   ▄███     ███▄  
 ▀███▀███▀   ▀█████▀   ▀████████▀ █▀   ████       ███▄               
"""


def search_in_txt_files(directory, searchInp):
    pattern = re.compile(re.escape(searchInp), re.IGNORECASE)

    found = False

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        for line_number, line in enumerate(file, 1):
                            if pattern.search(line):
                                print(f"Found in {filename}: {line.strip()}")
                                found = True
                except Exception as e:
                    print(f"Cant open file:( {file_path}: {e}")

    if not found:
        print("404")


def DBsearch():
    print(name)

    while True:
        searchInp = input("Enter any information ('exit' to quit): ")
        if searchInp.lower() == 'exit':
            break

        search_in_txt_files(DBpath, searchInp)
        print("-" * 40)


DBsearch()
