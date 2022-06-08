from __future__ import annotations

from django.db import models


class Vps(models.Model):
    template = models.ForeignKey["OSTemplate"]("OSTemplate", models.CASCADE)

    def reinstall(self, template: OSTemplate):
        ...


class ConfigTemplate(models.Model):
    pass


class OSTemplate(ConfigTemplate):
    pass


class VPSTemplate(ConfigTemplate):
    pass


OSTemplate.objects.get()
