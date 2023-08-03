from django.shortcuts import render
import datetime

def calculate_typing_speed(script, time_taken):
    words = script.split()
    num_words = len(words)
    words_per_minute = (num_words / time_taken) * 60
    return words_per_minute

def typing_test(request):
    if request.method == 'POST':
        script_to_type = 'Returns the number of times the specified element appears in the list. Example. # create a list numbers'
        time_limit_in_seconds = int(request.POST.get('time_limit', 60))

        context = {}
        context['script_to_type'] = script_to_type
        context['time_limit_in_seconds'] = time_limit_in_seconds

        return render(request, 'typing_test.html', context)

    return render(request, 'typing_test_start.html')
