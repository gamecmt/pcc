# 9-10
from newrestanurant import NewRestaurant
from admin import Admin

restannurant = NewRestaurant('mid', 'Franch')
restannurant.describe_restaurant()

# 9-11

admin_user = Admin('chen', 'mid')
admin_user.privileges.show_privileges()
