from decimal import Decimal
from django.conf import settings
from product.models import Product

class Cart:
     def __init__(self, request):
          """
          Initalize the cart
          """
          self.session=request.session
          cart=self.session.get(settings.CART_SESSION_ID)

          if not cart:
               #save an empty cart in the session
               cart=self.session[settings.CART_SESSION_ID]={}

          self.cart=cart

     def add(self, item, quantity=1, override_quantity=False):
               """
               Add a product to the cart or update its quantity
               """
               product_id=str(item.id)
               if product_id not in self.cart:
                    self.cart[product_id]={'quantity':0, 'price':str(item.price)}
               if override_quantity:
                    self.cart[product_id]['quantity']=quantity
               else:
                    self.cart[product_id]['quantity'] += quantity

               self.save()
            
     def save(self):
               """
               Mark the session as 'modified' to make sure its saved
               """
               self.session.modified=True
     
     def remove(self, item):
           """
           Remove a product from the Cart
           """
           product_id=str(item.id)

           if product_id in self.cart:
                 del self.cart[product_id]
                 self.save()

     def __iter__(self):
           """
           Iterate over the items in the cart and get the products from the database
           """

           product_ids=self.cart.keys()
            #get the product objects and add them to the cart
           products=Product.objects.filter(id__in=product_ids)
           cart=self.cart.copy()

           for product in products:
                 cart[str(product.id)]['product']=product
           
           for item in cart.values():
                 item['price']=Decimal(item['price'])
                 item['total_price']=item['price']*item['quantity']

                 yield item

     def __len__(self):
            """
            Count all items in the cart
            """ 
            return sum(item['quantity'] for item in self.cart.values())
     
     
     def get_total_price(self):
           return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())



     def clear(self):
           # remove cart from the session
           del self.session[settings.CART_SESSION_ID]

           self.save()
               