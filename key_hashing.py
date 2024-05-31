import os
import face_recognition
import hashlib

def generate_key_from_images_in_directory(directory_path, person_name):
    # 디렉토리 내의 모든 이미지 파일 경로를 가져옴
    image_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # 사진에서 얼굴의 특징을 추출하여 저장할 리스트
    face_landmarks_list = []

    # 각 사진에서 얼굴의 특징을 추출
    for image_path in image_paths:
        # 이미지 파일을 불러와 얼굴 인식 및 특징점 추출
        image = face_recognition.load_image_file(image_path)
        face_landmarks = face_recognition.face_landmarks(image)
        # 추출된 얼굴 특징을 리스트에 추가
        if len(face_landmarks) > 0:
            face_landmarks_list.extend(face_landmarks)

    # 추출된 모든 얼굴 특징을 하나의 리스트로 통합하여 문자열로 변환
    integrated_landmarks = str(face_landmarks_list)

    # 문자열에 해시 함수를 적용하여 키 값을 생성
    key = hashlib.sha256(integrated_landmarks.encode()).hexdigest()

    # 키 값을 지정한 경로에 저장
    key_filename = os.path.join(directory_path, person_name + "_key.txt")
    with open(key_filename, 'w') as file:
        # 키 값을 파일에 저장
        file.write(key)
    return key_filename

def main():
    # 사용자로부터 이미지 파일이 있는 디렉토리 경로와 사람 이름을 입력 받음
    directory_path = input("Enter the directory path containing the images: ")
    person_name = input("Enter the person's name: ")

    # 이미지에서 고유한 키 값을 생성하고 파일에 저장
    key_filename = generate_key_from_images_in_directory(directory_path, person_name)
    print("Key saved to", key_filename)

if __name__ == "__main__":
    main()
