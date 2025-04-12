from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Cursos

@receiver([post_delete, post_save], sender=Cursos)
def invalidate_colleges_cache(sender, instance, **kwargs):
    """
    Invalidate colleges caches when a product is created, updated, or deleted
    """
    print("Clearing product cache")
    
    # Clear product list caches
    cache.delete_pattern('*college_list*')