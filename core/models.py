from django.db import models


class GlitchedFiles(models.Model):
    name = models.CharField("Nome", max_length=125)
    original_file = models.ImageField("Imagem original")
    glitched_file = models.ImageField("Imagem vanellopelizada")
    size = models.PositiveIntegerField("Tamanho da parte do arquivo a ser vanellipelizado")
    times = models.PositiveIntegerField("Vezes em que o arquivo passará pela vanellopelização")
