from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class ProffyUser(Base):
    name = models.CharField('Nome', max_length=128)
    avatar = models.CharField('Avatar', max_length=164)
    whatsapp = models.CharField('Whatsapp', max_length=20)
    bio = models.CharField('Bio', max_length=256)

    def __str__(self):
        return self.name


class Class(Base):
    subject = models.CharField('Matéria', max_length=64)
    cost = models.DecimalField('Custo', max_digits=8, decimal_places=2)
    proffy_user = models.ForeignKey(ProffyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class ClassSchedule(Base):
    week_day = models.IntegerField('Dia da Semana')
    start_at = models.IntegerField('De')
    end_at = models.IntegerField('Até')
    klass = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.klass} {self.week_day}'


class Connection(Base):
    proffy_user = models.ForeignKey(ProffyUser, on_delete=models.CASCADE)
