import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit

active_passcard = Passcard.objects.filter(is_active=True)

if __name__ == '__main__':
    # Получаем только активные пропуска
    active_passcards = Passcard.objects.filter(is_active=True)

    # Выводим информацию
    print('Количество пропусков:', Passcard.objects.count())
    print('Активных пропусков:', active_passcards.count())
    print()
    print('Получите визиты пользователей', Visit.objects.all())
    print()
    print('Пользователи в хранилище', Visit.objects.filter(leaved_at__isnull=True))
    print()
    # Выводим информацию о первом активном пропуске
    first_active_passcard = active_passcards.first()
    print(f"owner_name: {first_active_passcard.owner_name}")
    print(f"passcode: {first_active_passcard.passcode}")
    print(f"created_at: {first_active_passcard.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    print(f"is_active: {first_active_passcard.is_active}")
    print()
    # Сколько времени посетители провели в хранилище
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in active_visits:
        entered_at = timezone.localtime(visit.entered_at)
        now = timezone.localtime(timezone.now())
        duration = now - entered_at
        print(f'Зашёл в хранилище, время по Москве: {entered_at}')
        print(f'Находится в хранилище: {duration}')





