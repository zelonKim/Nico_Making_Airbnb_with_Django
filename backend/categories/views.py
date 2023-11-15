from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



##############################


""" 
class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors) 
"""
    


""" 
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":   # django object -> JSON
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)   # 데이터가 여러 개일 경우에는 many=True를 지정해줘야 함.
        return Response(serializer.data)
    
    elif request.method == "POST":   # JSON -> django object
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            new_category = serializer.save()   # automatically, save() calls the serializer`s create() method 
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)
"""

        

#####################################




""" 
class CategoryDetail(APIView):
    def get_object(self, pk): # get a detail object
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
             
    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        print(serializer)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk), data=request.data, partial=True,)
        if serializer.is_valid():
           updated_category = serializer.save() 
           return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT) 
        """



""" 
@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound
        
    if request.method == "GET":    
        serializer = CategorySerializer(category) 
        return Response(serializer.data)
       
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data, partial=True,) # partial=True로 지정하면 일부 업데이트(PUT)가 가능함.
        if serializer.is_valid():
           updated_category = serializer.save() #  automatically, save() calls the serializer`s update() method 
           return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
        
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT) 
"""