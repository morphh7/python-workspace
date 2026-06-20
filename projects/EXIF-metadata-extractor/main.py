from exif import Image
import sys
import requests

# CLI things
CYAN    = "\033[96m"
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

class ExifTools:
    @staticmethod
    def load_image_dict(image_dict: dict) -> list:
        returner = []

        for i in range(len(image_dict)):
            loaded_image = ExifTools.load_local_image(image_dict[i])
            returner.append(loaded_image)

        return returner
    
    @staticmethod
    def load_local_image(iamge_path: str) -> Image:
        with open(iamge_path, "rb") as local_image:
            return Image(local_image)
    
    @staticmethod
    def load_web_image(image_url: str) -> Image:
        response = requests.get(image_url)
        response.raise_for_status()

        with open(r"./img/.tempo_img.jpg", "wb") as temp_img:
            temp_img.write(response.content)
        
        return ExifTools.load_local_image(r"./img/.tempo_img.jpg")
        
    @staticmethod
    def extract_metadata(image: Image) -> None:
        if not image.has_exif:
            print(f"{BOLD}{RED}!{RESET} This image contains no EXIF metadata.")
            return

        tags = dir(image)

        for current_tag in tags:
            if current_tag.startswith("_"):
                continue

            if current_tag in ["delete", "delete_all", "get", "has_exif", "get_file", "get_thumbnail"]:
                continue

            try:
                value = getattr(image, current_tag)
                
                if value is not None and str(value).strip() != "":
                    print(f"{current_tag}: {value}")
                    
            except (AttributeError, NotImplementedError): # safely iterate larg arrays without crashing
                continue
        
        try:
            print("")

            if hasattr(image, "gps_latitude") and hasattr(image, "gps_longitude"):
                print(f"GPS Location: {ExifTools.convert_lat_long_to_decimal(image.gps_latitude, image.gps_latitude_ref)}, {ExifTools.convert_lat_long_to_decimal(image.gps_longitude, image.gps_longitude_ref)}")
                print(f"Google Maps Link: {ExifTools.to_google(image.gps_latitude, image.gps_latitude_ref, image.gps_longitude, image.gps_longitude_ref)}")
        except AttributeError:
            print("GPS data was present but format was unreadable.")

    @staticmethod
    def convert_lat_long_to_decimal(coordinates: any, coordinates_ref: str) -> float:
        decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600

        if coordinates_ref == "S" or coordinates_ref == "W":
            decimal_degrees = -decimal_degrees

        return decimal_degrees

    @staticmethod
    def to_google(latitude, latitude_ref, longitude, longitude_ref) -> str:
        decimal_latitude = ExifTools.convert_lat_long_to_decimal(latitude, latitude_ref)
        decimal_longitude = ExifTools.convert_lat_long_to_decimal(longitude, longitude_ref)

        return (f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}")

def display_ui() -> None:
    print(f"\n{BOLD}{RED}?{RESET} What do you want to do?")
    print(f"  1: Process local image (path)")
    print(f"  2: Process web image (url)")
    print(f"  3: Process pre-downloaded img (./img)")
    print(f"  q: quit app\n")

def pause() -> None:
    input(f"{BOLD}{RED}?{RESET} Press {BOLD}{RED}ENTER{RESET} to continue")

def main() -> None:
    display_ui()
    choice = input(f"{BOLD}{RED}>{RESET} ").strip()

    while choice != "q":
        if choice == "1":
            path = input(f"{BOLD}{RED}-->{RESET} Local path: ")
            loaded_image = ExifTools.load_local_image(path)

            ExifTools.extract_metadata(loaded_image) # print stuff

        elif choice == "2":
            url = input(f"{BOLD}{RED}-->{RESET} Image url: ")
            loaded_image = ExifTools.load_web_image(url)

            ExifTools.extract_metadata(loaded_image) # print stuff
        
        elif choice == "3":
            images = ExifTools.load_image_dict(["img/palm-tree.jpg"])
            
            for index, image in enumerate(images):
                ExifTools.extract_metadata(image)

        else:
            print(f"{BOLD}{RED}!{RESET} Not a right command. Please choose 1, 2, or q.")

        print("")
        pause()
        display_ui()
        choice = input(f"{BOLD}{RED}>{RESET} ").strip()

    print(f"\n{BOLD}{RED}!{RESET} Exiting...")
    sys.exit(0)
        
if __name__ == "__main__":
    main()