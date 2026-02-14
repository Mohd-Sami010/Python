import webbrowser

#Ask the user for the search term 
query = input("What would you like to search for on YouTube? ")

#Construct the search url 
url = "https://www.youtube.com/results?search_query=" + query

#Open the search url using the default browser 
webbrowser.open(url)