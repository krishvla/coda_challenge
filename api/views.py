from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import hackersSerializer
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    allUrls = {
        'Important Note': 'Need Admin Code for The below Operation',
        'Add Hacker': '/add-hacker',
        'All Hacers': '/all-hackers',
        'Edit Hacker Details': '/edit-hacker/pk',
        'Delete Hacker': '/delete-hacker',
        
    }
    return Response(allUrls)


#Add Hacker
@api_view(['POST'])
def hackerAdd(request):
    checking = request.data
    try:
        db_code = admincode.objects.filter(code = checking['admin_code'])
        if(len(db_code) > 0):
            serialize = hackersSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
            return Response(serialize.data)
        else:
            return Response("Your Not authorized to do this operation")
    except Exception as e:
        print(e)
        return Response("Your Not authorized to do this operation")




#All Hackers
@api_view(['GET'])
def allhackers(request):
    hacker = hackers.objects.all()
    serialize = hackersSerializer(hacker, many=True)
    return Response(serialize.data)


#Updating hacker
@api_view(['POST'])
def hackerUpdate(request,pk):
    checking = request.data
    try:
        db_code = admincode.objects.filter(code = checking['admin_code'])
        if(len(db_code) > 0):
            hacker = hackers.objects.get(id=pk)
            serialize = hackersSerializer(instance=hacker, data=request.data)
            if serialize.is_valid():
                serialize.save()
            return Response(serialize.data)
        else:
            return Response("Your Not authorized to do this operation")
    except hackers.DoesNotExist:
        return Response("Hacker with that id Does not Exsists")
    except Exception as e:
        print(e)
        return Response("Your Not authorized to do this operation")

#Deleting hacker
@api_view(['POST'])
def hackerDelete(request):
    checking = request.data
    try:
        db_code = admincode.objects.filter(code = checking['admin_code'])
        if(len(db_code) > 0):
            hacker = hackers.objects.get(id=checking['id'])
            hacker.delete()
            return Response("Successfully Deleted")
        else:
            return Response("Your Not authorized to do this operation")
    except hackers.DoesNotExist:
        return Response("Hacker with that id Does not Exsists")
    except Exception as e:
        return Response("Your Not authorized to do this operation")

