from django.urls import path
from apps.business.api.views.general_views import CampusUnitListAPIView
from apps.business.api.views.business_viewsets import BusinessCreateAPIView, BusinessRetrieveUpdateDestroyAPIView 
"""BusinessRetrieveAPIView,BusinessDestroyAPIView,BusinessUpdateAPIView,BusinessCreateAPIView,BusinessViewSet"""
    

urlpatterns = [
    path("campus/", CampusUnitListAPIView.as_view(), name="campus"),
    path("business/", BusinessCreateAPIView.as_view(), name="business_list_create"),
    path("retrieve-update-destroy/<int:pk>/", BusinessRetrieveUpdateDestroyAPIView.as_view(), name="business_retrieve_update_destroy"),
    #path("business/list/", BusinessViewSet.as_view(), name="business_list"),
    #path("business/retrieve/<int:pk>/", BusinessRetrieveAPIView.as_view(), name="business_retrieve"),
    #path("business/create/", BusinessCreateAPIView.as_view(), name="business_create"),
    #path("business/destroy/<int:pk>/", BusinessDestroyAPIView.as_view(), name="business_destroy"),
    #path("business/update/<int:pk>/", BusinessUpdateAPIView.as_view(), name="business_update"),
]