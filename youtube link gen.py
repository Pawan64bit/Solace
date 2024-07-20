import webbrowser
from googlesearch import search

def get_youtube_link(search_query):
    try:
        search_results = search(f"{search_query} site:youtube.com", num=1, stop=1, pause=2)
        
        for result in search_results:
            if 'watch?v=' in result:
                return result
        
        return None
    except Exception as e:
        print(f"Try again. {str(e)}")
        return None

if __name__ == "__main__":
    user_input = input("Enter your search query: ")
    youtube_link = get_youtube_link(user_input)
    
    if youtube_link:
        print("Opening")
        webbrowser.open(youtube_link)
    else:
        print("No YouTube link found")