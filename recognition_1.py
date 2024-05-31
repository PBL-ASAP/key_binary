import cv2
import face_recognition
import hashlib
import time

def load_key_from_file(key_filename):
    with open(key_filename, 'r') as file:
        return file.read().strip()

def main(video_path, key):
    # 동영상 파일 열기
    video_capture = cv2.VideoCapture(video_path)
    
    if not video_capture.isOpened():
        print("Error: Unable to open video file")
        return

    frame_count = 0
    face_found = False

    while True:
        # 프레임 읽기
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 30 == 0:
            print(f"Processing frame {frame_count}...")

        # 얼굴 인식 및 특징 추출
        start_time = time.time()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # 추출된 특징을 해시 함수를 적용하여 키 값 생성
        for face_encoding in face_encodings:
            integrated_encoding = str(face_encoding)
            encoded_key = hashlib.sha256(integrated_encoding.encode()).hexdigest()

            # 저장된 키 값과 비교하여 일치하는지 확인
            if encoded_key == key:
                face_found = True
                print("Matching face found!")
                print("Time elapsed for face recognition:", elapsed_time, "seconds")
                break

        if face_found:
            break

    if not face_found:
        print("No matching face found in the video.")

    # 동영상 파일 닫기
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 동영상 파일 경로와 키 값을 입력 받음
    video_path = input("Enter the path of the video file: ")
    key_filename = input("Enter the path of the key file: ")

    key = load_key_from_file(key_filename)
    main(video_path, key)

