from blockmanlauncher import selfbot  # Import selfbot module

# Set login data here
user_data = {
    "id": "(ur user id, is a number of ur user what can anyone get)",
    "accessToken": "(ur token, is a string what can be get from app)"
} # Get ur accessToken and id from app

# Selfbot api definition
blockman = selfbot.SelfBot()  # Instance the selfbot api

# Conect to server as selfbot
blockman.bl(token=user_data["accessToken"], user_id=user_data["id"]) 