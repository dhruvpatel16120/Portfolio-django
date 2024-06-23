from django.db import models

# Create your models here.
class Portfolio(models.Model):
    portfolio_category = models.CharField(max_length=100)
    portfolio_name = models.CharField(max_length=100)
    portfolio_image = models.CharField(max_length=220)
    portfolio_url = models.CharField(max_length=233,default=1)
    date = models.DateField()

    def __str__(self):
        return f"{self.portfolio_name}"

class PortfolioDetails(models.Model):
    portfolio_name = models.ForeignKey("Portfolio", verbose_name=("Portfolilo"), on_delete=models.CASCADE)
    portfolio_heading = models.CharField(max_length=255)
    portfolio_client = models.CharField(max_length=100)
    portfolio_project_date = models.DateField()
    portfolio_project_url = models.URLField()
    portfolio_title = models.CharField(max_length=255)
    portfolio_description = models.TextField()
    portfolio_image_1 = models.CharField(max_length=220)
    portfolio_image_2 = models.CharField(max_length=220)
    portfolio_image_3 = models.CharField(max_length=220)
    keywords = models.TextField(default="dhruvwebfolio")
    description = models.TextField(default="dhruv")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.portfolio_heading

