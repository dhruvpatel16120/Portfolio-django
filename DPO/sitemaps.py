# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'home',
        ]

    def location(self, item):
        return reverse(item)
