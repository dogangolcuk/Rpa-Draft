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
    # child_list = []
    # for child in element_info.children():
    #     child_list.append(element_info.name,child)
    # return child_list
    result = []
    
    for child in element_info.children():
        # Create a dictionary for each child-parent pair
        child_dict = {
            'child': child,
            'parent': element_info.name
        }
        result.append(child_dict)
    
    return result

# def print_child_list(child_list):
#     for child in child_list:
#         print(child)
        
# def print_child_list_detailed(child_list):
#     for child in child_list:
#         print("---------------------------------------------------------")
#         print(f"Parent: {element_info.name}")
#         print(f"Control type: {child.control_type}")
#         print(f"Name: {child.name}")
#         print(f"Class Name: {child.class_name}")
#         print(f"Rectangle: {child.rectangle}")
#         print(f"ID: {id(child)}")
#         print("---------------------------------------------------------")
        
# # print_child_list(get_next(element_info()))

# print_child_list_detailed(get_next(element_info()))

# for node in get_next(element_info()) :
#     # print(node["parent"])
#     parent = node ["parent"]
#     child = node["child"]
#     # print(node["child"])
#     print("---------------------------------------------------------")
#     print(f"Parent: {parent}")
#     print(f"Control type: {child.control_type}")
#     print(f"Name: {child.name}")
#     print(f"Class Name: {child.class_name}")
#     print(f"Rectangle: {child.rectangle}")
#     print(f"ID: {id(child)}")
#     print("---------------------------------------------------------")
    
    
for index, node in enumerate(get_next(element_info()), start=1):
    parent = node["parent"]
    child = node["child"]
    print(str(index)+".---------------------------------------------------------")
    print(f"Element Number: {index}")
    print(f"Parent: {parent}")
    print(f"Control type: {child.control_type}")
    print(f"Name: {child.name}")
    print(f"Class Name: {child.class_name}")
    print(f"Rectangle: {child.rectangle}")
    print(f"ID: {id(child)}")
    print("---------------------------------------------------------")

