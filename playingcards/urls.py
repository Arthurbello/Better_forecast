from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cards.views.home', name='home'),
    url(r'^clubs/$', 'cards.views.clubs', name='clubs'),
    url(r'^diamonds/$', 'cards.views.diamonds', name='diamonds'),
    url(r'^face/$', 'cards.views.face', name='face'),
    url(r'^new/$', 'cards.views.card_filters', name='filters'),
    url(r'^template/$', 'cards.views.templatetags', name='templatetags'),
    url(r'^templatefilters/$', 'cards.views.templatefilters', name='templatefilters'),
    url(r'^random/$', 'cards.views.random_cards', name='random_cards'),
    url(r'^profile/$', 'cards.views.profile', name='profile'),
    url(r'^newpage/$', 'cards.views.newpage', name='newpage'),
    url(r'^faq/$', 'cards.views.faq', name='faq'),
    url(r'^newrpage/$', 'cards.views.newrpage', name='newrpage'),
    url(r'^blackjack/$', 'cards.views.blackjack', name='blackjack'),
    url(r'^poker/$', 'cards.views.poker', name='poker'),
    url(r'^heartpage/$', 'cards.views.heartpage', name='heartpage'),
    url(r'^register/$', 'cards.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^war/$', 'cards.views.war', name='war'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)