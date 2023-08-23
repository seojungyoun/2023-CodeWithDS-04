from django.shortcuts import render, redirect
from .models import Archive, Major


# Create your views here.
def main(request):
    return render(request, 'gradpage/main.html')

def write(request):
    # 전공(major) 선택을 위한 데이터
    major_values = [
        "국어국문학전공", "일어일문학전공", "중어중문학전공", "영어영문학전공",
        "불어불문학전공", "독어독문학전공", "스페인어전공", "사학전공",
        "철학전공", "미술사학전공", "문화인류전공", "경영학전공",
        "회계학전공", "국제통상학전공", "법학전공", "사회학전공",
        "문헌정보학", "전공심리학전공", "아동가족학전공", "사회복지학전공",
        "정치외교학전공", "의상디자인전공", "유아교육과"
    ]

    context = {
        'major_values': major_values
    }
    return render(request, 'team_board/write.html', context)

def create_archiving(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        major = request.POST.get('major')  # 추가한 전공 값
        author = request.user.username  # 현재 로그인된 사용자의 유저네임
        team_name = request.POST.get('team_name')
        description= request.POST.get('description')

        b = Archive(title=title, major=major, author=author,team_name = team_name,description = description)
        b.save()

    # 게시글 작성 후 게시글 목록 페이지로 이동
    all_infos = Archive.objects.all().order_by("pk")
    return redirect(Major.get_absolute_url())
