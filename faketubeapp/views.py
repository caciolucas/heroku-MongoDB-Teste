from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import Video
from .forms import VideoForm
from django.db.models import Count, F, Value, Sum

# Create your views here.

def home(request):
    videos = Video.objects.all()
    form = VideoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
        
    return render(request, 'faketubeapp/home.html', {'videos': videos,'form':form})

def like(request,id,like):
    if like==0:
        thumbs_down= int(Video.objects.get(id=id).thumbs_down)
        thumbs_down+=1
        Video.objects.filter(id=id).update(thumbs_down=thumbs_down)
    else:
        thumbs_up= int(Video.objects.get(id=id).thumbs_up)
        thumbs_up+=1
        Video.objects.filter(id=id).update(thumbs_up=thumbs_up)

    return redirect('home')

def ranking(request):
    music_videos = Video.objects.filter(theme='Music')
    entertainment_videos = Video.objects.filter(theme='Entertainment')
    education_videos = Video.objects.filter(theme='Education')
    kitties_videos = Video.objects.filter(theme='Kitties')
    doggos_videos = Video.objects.filter(theme='Doggos')

    total_thumbs={}

    thumbs_total_music=0
    thumbs_total_entertainment=0
    thumbs_total_education=0
    thumbs_total_kitties=0
    thumbs_total_doggos=0

    for video in music_videos:
	    thumbs_total_music+=video.thumbs_up+video.thumbs_down/2
    for video in education_videos:
	    thumbs_total_education+=video.thumbs_up+video.thumbs_down/2
    for video in entertainment_videos:
	    thumbs_total_entertainment+=video.thumbs_up+video.thumbs_down/2
    for video in kitties_videos:
	    thumbs_total_kitties+=video.thumbs_up+video.thumbs_down/2
    for video in doggos_videos:
	    thumbs_total_doggos+=video.thumbs_up+video.thumbs_down/2
    
    total_thumbs["Music"]=float(thumbs_total_music)
    total_thumbs["Entertainment"]=float(thumbs_total_entertainment)
    total_thumbs["Education"]=float(thumbs_total_education)
    total_thumbs["Kitties"]=float(thumbs_total_kitties)
    total_thumbs["Doggos"]=float(thumbs_total_doggos)
     

    ranked=[]
    i=0
    for key, value in sorted(total_thumbs.items(), key=lambda kv: kv[1], reverse=True):
	    i+=1
	    ranked.append({'rank':i,'theme':key,'thumbs':value})
    
    return render(request, 'faketubeapp/ranking.html', {'themes':ranked}) 