from django.urls import path
from main.views import register_ajax, login_ajax,register,login_user,logout_user,show_main, create_product,add_product_entry_ajax, delete_product_ajax,edit_product, edit_product_entry_ajax, delete_product,show_product, show_xml, show_json,show_xml_by_id,show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-product/', create_product, name='create_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('product/<uuid:id>/edit-product-ajax', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
]

