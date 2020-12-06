import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.join(os.path.dirname(ABS_PATH), "Main Directory")

########### RESOURCES DIRECTORY ####################
RESOURCE_DIR = os.path.join(BASE_DIR, "Resources")
DOWNLOADED_IMAGE_DIR = os.path.join(RESOURCE_DIR, "downloaded pictures")
DOWNLOADED_AUDIO_DIR = os.path.join(os.path.join(RESOURCE_DIR, "Free Audio for commercial use"), "Audio Files")
Intro_and_End_DIR = os.path.join(RESOURCE_DIR, "Intro and End")
INTRO_DIR = os.path.join(Intro_and_End_DIR, "INTRO")
END_DIR = os.path.join(Intro_and_End_DIR, "END")

########### OUTPUT DIRECTORY #######################
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")

########### SELENIUM DRIVER DIRECTORY #######################
SELENIUM_DRIVER_DIR = os.path.join(os.path.dirname(ABS_PATH), "Selenium driver")

if __name__ == '__main__':
    print(ABS_PATH)
    print(BASE_DIR)
    print(RESOURCE_DIR)
    print(DOWNLOADED_IMAGE_DIR)
    print(DOWNLOADED_AUDIO_DIR)
    print(Intro_and_End_DIR)
    print(INTRO_DIR)
    print(END_DIR)
    print(OUTPUT_DIR)
    print(SELENIUM_DRIVER_DIR)
