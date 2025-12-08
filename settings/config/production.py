from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# add this in the ALLOWED_HOSTS
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
        "OPTIONS": {
            "sslmode": os.getenv("POSTGRES_SSLMODE", "require"),  # database encryption
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production

# cors settings
CORS_ALLOWED_ORIGINS = []  # list of domain names that are to be allowed

# csrf settings - Required when using HTTPS, proxies, load balancers
CSRF_TRUSTED_ORIGINS = []  # list of domain names that are trusted

CORS_ALLOW_CREDENTIALS = True

# HTTPS & SSL enforcement - handle redirecting from http to https
# Redirect all HTTP → HTTPS
SECURE_SSL_REDIRECT = True
# Trust SSL from reverse proxy (Nginx, Load Balancer)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS — enable only after HTTPS confirmed working. Protects against protocol-downgrade & MITM attacks
SECURE_HSTS_SECONDS = 3600  # 1 hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies - Prevents session theft & XSS-cookie extraction
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # must remain False for browsers to send it
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"


# Clickjacking protection - Prevents UI redress, clickjacking attacks
X_FRAME_OPTIONS = "DENY"


# Referrer privacy - stops leaking sensitive urls
SECURE_REFERRER_POLICY = "strict-origin"

# Browser security headers - reduces MIME-sniffing attacks
SECURE_BROWSER_XSS_FILTER = True  # legacy browsers
SECURE_CONTENT_TYPE_NOSNIFF = True


# You can add other third party settings