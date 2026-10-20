from django.db import migrations


def create_default_vip_seats(apps, schema_editor):
    VipSeat = apps.get_model('CineBoard', 'VipSeat')
    existing_numbers = set(
        VipSeat.objects.values_list('seat_number', flat=True)
    )
    VipSeat.objects.bulk_create([
        VipSeat(seat_number=seat_number)
        for seat_number in range(1, 11)
        if seat_number not in existing_numbers
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('CineBoard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_vip_seats,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
