# Import the module
!pip install instaloader
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'aman.kharwal')

print(type(profile))
