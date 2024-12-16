from rest_framework_simplejwt.tokens import RefreshToken


def custom_to_representation(instance):
    refresh = RefreshToken.for_user(instance)
    return {
        'user': {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
        },
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }