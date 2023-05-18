from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . forms import AssistChat
from gradio_client import Client


@csrf_exempt
def assist(request):
    form = AssistChat(request.POST or None)
    if form.is_valid():
        userInput = form.cleaned_data.get("userInput")
        client = Client("https://mosaicml-mpt-7b-chat--4nw7r.hf.space/")
        result = client.predict(
				userInput,	# str representing string value in 'Chat Message Box' Textbox component
				"null",	# str representing filepath to JSON file in 'parameter_3' Chatbot component
				fn_index=0
            )
        print(result)
        formoutput = AssistChat(initial={'userInput': userInput, 'output': result})
        # r = Records_log(Query=userInput, Emotion=output)
        # r.save()
        return render(request, 'home.html', {'form': formoutput})
    return render(request, 'home.html', {'form': form})