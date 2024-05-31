import cv2
import face_recognition
import hashlib
import time

def main(video_path, key):
    # 동영상 파일 열기
    video_capture = cv2.VideoCapture(video_path)

    while True:
        # 프레임 읽기
        ret, frame = video_capture.read()
        if not ret:
            break

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
                print("Matching face found!")
                print("Time elapsed for face recognition:", elapsed_time, "seconds")

    # 동영상 파일 닫기
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 동영상 파일 경로와 키 값을 입력 받음
    video_path = input("Enter the path of the video file: ")
    key = input("Enter the key value: ")

    main(video_path, key)

