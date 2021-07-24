from datetime import datetime
from urllib.parse import urlunparse, urlencode
import requests

from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import UserProfile

import logging

logger = logging.getLogger(__name__)


def save_user_profile_vk(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode({'fields': ','.join(('bdate', 'sex', 'about')),
                                     'access_token': response['access_token'],
                                     'v': '5.92'}),
                          None
                          ))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = timezone.now().date().year - bdate.year

        if age < 18:
            user.delete()
            logger.info(f'Пользователю {user.username} запрещена авторизация, '
                        f'т.к. его возраст не соответствует требованиям')
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.birthday = bdate

    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    user.save()


def save_user_profile_google(backend, user, response, *args, **kwargs):
    if backend.name != 'google-oauth2':
        return

    api_url = urlunparse(('https',
                          'people.googleapis.com',
                          f'/v1/people/{response["sub"]}',
                          None,
                          urlencode({'personFields': ','.join(('birthdays', 'biographies', 'genders'))}),
                          None
                          ))

    resp = requests.get(api_url, headers={
        'Authorization': f'Bearer {response["access_token"]}'
    })

    if resp.status_code != 200:
        return

    data = resp.json()

    if data['birthdays']:
        bdate = data['birthdays'][0]['date']
        bdate = datetime(day=bdate['day'], month=bdate['month'], year=bdate['year'])
        age = timezone.now().date().year - bdate.year

        if age < 18:
            user.delete()
            logger.info(f'Пользователю {user.username} запрещена авторизация, '
                        f'т.к. его возраст не соответствует требованиям')
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.birthday = bdate

    if data['genders']:
        gender = data['genders'][0]['value']

        user.userprofile.gender = UserProfile.MALE if gender == 'male' else UserProfile.FEMALE

    user.save()


def save_user_profile_yandex(backend, user, response, *args, **kwargs):
    if backend.name != 'yandex-oauth2':
        return

    if response['birthday']:
        bdate = datetime.strptime(response['birthday'], '%Y-%m-%d')
        age = timezone.now().date().year - bdate.year

        if age < 18:
            user.delete()
            logger.info(f'Пользователю {user.username} запрещена авторизация, '
                        f'т.к. его возраст не соответствует требованиям')
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.birthday = bdate

    if response['sex']:
        user.userprofile.gender = UserProfile.MALE if response['sex'] == 'male' else UserProfile.FEMALE

    if response['login']:
        user.username = response['login']

    user.save()
