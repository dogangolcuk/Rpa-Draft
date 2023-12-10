import os
import ast

def extract_main_packages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    main_packages = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and node.names:
            for alias in node.names:
                package_name = alias.name.split('.')[0]  # Extract only the main package
                main_packages.add(package_name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            package_name = node.module.split('.')[0]  # Extract only the main package
            main_packages.add(package_name)

    return main_packages

def scan_project(directory):
    all_main_packages = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                main_packages = extract_main_packages(file_path)
                all_main_packages.update(main_packages)

    return all_main_packages

project_directory = os.getcwd()  # Use the current working directory

needed_main_packages = scan_project(project_directory)
print(needed_main_packages)
