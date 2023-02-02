import os
from package import tistory_downloader
from package import extractor

def main():
    post_url = input("Input post url: ").strip()
    location = input("Input download location: ").strip()
    etraction_flag = input("Extract files from the archive? [y/n]: ").strip().lower()

    os.chdir(location)

    downloaded_files = tistory_downloader.download_from(post_url)
    downloaded_files.sort()

    if etraction_flag == "y":
        extractor.extract(location, downloaded_files[0])
        extractor.remove_files(location, downloaded_files)

    print("download completed")
    return

if __name__ == "__main__":
    main()