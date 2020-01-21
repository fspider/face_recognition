import face_recognition

def compare(sourceURL, targetURL):
    srcImg = face_recognition.load_image_file(sourceURL)
    tgtImg = face_recognition.load_image_file(targetURL)
    src_encs = face_recognition.face_encodings(srcImg) 
    tar_encs = face_recognition.face_encodings(tgtImg)
    if len(src_encs) < 1 or len(tar_encs) < 1:
        return False
    src_enc = src_encs[0]
    tar_enc = tar_encs[0]
    distance = face_recognition.face_distance([src_enc], tar_enc)

    print(distance)

    if distance < 0.5:
        return True
    return False

