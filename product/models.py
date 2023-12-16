from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['name']),
        ]
        verbose_name='Category'
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product:product_list_by_category', args=[self.slug])


class ArtSize(models.Model):
    size=models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Product(models.Model):
    AVAILABLE_SIZE=[
        ('SM','Small'),
        ('MD','Medium'),
        ('LG','Large'),
        ('XL','ExtraLarge'),
    ]
    category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%Y/%m/%d')
    image_1=models.ImageField(upload_to='products',blank=True, null=True)
    image_2=models.ImageField(upload_to='products',blank=True, null=True)
    image_3=models.ImageField(upload_to='products',blank=True, null=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    size=models.CharField(max_length=4, choices=AVAILABLE_SIZE)
    available_size=models.ForeignKey(ArtSize, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),

        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.id, self.slug])
    
    def save(self, *args, **kwargs):
        super().save(self, *args,**kwargs)
        self.slug=slugify(self.name)
    


class Exhibition(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('soldout', 'SoldOut'),
        ('cancel','Cancelled'),
    ]

    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='activity')
    description=models.TextField(blank=True)
    venue=models.CharField(max_length=100)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    publish=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')


    class Meta:
        ordering=['-title']
        verbose_name_plural='Exhibitions'
    
    def __str__(self):
        return self.title
    
    
    



class Testimonial(models.Model):
    name=models.CharField(max_length=65)
    designation=models.CharField(max_length=65, null=True, blank=True)
    image=models.ImageField(upload_to='testimonials/%Y/%m/%d')
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
