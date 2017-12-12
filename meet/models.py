from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)


class MeetingRoom(models.Model):
    title = models.CharField(verbose_name='会议室', max_length=32)


class Booking(models.Model):
    user = models.ForeignKey(verbose_name='用户', to='UserInfo')

    room = models.ForeignKey(verbose_name='会议室', to='MeetingRoom')

    booking_date = models.DateField(verbose_name='预定日期')
    # time_choices = (
    #     (1, '8:30 - 9:00'),
    #     (2, '9:00 - 9:30'),
    #     (3, '9:30 - 10:00'),
    #     (4, '10:00 - 10:30'),
    #     (5, '10:30 - 11:00'),
    #     (6, '11:00 - 11:30'),
    #     (7, '11:30 - 12:00'),
    #     (8, '12:00 - 12:30'),
    #     (9, '12:30 - 13:00'),
    #     (10, '13:00 - 13:30'),
    #     (11, '13:30 - 14:00'),
    #     (12, '14:00 - 14:30'),
    #     (13, '14:30 - 15:00'),
    #     (14, '15:00 - 15:30'),
    #     (15, '15:30 - 16:00'),
    #     (16, '16:00 - 16:30'),
    #     (17, '16:30 - 17:00'),
    #     (18, '17:00 - 17:30'),
    #     (19, '17:30 - 18:00'),
    #     (20, '18:00 - 18:30'),
    #     (21, '18:30 - 19:00'),
    #     (22, '19:00 - 19:30'),
    #     (23, '19:30 - 20:00'),
    #     (24, '20:00 - 20:30'),
    # )

    time_choices = (
        (1, '8:00'),
        (2, '9:00'),
        (3, '10:00'),
        (4, '11:00'),
        (5, '12:00'),
        (6, '13:00'),
        (7, '14:00'),
        (8, '15:00'),
        (9, '16:00'),
        (10, '17:00'),
        (11, '18:00'),
        (12, '19:00'),
        (13, '20:00'),
    )
    booking_time = models.IntegerField(verbose_name='预定时间段', choices=time_choices)

    class Meta:
        unique_together = (
            ('booking_date', 'booking_time', 'room')
        )
