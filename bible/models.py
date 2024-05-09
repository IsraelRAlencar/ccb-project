from django.db import models


class Livros(models.Model):
    liv_id = models.AutoField(primary_key=True)
    liv_tes_id = models.PositiveIntegerField()
    liv_posicao = models.PositiveIntegerField()
    liv_nome = models.CharField(max_length=30)
    liv_abreviado = models.CharField(max_length=3)

    class Meta:
        db_table = 'livros'
        unique_together = (('liv_tes_id', 'liv_posicao'),)


class Testamentos(models.Model):
    tes_id = models.AutoField(primary_key=True)
    tes_nome = models.CharField(max_length=30)

    class Meta:
        db_table = 'testamentos'


class Versoes(models.Model):
    vrs_id = models.AutoField(primary_key=True)
    vrs_nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'versoes'


class Versiculos(models.Model):
    ver_id = models.AutoField(primary_key=True)
    ver_vrs_id = models.ForeignKey(
        Versoes,
        on_delete=models.DO_NOTHING,
        db_column='vrs_id',
    )
    ver_liv_id = models.ForeignKey(
        Livros,
        on_delete=models.DO_NOTHING,
        db_column='liv_id',
    )
    ver_capitulo = models.PositiveIntegerField()
    ver_versiculo = models.PositiveIntegerField()
    ver_texto = models.TextField()

    class Meta:
        db_table = 'versiculos'
