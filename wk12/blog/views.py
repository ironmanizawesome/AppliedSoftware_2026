from django.views.generic import ListView, DetailView
from .models import Post

# ===== FBV -> CBV 로 바꾼 부분 =====
# FBV 땐 이렇게 함수로 다 직접 짰음:
#   def index(request):
#       posts = Post.objects.all().order_by('-created_at')
#       return render(request, 'blog/index.html', {'posts': posts})
#   def detail(request, pk):
#       post = get_object_or_404(Post, pk=pk)
#       return render(request, 'blog/detail.html', {'post': post})
# CBV는 제네릭 뷰 상속만 하면 위 쿼리+render+context 를 장고가 알아서 해줌.


class PostList(ListView):
    model = Post          # FBV의 Post.objects.all() 을 이 한 줄이 대신함
    ordering = '-pk'      # FBV의 .order_by(...) 대신임. 최신순 정렬
    # 템플릿: 안 적으면 blog/post_list.html 을 관례로 자동으로 찾음
    #         (FBV는 render() 에 'blog/index.html' 직접 박았음)
    # context: 'post_list' 라는 이름으로 자동으로 넘어감
    #          (FBV는 {'posts': posts} 처럼 직접 넘겼음)


class PostDetail(DetailView):
    model = Post          # FBV의 get_object_or_404(Post, pk=pk) 를 자동으로 함
    # url 의 <int:pk> 를 받아서 해당 글 1개 알아서 찾아줌
    # 템플릿은 blog/post_detail.html 자동, context 이름은 'post' 임
