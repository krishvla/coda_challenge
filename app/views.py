from django.shortcuts import render, redirect
from api.models import *
import socket

# Create your views here.

def homeview(request):
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname) 
    voted = votes.objects.filter(ip_addr=IPAddr).first()
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
    print(context)
    context['total_votes'] = len(votes.objects.all())
    context['candidates'] = candidates
    if request.method == 'POST':
        candidate_id = request.POST['candi_id']
        candi_obj = hackers.objects.get(id = candidate_id)
        testing = votes.objects.filter(ip_addr=IPAddr)
        print(len(testing))
        if(len(testing) > 0):
            context["message"] = True
            context["message_info"] = "You have used your voting limit"
            return render(request, "home.html",context)
        else:
            voting_obj = votes(
                candidate = candi_obj,
                ip_addr = IPAddr,
                voted = True

            )
            voting_obj.save()
            context["message"] = True
            context["message_info"] = "Successfully Voted for {}".format(candi_obj.name)
        return render(request, "home.html",context)
    return render(request, "home.html",context) 

