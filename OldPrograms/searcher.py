import webbrowser

# get the search query from user
query = input("What do you want to search on Google? ")

# Open a web browser tab with the search results
webbrowser.open("https://platform.openai.com/playground" + query)