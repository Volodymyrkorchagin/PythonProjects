from django.shortcuts import render

def english(request):
    return render(request, 'song/lyrics.html', {
        'lyrics': "We are the champions, my friends And we'll keep on fighting till the end",
        'author': 'Queen - We Are The Champions'
    })

def french(request):
    return render(request, 'song/lyrics.html', {
        'lyrics': "Nous sommes les champions, mes amis Et nous continuerons à nous battre jusqu'à la fin",
        'author': 'Queen - We Are The Champions'
    })

def german(request):
    return render(request, 'song/lyrics.html', {
        'lyrics': "Wir sind die Champions, meine Freunde Und wir werden bis zum Ende weiterkämpfen",
        'author': 'Queen - We Are The Champions'
    })

def spanish(request):
    return render(request, 'song/lyrics.html', {
        'lyrics': "Somos los campeones, amigos míos Y seguiremos luchando hasta el final",
        'author': 'Queen - We Are The Champions'
    })