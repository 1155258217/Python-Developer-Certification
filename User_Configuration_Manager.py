def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    else:
        msg = "Current User Settings:\n"
        for key,value in settings.items():
            msg += key.title()+': '+value+'\n'
        return msg

test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}
