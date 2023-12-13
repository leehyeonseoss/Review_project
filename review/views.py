from .models import Review
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .admin import ReviewAdmin
# from django.contrib.auth.decorators import login_required



def create_review(request):
    if request.method == 'POST':
        admin = ReviewAdmin(request.POST, request.FILES)
        if admin.is_valid():
            review = admin.save()
            review.user = request.user
            review.save()

            return redirect('review:index')  
    else:
        admin = ReviewAdmin()

    return render(request, 'review_create.html', {'admin': admin})

def detail(request, review_id):
 board = Review.objects.get(id=review_id)
 context = {'review': board}
 return render(request, 'review/review_detail.html', context) 

class create(generic.CreateView):
   model = Review
   fields = ['subject', 'content', 'create_date']
   success_url = reverse_lazy('review:index')
   template_name_suffix = '_create'

def index(request):
    # your view logic here
    board_list = Review.objects.order_by('-create_date')
    context = {'review_list': board_list}
    return render(request, 'review/review_list.html', context)

def mypage(request):
   user = request.user
   user_reviews = Review.objects.filter(user=request.user)
   return render(request, 'review/mypage.html')


def image(request):
   image = Review.dbject.all()
   return render(request, 'review/review_list.html', {'image':image})

def edit(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        admin= ReviewAdmin(request.POST, request.FILES, instance=review)
        if admin.is_valid():
            admin.save()
            return redirect('review:detail', review_id=review_id)
    else:
        admin= ReviewAdmin(instance=review)

    return render(request, 'review/edit.html', {'admin': admin, 'review': review})

def delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('review:index')  # 리뷰 삭제 후 이동할 페이지 지정

    return render(request, 'review/delete.html', {'review': review})
