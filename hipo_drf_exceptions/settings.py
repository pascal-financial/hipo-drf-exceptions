from django.conf import settings as django_settings

HIPO_DRF_SETTINGS = getattr(django_settings, "HIPO_DRF_SETTINGS", {})

INTERNAL_SERVER_ERROR_FALLBACK_MESSAGE = HIPO_DRF_SETTINGS.get(
    "INTERNAL_SERVER_ERROR_FALLBACK_MESSAGE",
    _('Our servers are unreachable at the moment. Please try again a few minutes later.')
)
