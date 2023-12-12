from pywinauto import backend

def get_backends():
    return list(backend.registry.backends.keys())

def element_info(backend_name="uia"):
    selected_backend = backend.registry.backends.get(backend_name)
    if not selected_backend:
        raise ValueError("Backend not found")
    
    element_info = selected_backend.element_info_class()
    return element_info

def get_next(element_info):
    result = []
    for child in element_info.children():
        child_dict = {
            'child': child,
            'parent': element_info.name
        }
        result.append(child_dict)
    return result

def print_element_info(node, index):
    parent = node["parent"]
    child = node["child"]
    print(f"{index}.---------------------------------------------------------")
    print(f"Element Number: {index}")
    print(f"Parent: {parent}")
    print(f"Control type: {child.control_type}")
    print(f"Name: {child.name}")
    print(f"Class Name: {child.class_name}")
    print(f"Rectangle: {child.rectangle}")
    print(f"ID: {id(child)}")
    print("---------------------------------------------------------")

element_info_instance = element_info("uia")
elements = get_next(element_info_instance)

for index, node in enumerate(elements, start=1):
    print_element_info(node, index)
