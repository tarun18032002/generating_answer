from django.shortcuts import render, redirect
from .models import Question
from .forms import UploadDocForm
import docx
import openai
from django.conf import settings

# Set API key directly
openai.api_key = settings.OPENAI_API_KEY

def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})

def upload_docx(request):
    if request.method == 'POST':
        form = UploadDocForm(request.POST, request.FILES)
        if form.is_valid():
            doc_file = request.FILES['file']
            doc = docx.Document(doc_file)
            for para in doc.paragraphs:
                if para.text.strip():
                    Question.objects.get_or_create(text=para.text.strip())
            return redirect('home')
    else:
        form = UploadDocForm()
    return render(request, 'upload.html', {'form': form})

def generate_answers(request):
    questions = Question.objects.filter(is_answered=False)
    count = questions.count()
    for q in questions:
        prompt = f"Answer the following question in detail:\n{q.text}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ]
            )
            answer = response['choices'][0]['message']['content'].strip()
            # answer = "answer"+str(count)
            
            # count -=1
            q.answer = answer
            q.is_answered = True

            q.save()
        except Exception as e:
            print(f"Error for question: {q.text[:30]}... => {e}")
    return redirect('home')
