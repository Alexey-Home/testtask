from django.contrib.auth.models import User

from .models import Profile, Products, Lessons


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_access_products(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            product = Profile.objects.values('products').filter(user=self.request.user)
            acces_product = [i["products"] for i in product]
            if acces_product[0] is None:
                acces_product = [1]
            acces_video = {}
            all_product = Products.objects.values("id")
            number_product = [i["id"] for i in all_product]
            for i in number_product:
                name_products = Products.objects.values('title').filter(pk=i)[0]
                if i in acces_product:
                    acces_video[name_products["title"]] = Lessons.objects.filter(products=i)
            context["content"] = acces_video
        else:
            context["content"] = {}
        context["all_product"] = Products.objects.all()
        return context

    def get_product_video(self, **kwargs):
        context = kwargs
        content = Lessons.objects.filter(products=context['id'])
        context['content'] = content
        return context

#prefetch_related
