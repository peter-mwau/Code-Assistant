from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . forms import AssistChat


@csrf_exempt
def assist(request):
    form = AssistChat(request.POST or None)
    if form.is_valid():
        userInput = form.cleaned_data.get("userInput")
        response = requests.post("https://elitecode-detect-emotions.hf.space/run/predict", json={
        "data": [
            userInput,
        ]
        }).json()
        data = response["data"]
        #decode the json data
        # convert to string
        data = json.dumps(data) 
        # convert to dictionary
        data = json.loads(data)  
        output = data[0]['label']
        formoutput = EmotionForm(initial={'output': output, 'userInput': userInput})
        # print(formoutput)
        form = EmotionForm(request.POST or None)
        r = Records_log(Query=userInput, Emotion=output)
        r.save()
        return render(request, 'home.html', {'form': formoutput})
    return render(request, 'home.html', {'form': form})