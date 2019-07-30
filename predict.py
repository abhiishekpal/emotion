import cv2
fisher_face = cv2.face.createFisherFaceRecognizer()
fisher_face.load('classifier.yml')

emojis = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] 
def predict(path='final_dataset/anger/0.jpg'):
    image = cv2.imread(path) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pred, conf = fisher_face.predict(gray)
    return emojis[pred] 

predict()