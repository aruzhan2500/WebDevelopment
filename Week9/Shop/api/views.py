from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    products_to_json = [p.to_json() for p in products]
    return JsonResponse(products_to_json, safe=False)

def product_id(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')
    return JsonResponse(product.to_json())

def categories_list(request):
    categories = Category.objects.all()
    categories_to_json = [c.to_json() for c in categories]
    return JsonResponse(categories_to_json, safe=False)

def category_id(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2')
    return JsonResponse(category.to_json())

def products_by_category(request, category_id):
    products = Product.objects.all()
    products_to_json = [p.to_json() for p in products]
    p = []
    for i in products_to_json:
        if i['category_id'] == category_id:
            p.append(i.copy())
    if not p:
        return HttpResponse(f'<h2>Product DoesNotExist!!!</h2>')
    return JsonResponse(p, safe=False)