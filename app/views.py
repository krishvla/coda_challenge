from django.shortcuts import render, redirect
from api.models import *

# Create your views here.

def auth_chec(request):
    try:
        if request.session['id']:
            return True
        else:
            return False
    except:
        return False

def homeview(request):   
    if(auth_chec(request)):
        voted = votes.objects.filter(who_voted=request.session['id']).first()
        context = {}
        if(voted):
            context['is_voted'] = True
            context['voted'] = voted.candidate.id
        else:
            context['is_voted'] = False
        context["message"] = False

        candidates = hackers.objects.all()
        indi_votes = {}
        for candi in candidates:
            candi_votes = votes.objects.filter(candidate = candi)
            indi_votes[candi.id] = str(len(candi_votes))
        context['indi_votes'] = indi_votes
        context['total_votes'] = len(votes.objects.all())
        context['candidates'] = candidates
        if request.method == 'POST':
            candidate_id = request.POST['candi_id']
            candi_obj = hackers.objects.get(id = candidate_id)
            testing = votes.objects.filter(who_voted=request.session['id'])
            print(len(testing))
            if(len(testing) > 0):
                context["message"] = True
                context["message_info"] = "You have used your voting limit"
                return render(request, "home.html",context)
            else:
                voting_obj = votes(
                    candidate = candi_obj,
                    who_voted=request.session['id'],
                    voted = True

                )
                voting_obj.save()
                context["message"] = True
                context["message_info"] = "Successfully Voted for {}".format(candi_obj.name)
            return render(request, "home.html",context)
        return render(request, "home.html",context) 
    else:
        return redirect(loginview)


def loginview(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        check = hackers.objects.filter(name = name, password = password).first()
        if(check):
            request.session['id'] = check.id
            return redirect(homeview)
        else:
            context['msg'] = "Wrong credentials"
            return render(request,"login.html",context)
    return render(request,"login.html")