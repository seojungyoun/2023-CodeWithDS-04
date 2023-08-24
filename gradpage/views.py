from django.shortcuts import render, redirect
from .models import Archive, Major


# Create your views here.
def main(request):
    return render(request, 'gradpage/main.html')

def computer(request, a_id=None):
    # if a_id is not None:
    #     a = Archive.objects.get(id=a_id)
    # else:
    #     a = None
    archive_list = Archive.objects.all()
    return render(request, 'gradpage/computer.html', {'archive_list':archive_list})

def itmedia_department(request):
    return render(request, 'gradpage/itmedia.html')

def software_department(request):
    return render(request, 'gradpage/software.html')

def cyber_department(request):
    return render(request, 'gradpage/cyber.html')

def bio_department(request):
    return render(request, 'gradpage/bio.html')

def technology_view(request):
    return render(request, 'gradpage/technology.html')

def sports_department(request):
    return render(request, 'gradpage/sports.html')

def food_department(request):
    return render(request, 'gradpage/food.html')

def infstatic_department(request):
    return render(request, 'gradpage/infstatic.html')

def chemical_department(request):
    return render(request, 'gradpage/chemical.html')

def math_department(request):
    return render(request, 'gradpage/math.html')

def create_archiving(request):
    if request.method == 'POST':
        exhibit_title = request.POST.get('exhibit_title')
        service_title = request.POST.get('service_title')
        major = request.POST.get('major')
        team_name = request.POST.get('team_name')
        team_member = request.POST.get('team_member')
        description = request.POST.get('description')

        # 파일 업로드 처리
        file = request.FILES.get('file')

        # major_instance, created = Major.objects.get_or_create(name=major_name)

        # Archive 모델 생성 및 저장
        a = Archive(
            exhibit_title=exhibit_title,
            service_title=service_title,
            major=major,
            team_name=team_name,
            team_member=team_member,
            description=description,
            file=file
        )
        a.save()
        return redirect('computer') # 수정해야됨

    return render(request, 'gradpage/archiving.html')
