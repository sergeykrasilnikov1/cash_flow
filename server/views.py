from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from server.models import Status, Type, Category, Subcategory, CashFlow
from server.forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm
from server.widgets import FlatPickrDateInput
from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter, NumberFilter

class CashFlowFilter(FilterSet):
    date_from = DateFilter(
        field_name='date',
        lookup_expr='gte',
        label='От',
        widget=FlatPickrDateInput()
    )
    date_to = DateFilter(
        field_name='date',
        lookup_expr='lte',
        label='До',
        widget=FlatPickrDateInput()
    )
    status = ModelChoiceFilter(queryset=Status.objects.all(), label='Статус')
    type = ModelChoiceFilter(queryset=Type.objects.all(), label='Тип')
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    subcategory = ModelChoiceFilter(queryset=Subcategory.objects.all(), label='Подкатегория')
    amount_min = NumberFilter(field_name='amount', lookup_expr='gte', label='Сумма от')
    amount_max = NumberFilter(field_name='amount', lookup_expr='lte', label='Сумма до')

    class Meta:
        model = CashFlow
        fields = ['date_from', 'date_to', 'status', 'type', 'category', 'subcategory', 'amount_min', 'amount_max']

class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'cash_flow/list.html'
    context_object_name = 'cash_flows'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CashFlowFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cash_flow/form.html'
    success_url = reverse_lazy('cash_flow:cash_flow_list')

    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно создана')
        return super().form_valid(form)

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cash_flow/form.html'
    success_url = reverse_lazy('cash_flow:cash_flow_list')

    def form_valid(self, form):
        messages.success(self.request, 'Запись успешно обновлена')
        return super().form_valid(form)

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    success_url = reverse_lazy('cash_flow:cash_flow_list')
    template_name = 'cash_flow/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Запись успешно удалена')
        return super().delete(request, *args, **kwargs)

def load_categories(request):
    type_id = request.GET.get('type')
    categories = Category.objects.filter(type_id=type_id).order_by('name')
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)

# Reference data management views
class StatusListView(ListView):
    model = Status
    template_name = 'cash_flow/reference_list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Статусы',
        'create_url': 'cash_flow:status_create',
        'edit_url': 'cash_flow:status_edit',
        'delete_url': 'cash_flow:status_delete'
    }

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:status_list')
    extra_context = {
        'title': 'Добавить статус',
        'list_url': 'cash_flow:status_list'
    }

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:status_list')
    extra_context = {
        'title': 'Редактировать статус',
        'list_url': 'cash_flow:status_list'
    }

class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('cash_flow:status_list')
    template_name = 'cash_flow/confirm_delete.html'

# Type views
class TypeListView(ListView):
    model = Type
    template_name = 'cash_flow/reference_list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Типы',
        'create_url': 'cash_flow:type_create',
        'edit_url': 'cash_flow:type_edit',
        'delete_url': 'cash_flow:type_delete'
    }

class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:type_list')
    extra_context = {
        'title': 'Добавить тип',
        'list_url': 'cash_flow:type_list'
    }

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:type_list')
    extra_context = {
        'title': 'Редактировать тип',
        'list_url': 'cash_flow:type_list'
    }

class TypeDeleteView(DeleteView):
    model = Type
    success_url = reverse_lazy('cash_flow:type_list')
    template_name = 'cash_flow/confirm_delete.html'

# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'cash_flow/reference_list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Категории',
        'create_url': 'cash_flow:category_create',
        'edit_url': 'cash_flow:category_edit',
        'delete_url': 'cash_flow:category_delete'
    }

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:category_list')
    extra_context = {
        'title': 'Добавить категорию',
        'list_url': 'cash_flow:category_list'
    }

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:category_list')
    extra_context = {
        'title': 'Редактировать категорию',
        'list_url': 'cash_flow:category_list'
    }

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('cash_flow:category_list')
    template_name = 'cash_flow/confirm_delete.html'

# Subcategory views
class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'cash_flow/reference_list.html'
    context_object_name = 'items'
    extra_context = {
        'title': 'Подкатегории',
        'create_url': 'cash_flow:subcategory_create',
        'edit_url': 'cash_flow:subcategory_edit',
        'delete_url': 'cash_flow:subcategory_delete'
    }

class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:subcategory_list')
    extra_context = {
        'title': 'Добавить подкатегорию',
        'list_url': 'cash_flow:subcategory_list'
    }

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'cash_flow/reference_form.html'
    success_url = reverse_lazy('cash_flow:subcategory_list')
    extra_context = {
        'title': 'Редактировать подкатегорию',
        'list_url': 'cash_flow:subcategory_list'
    }

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('cash_flow:subcategory_list')
    template_name = 'cash_flow/confirm_delete.html'

