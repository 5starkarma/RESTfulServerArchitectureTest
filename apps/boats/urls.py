from django.urls import path, include

urlpatterns = [
    path('boats/', include([
        # path('', MemoListView.as_view(), name='memos'),
        # path('stats/', MemoStatisticsListView.as_view(), name='memo-stats'),
        # path('<int:pk>', MemoDetailView.as_view(), name='memos-detail'),
        # path('create/', MemoCreateView.as_view(), name='memos-create'),
        # path('<int:pk>/update/', MemoUpdateView.as_view(), name='memos-update'),
        # path('<int:pk>/delete/', MemoDeleteView.as_view(), name='memos-delete'),
        # path('<int:pk>/notify', MemoNotificationView.as_view(), name='memos-notify'),
        # path('<int:pk>/download/', download_memo, name='memo-download'),
    ])),
]
