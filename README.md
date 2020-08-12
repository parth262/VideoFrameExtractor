# Video Frame Extractor

### Prerequisites
- Open-CV
- Run `pip install -r requirements.txt` to install necessary libraries

### Steps to Extract Frames
- Open `extractFramesFromVideo.py`
- Change `video_path` to point to the folder with videos
- Change `images_path` to point to the folder where images will be extracted
- Set `save_every` to number representing every nth frame of the video to be saved
- Run `python3 extractFramesFromVideo.py`
- The images will be extracted in the folder which will have the same name as the video file


### Steps to Choose Random Images
- Open `chooseRandomImages.py`
- Chamge `images_path` to point to the folder with extracted images
- Change `target_folder` to the name of the folder where the randomly chosen images will be saved
- Run `chooseRandomImages.py`