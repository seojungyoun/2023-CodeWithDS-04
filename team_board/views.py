from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Board
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .forms import BoardForm
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def index(request):
    all_boards = Board.objects.all().order_by("-pub_date")
    return render(request, 'team_board/community.html', {'title': 'Board List', 'board_list': all_boards})

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'team_board/teamdetail.html', {'board': board})

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
#     return render(request, 'team_board/teampost.html', context)

def write_team_board(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        major = request.POST.get('major')  # 추가한 전공 값
        author = request.user.username  # 현재 로그인된 사용자의 유저네임
        pub_date = timezone.now()

        b = Board(title=title, content=detail, major=major, author=author, pub_date=pub_date)
        b.save()
        return redirect('team_board:index')

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
    return render(request, 'team_board/teampost.html', context)

def create_reply(request, board_id):
    board = Board.objects.get(id=board_id)
    board.replies.create(comment=request.POST['comment'], rep_date=timezone.now())  # 'replies'는 related_name
    return HttpResponseRedirect(reverse('team_board:detail', args=(board_id,)))

def edit_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'GET':
        context = {'board':board}
        return render(request, 'team_board/teamrepost.html', context)
    elif request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('detail')
        board.major = request.POST.get('major')
        board.save()
        return redirect('team_board:index')

def delete_board(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)
        if request.user == board.author:
            board.delete()
            messages.success(request, '게시글이 삭제되었습니다.')
            return redirect('team_board:index')
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied



# def editboard(request, pk):
#     if request.user.is_authenticated:
#         item = get_object_or_404(Board, pk=pk)
#         if request.method == 'POST':
#             board_form = BoardForm(request.POST)
#             if board_form.is_valid():
#                 board = board_form.save(board=False)
#                 board.item = item
#                 board.author = request.user
#                 board.save()
#                 return redirect(board.get_absolute_url())
#         else:
#             return redirect(item.get_absolute_url())
#     else:
#         raise PermissionDenied

# class BoardUpdate(LoginRequiredMixin, UpdateView):
#     model = Board
#     form_class = BoardForm

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user == self.get_object().author:
#             return super(BoardUpdate, self).dispatch(request, *args, **kwargs)
#         else:
#             raise PermissionDenied