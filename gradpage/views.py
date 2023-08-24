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

# def write(request):
#     # 전공(major) 선택을 위한 데이터
#     major_values = [
#         "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
#         "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
#         "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
#         "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
#         "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
#         "정치외교학전공", "의상디자인전공", "유아교육과"
#     ]

#     context = {
#         'major_values': major_values
#     }
#     return render(request, 'team_board/write.html', context)

# def select_department(request):
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             selected_department = form.cleaned_data['department']
#             if selected_department == 'itmedia':
#                 return redirect('itmedia_department')
            
#     else:
#         form = DepartmentForm()
        
#     return render(request, 'computer.html', {'form':form})

def itmedia_department(request):
    return render(request, 'gradpage/itmedia.html')

def software_department(request):
    return render(request, 'gradpage/software.html')

def cyber_department(request):
    return render(request, 'gradpage/cyber.html')

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

# def create_archiving(request, major):
#     if request.method == 'POST':
#         exhibit_title = request.POST.get('exhibit_title')
#         service_title = request.POST.get('service_title')
#         team_name = request.POST.get('team_name')
#         team_member = request.POST.get('team_member')
#         description = request.POST.get('description')
#         file = request.FILES.get('file')

#         major_instance = Major.objects.get(name=major)
#         # 아카이빙 객체 생성시 선택한 전공(major) 정보 추가
#         a = Archive(
#             exhibit_title=exhibit_title,
#             service_title=service_title,
#             major=major_instance,
#             team_name=team_name,
#             team_member=team_member,
#             description=description,
#             file=file
#         )
#         a.save()

#         return redirect('computer')

#     return render(request, 'gradpage/archiving.html', {'major': major})

