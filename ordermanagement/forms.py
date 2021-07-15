# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 20:27:18 2021

@author: ansari
"""

from django import forms
from .models import upload,addcart
  
class Uploadform(forms.ModelForm):
  
    class Meta:
        model = upload
        fields = ['id1','name','images', 'price','count']
    
class Add_cart(forms.ModelForm):
  
    class Meta:
        model = addcart
        fields = ['id2','name2','images2', 'price2','count2']
        
        
        
        
        
'''     
        raw = upload.objects.all()
    raw2 = addcart.objects.all()
    upload2 = addcart()
    print(raw2)
    if request.method == 'POST':
        form = Add_cart(request.POST, request.FILES)
        form1 = Uploadform(request.POST, request.FILES)
        id_del = request.POST['id_order']
        if form.is_valid():
            form.save()
        try:
            instance = raw.get(id1=id_del)
            if instance.count>0:
                raw = deepcopy(instance)
                raw.save()
                print(raw)
                instance.count -= 1
                instance.save()
        except upload.DoesNotExist:
            user = None
            
        form = Uploadform()
    return render(request, 'userhomepage.html', {'raw': raw})

'''