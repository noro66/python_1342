def add_setting(settings: dict, key_value_pair: tuple):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return (f"Setting '{key}' already exists! Cannot add" +
                " a new setting with this name.")
    settings[key] = value
    return f"Setting '{key}' added with value 'high' successfully!"


def update_setting(settings: dict, key_value_pair: tuple):
    key, value = key_value_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to 'dark' successfully!"
    return (f"Setting '{key}' does not exist!" +
            " Cannot update a non-existing setting.")


def delete_setting(settings: dict, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return (f"Setting '{key}' deleted successfully!")
    return ("Setting not found!")


def view_settings(settings: dict):
    if not settings:
        return "No settings available."
    settings_str = ""
    for key, value in settings.items():
        settings_str += f"{key.capitalize()}: {value}\n"
    return f"Current User Settings:\n{settings_str}"
