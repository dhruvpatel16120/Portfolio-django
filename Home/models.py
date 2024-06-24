from django.db import models

class SEO_tag(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Type_words(models.Model):
    tags = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.tags
    
class Description(models.Model):
    choice=(
        ('About','About'),
        ('Facts','Facts'),
        ('Skills','Skills'),
        ('Services','Services'),
        ('Resume','Resume'),
        ('Portfolio','Portfolio'),
        ('Contact','Contact'),
        ('Recommendation&Review','Recommendation&Review'),
    )
    title= models.CharField(max_length=220,choices=choice)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Fact(models.Model):
    title= models.CharField(max_length=220)
    icon= models.CharField(max_length=220)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title= models.CharField(max_length=220)
    icon= models.CharField(max_length=220)
    delay_ms = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    skill = models.CharField(max_length=220)
    percent = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.skill

class Testimonial(models.Model):
    name = models.CharField(max_length=220)
    occupation = models.CharField(max_length=220)
    image = models.CharField(max_length=220)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
