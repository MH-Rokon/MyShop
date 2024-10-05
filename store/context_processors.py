# store/context_processors.py
def categories_processor(request):
    from store.models import Category 
    categories = Category.objects.all()
    return {'cat': categories}
