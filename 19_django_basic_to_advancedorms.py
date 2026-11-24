a = Author.objects.create(name="Rk narayan ", country="India")

# to update things

b = Book(title="Malgudi Days", author=a, price=250)
b.save()


Book.ojects.bulk_create(
    [  # ONE insert for many rows
        Book(title="Swami", author=a, price=199),
        Book(title="The Guide", author=a, price=299),
    ]
)


author, created = Author.objects.get_or_create(
    name="ruskin_bond", defaults={"country": "India"}
)

obj, created = Author.objects.update_or_create(
    name="Ruskin Bond", defaults={"country": "India"}
)  # gets and updates, or creates


book.objects.all()
book.objects.get(id=1)
book.objects.filter(is_available=True)
book.objects.exclude(is_available=True)
book.objects.order_by("price")
book.objects.order_by("-price")
book.objects.all()[:5]
book.objects.first()
book.objects.count()
book.objects.filter(price__gt=500).exists()


# lookups into data
book.objects.filter(price__gt=50)
book.objects.filter(price__gte=50)
book.objects.filter(price__lt=50)
book.objects.filter(price__lte=50)
book.objects.filter(price__range(200, 400))
book.objects.filter(title__contains="Guide")  # exactly search for Guide
book.objects.filter(title__icontains="guide")  # case incsensitive most used
book.objects.filter(id__in=[1, 2, 3])
book.objects.filter(published_on__year=2020)


# using and queires AND AND AND USE .FILTER () .FILTER CHAIN OR USE ',' IN BRACKET
Book.objects.filter(is_available=True, price__lt=300)
Book.objects.filter(is_available=True).filter(price__lt=300)  # same


#### filter can only do AND


### for OR queries use the Q (OR,NOT ) and f expressions


from django.db.models import Q


book.objects.filter(Q(price__lt=200) | Q(pages__gt == 500))

book.objects.filter(Q(is_available=True) & ~Q(price__gt=500))


b = Book.objects.get(id=1)
b.price = 300
b.save()  # updates ALL columns of this row
b.save(update_fields=["price"])  # updates only price (better)

Book.objects.filter(author=a).update(is_available=False)  # one UPDATE for many rows
Book.objects.filter(is_available=False).delete()  # DELETE ... WHERE


### the n+1 problem first use the 1 query
books = Book.objects.all()  # 1 query
for b in books:
    print(b.author.name)  # n queries  extra query PER BOOK to find the nth data

## to fix this use the select related
# it brings the data of author also with object in oneplace

books = Book.objects.select_realted("author")


for b in books:
    print(b.author.name)


# for saving memory


Book.objects.iterator(chunk_size=2000)  # for huge tables, avoids loading all in memory
