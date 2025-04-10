from django.urls import path
from . import views

app_name = 'cash_flow'

urlpatterns = [
    # Cash Flow URLs
    path('', views.CashFlowListView.as_view(), name='cash_flow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cash_flow_create'),
    path('<int:pk>/edit/', views.CashFlowUpdateView.as_view(), name='cash_flow_edit'),
    path('<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cash_flow_delete'),

    # AJAX URLs
    path('load-categories/', views.load_categories, name='ajax_load_categories'),
    path('load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),

    # Status URLs
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/edit/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),

    # Type URLs
    path('types/', views.TypeListView.as_view(), name='type_list'),
    path('types/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('types/<int:pk>/edit/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('types/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),

    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Subcategory URLs
    path('subcategories/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategories/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategories/<int:pk>/edit/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategories/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
]
