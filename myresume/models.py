from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='中文名')
    username_eng = models.CharField(max_length=60, verbose_name='英文名')
    phone_number = models.CharField(max_length=20, verbose_name='联系方式')
    email = models.EmailField(verbose_name='电子邮箱')
    github = models.CharField(max_length=100, verbose_name='Github账号')

    def __str__(self):
        return f"{self.username}/{self.username_eng}"


class Section(models.Model):
    section_name = models.CharField(max_length=30)
    section_name_eng = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.section_name}/{self.section_name_eng}"


class Subsection(models.Model):
    subsection_name = models.CharField(max_length=100)
    subsection_name_eng = models.CharField(max_length=100)
    by_section = models.ForeignKey(Section, on_delete='CASCADE')
    period = models.CharField(max_length=30, blank=True)
    period_eng = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.by_section}[{self.id}]"


class Item(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=256)
    title_eng = models.CharField(max_length=200)
    text_eng = models.CharField(max_length=512)
    by_subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.by_subsection}[{self.title}]"


class Entry(models.Model):
    text = models.CharField(max_length=256)
    text_eng = models.CharField(max_length=512)
    by_subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.by_subsection}"
