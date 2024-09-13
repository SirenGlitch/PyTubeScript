from pytubefix import Search, YouTube
from pytubefix.cli import on_progress

results = Search(input('Enter the search term: '))

vidNumber = 0
options = [] # Create an empty list to hold the selected options

for video in results.videos:
    vidNumber += 1
    print(f'Option: {vidNumber}')
    print(f'Title: {video.title}')
    print(f'Author: {video.author}')
    print(f'Duration: {video.length} seconds')
    print('---')

while True:
    selected_option = input("Enter the number of the video you want to download or 'q' to quit: ") # Ask the user to enter a video option

    if selected_option.lower() == 'q':
        print("Quitting...")
        quit()

    elif selected_option.isdigit() and 0 < int(selected_option) <= vidNumber: # Validate user input
        selected_option = int(selected_option)
        options.append(results.videos[selected_option - 1])  # Append the corresponding video object from results to options list using zero-based indexing

        # TODO: Allow user to download multiple videos at once
        print("Is this right? (y/n) ") # Ask whether the user's selection is what the user wants
        print(f"Title: {options[0].title}")
        print(f"Author: {options[0].author}")

        confirm = input()
        if confirm.lower() == 'y':
            break # If the user is satisfied, continue the program
        else:
            options.pop() # If not, remove the last item from options list

    else: # Prompt the user for a valid option if neither 'q' nor a valid option was entered
        selected_option = int(input("Invalid Option. Enter the number of the video you want to download again: "))  # Re-request user input if invalid

url = options[0].watch_url

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

# TODO: Allow video to be downloaded in MP4
ys = yt.streams.get_audio_only()
ys.download(mp3=True)

quit()