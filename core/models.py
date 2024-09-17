from django.db import models

from stdimage.models import StdImageField

# importante - fazer migrates depois de finalizar models-
#SIGNALS
from django.db.models import signals #signals - antes de colocar algo no BD faz algo - Depois de colocar algo no BD faz algo

from django.template.defaultfilters import slugify # slugify cria um slug com os titulos da pagina

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modeficado = models.DateField('Data de Modificação', auto_now=True)
    ativo = models.DateField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)

    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    estoque = models.IntegerField('Estoque')

    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    
    slug = models.SlugField('Slug', max_length=100,blank=True, editable=False)

    def __str__(self):
        return self.nome
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)