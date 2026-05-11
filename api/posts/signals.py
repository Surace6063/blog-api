from .models import Post
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Signal - 1
# delete image after post is deleted
@receiver(post_delete,sender=Post)
def delete_post_image(sender,instance,**kwargs):
    # After post is deleted, first check if it's image exists or not
    # if exists delete
    if instance.image:
        instance.image.delete(False)



# Signal - 2
# delete old image of post after new image is updated
@receiver(pre_save,sender=Post)
def delete_old_image_on_update(sender,instance,**kwargs):
    if not instance.pk:
        # skip if this is new post(no previous image)
        return
    
    try:
        # get old image before update
        old_image = Post.objects.get(pk=instance.pk).image
    except Post.DoesNotExist:
        return 
    
    new_image = instance.image
    
    # comapare old and new images
    # if different delete old image 
    if old_image and old_image != new_image:
        old_image.delete(False)  
        
             