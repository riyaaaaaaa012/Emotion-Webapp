from django.shortcuts import render
from transformers import pipeline

# Load Hugging Face model globally (once)
emotion_classifier = pipeline("text-classification",
                              model="j-hartmann/emotion-english-distilroberta-base",
                              return_all_scores=True)

def home(request):
    return render(request, 'chat_analyzer/home.html')

def analyze_text(request):
    if request.method == "POST":
        user_input = request.POST.get("user_text")
        results = emotion_classifier(user_input)[0]  # Get list of emotions
        # Sort emotions by score (highest first)
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        return render(request, 'chat_analyzer/result.html', {
            "user_input": user_input,
            "results": sorted_results
        })
    return render(request, 'chat_analyzer/home.html')
