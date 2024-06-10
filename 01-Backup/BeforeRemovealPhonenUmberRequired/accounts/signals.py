from django.db.models.signals import post_save, pre_save  # CH29
from django.dispatch import receiver # CH29
from .models import User, UserProfile

# MEthod 2 Decorator function        
@receiver(post_save, sender=User)    
# we are generating a post save function
def post_save_create_profile_receiver(sender, instance,created,**kwargs):
    print(created) 
    if (created):
        UserProfile.objects.create(user=instance)
        print ('User profile is created')
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:       
            UserProfile.objects.create(user=instance)
            print('Profile Was not exist, but I cretaed one') 
        print('user is updated')
# method 1 
#post_save.connect(post_save_create_profile_receiver, sender=User)
# also import post_save signal

##############Pre save ####
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username,'this user is being saved')