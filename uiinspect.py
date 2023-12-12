from pywinauto import backend


def get_backends():
    backend_list = []
    for _backend in backend.registry.backends.keys():
        backend_list.append(_backend)
    return backend_list

# backends = get_backends()
# print(backends)


# from pywinauto import backend

def element_info(backend_name="uia"):
    selected_backend = backend.registry.backends[backend_name]
    element_info = selected_backend.element_info_class()
    # Now you have the element_info_class instance ready for usage
    # You might want to return it or perform operations on it
    
    # Example: print some attributes of the element_info_class
    # print(f"Backend: {backend_name}")
    # print(f"Control types: {element_info.control_type}")
    # print(f"Name: {element_info.name}")
    # print(id(element_info))
    return element_info

# element_info(backend_name="uia")

def get_next(element_info):
    for child in element_info.children():
        print("---------------------------------------------------------")
        print(f"Parent: {element_info.name}")
        print(f"Control type: {child.control_type}")
        print(f"Name: {child.name}")
        print (f"Class Name: {child.class_name}")
        print(f"ID: {id(child)}")
        print("---------------------------------------------------------")
        
        
get_next(element_info())