import face_recognition

def compare(sourceURL, targetURL):
    srcImg = face_recognition.load_image_file(sourceURL)
    tgtImg = face_recognition.load_image_file(targetURL)
    src_enc = face_recognition.face_encodings(srcImg)[0]
    tar_enc = face_recognition.face_encodings(tgtImg)[0]
    results = face_recognition.compare_faces([src_enc], tar_enc)
    return results[0]