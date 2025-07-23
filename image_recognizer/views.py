from django.shortcuts import render
from fer import FER
import numpy as np
from PIL import Image

detector = FER(mtcnn=True)

def home(request):
    return render(request, 'image_recognizer/home.html')

def detect_emotion(request):
    if request.method == "POST" and request.FILES.get('image'):
        img_file = request.FILES['image']
        img = Image.open(img_file).convert("RGB")  # ensure RGB
        img_np = np.array(img)

        faces = detector.detect_emotions(img_np)

        if not faces:
            return render(request, "image_recognizer/result.html", {"results": None})

        # Combine emotions across all faces
        combined_emotions = {}
        for face in faces:
            for emotion, score in face["emotions"].items():
                combined_emotions[emotion] = combined_emotions.get(emotion, 0) + score

        # Average the scores if multiple faces
        for emotion in combined_emotions:
            combined_emotions[emotion] /= len(faces)

        # Find dominant emotion
        dominant_emotion, dominant_score = max(combined_emotions.items(), key=lambda x: x[1])

        # Prepare results for template
        results = {
            "dominant": {"emotion": dominant_emotion, "score": dominant_score},
            "all_emotions": combined_emotions,
        }

        return render(request, "image_recognizer/result.html", {"results": results})

    return render(request, "image_recognizer/upload.html")
