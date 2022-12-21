from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [FedeOcampo.pythonanywhere.com.]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backend.mysql',
		'NAME': 'FedeOcampo$dbsql_1',
		'USER': 'FedeOcampo',
		'PASSWORD': '2y2son4!',
		'HOST': 'FedeOcampo.mysql.pythonanywhere-services.com',
	}
}
