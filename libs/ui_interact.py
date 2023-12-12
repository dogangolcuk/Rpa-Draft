from pywinauto import Desktop


def find_and_double_click(cmd):
    desktop = Desktop(backend="uia")
    desk = desktop.window(auto_id="1")  # Change this if needed

    try:
        element = desk.child_window(
            title=cmd["title"], control_type=cmd["control_type"])
        if element.exists() and element.is_visible() and element.is_enabled():
            element.double_click_input()
            return True  # Action performed successfully
    except Exception as e:
        print(f"Error: {e}")

    return False  # Element not found or action unsuccessful

# # Example usage:
# element_properties = {
#     "title": "test6",  # Replace with the desired properties
#     "control_type": "ListItem"
# }

# if not find_and_double_click(**element_properties):
#     print("Element not found or action unsuccessful")
