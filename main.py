import webbrowser
import pywhatkit

def process_command(command):
    if "youtube" in command:
        query = command.replace("youtube", "").strip()
        
        if "search" in command:
            search_query = query.replace("search", "").strip()
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            speak(f"Searching {search_query} on YouTube.")
        
        elif "play" in command:
            song = query.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

# Example usage:
command = "search coding tutorials on youtube"
process_command(command)

command = "play shape of you on youtube"
process_command(command)
