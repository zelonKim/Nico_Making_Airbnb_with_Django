from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    title="Filter by words" # 필터 제목
    parameter_name = 'potato' # 쿼리 파라미터명

    def lookups(self, request, model_admin): # lookups() shows filtering side bar and URL
        return [ 
            ("good", "Good"), # ("쿼리 파라미터값", "필터 항목")
            ("nice", "Nice"),
            ("awesome", "Awesome")
        ]
    
    def queryset(self, request, reviews): # queryset() shows filtered result on main screen  # 필터 항목에서 Good을 클릭한 경우,
        print(self.value()) # good  # 쿼리 파라미터값
        print(request.GET) # <QueryDict: {'potato': ['good']}>  # {'쿼리 파라미터명': ['쿼리 파라미터값']}
        print(reviews) # [<Review: ksz1860 / 5★>, <Review: ksz1860 / 4★>, <Review: ksd2475 / 3★>] # 모델의 전체 데이터
        return reviews 


    def queryset(self, request, reviews): # 필터 항목에서 Good을 클릭한 경우,
        word = self.value()
        if word:
            result =reviews.filter(payload__contains=word)  # 모델의 payload가 Good을 포함하고 있는 데이터
            print(result) # [<Review: ksd2475 / 3★>]
            return result
        else:
            return reviews







@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display= (
        "__str__",
        "payload",
    )

    list_filter=(
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
