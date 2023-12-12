from pywinauto import Desktop

# Connect to the desktop
desktop = Desktop(backend="uia")

# Find the icon on the desktop based on its name or other properties
desk = desktop.window(auto_id="1")  # Replace "Icon Title" with the actual title of the icon
icon = desk.child_window(title="test6", control_type="ListItem") 

# Ensure the icon is visible and enabled before performing actions
if icon.exists() and icon.is_visible() and icon.is_enabled():
    # Double-click the icon
    icon.double_click_input()
else:
    print("Icon not found or not accessible")
