from pytube import YouTube
from pathlib import Path
from colorama import init, Fore


print(f"{Fore.RED}You{Fore.WHITE}Tube\033[39m to MP3/MP4 made by: {Fore.MAGENTA}Lewd\033[39m")
link = input(f"[{Fore.YELLOW}?\033[39m]\033[39mLink to video: ")
video_object = YouTube(link)
downloads_path = str(Path.home() / "Downloads")

print("****************************************************")
print(  f"[{Fore.CYAN}*\033[39m]Title:  \033[39m {video_object.title}")
print(  f"[{Fore.CYAN}*\033[39m]Length: \033[39m {round(video_object.length / 60,2)} minutes")
print(  f"[{Fore.CYAN}*\033[39m]Views:  \033[39m {video_object.views}")
print(  f"[{Fore.CYAN}*\033[39m]Creator: \033[39m {video_object.author}")
print("****************************************************")
print(" ")
print("[1] MP4")
print("[2] MP3")
print(" ")

choice = int(input(f"[{Fore.YELLOW}?\033[39m]\033[39m What filetype do you want to download: "))

if choice == 1:
	print(f"Downloading {video_object.title} as MP4!")
	video_object.streams.get_highest_resolution().download(downloads_path)


elif choice == 2:
	print(f"Downloading {video_object.title} as MP3!")
	video_object.streams.get_audio_only().download(downloads_path)

else:
	print(f"{Fore.RED}That is not a valid choice!\033[39m")



print(f"[{Fore.GREEN}!\033[39m]{Fore.GREEN}Download Complete!\033[39m")
print(f"File downloaded to {downloads_path}")
input(f"[{Fore.CYAN}*\033[39m]Press any key to exit...")