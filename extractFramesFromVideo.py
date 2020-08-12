import cv2
import os

video_path = "./videos/custom"
images_path = "./images"
save_every = 20


def extract_frames(folder, video_file):
    video_file_path = os.path.join(video_path, folder, video_file)
    image_folder_path = os.path.join(
        images_path, folder, os.path.splitext(video_file)[0])
    os.makedirs(image_folder_path, exist_ok=True)
    cap = cv2.VideoCapture(video_file_path)

    frame_index = 0
    image_index = 1

    while True:
        ret, frame = cap.read()

        if frame is None:
            break

        if frame_index % save_every == 0:
            image_file_path = os.path.join(image_folder_path,
                                           str(image_index)) + ".png"
            cv2.imwrite(image_file_path, frame)
            print(image_file_path, "saved")
            image_index += 1

        frame_index += 1

        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    # extract_frames("22", "1828.mp4")
    folders = os.listdir(video_path)

    for folder in folders:
        folder_path = os.path.join(video_path, folder)
        video_files = os.listdir(folder_path)
        for video_file in video_files:
            extract_frames(folder, video_file)
