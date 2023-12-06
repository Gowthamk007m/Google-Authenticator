# your_app/context_processors.py
from allauth.socialaccount.models import SocialAccount


def social_account_context(request):
    context = {}
    if request.user.is_authenticated:
        try:
            google_account = SocialAccount.objects.get(
                provider='google', user=request.user)

            # Accessing user information
            user_id = google_account.uid
            email = google_account.extra_data.get('email')
            full_name = google_account.extra_data.get('name')
            given_name = google_account.extra_data.get('given_name')
            family_name = google_account.extra_data.get('family_name')
            profile_picture_url = google_account.extra_data.get('picture')
            
            request.user.email = email
            request.user.first_name = given_name
            request.user.last_name = family_name
            request.user.username = full_name
            request.user.save()

            context = {
                'user_id': user_id,
                'email': email,
                'full_name': full_name,
                'profile_picture_url': profile_picture_url,
            }
        except SocialAccount.DoesNotExist:
            pass

    return context
