import webbrowser

# Define your favorite websites
facebook_link = "https://www.facebook.com"
google_link = "https://www.google.com"
youtube_link = "https://www.youtube.com"

def firefox(url):
    """Open the given URL in the default web browser."""
    webbrowser.open(url)
