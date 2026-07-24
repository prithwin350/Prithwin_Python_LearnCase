def validate(config, environment):
    if config.application_name == "":
        print("Application name cannot be empty.")
        return False

    return True