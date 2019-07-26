from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from core import views as myapp_views


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
friends = router.register(r"friends", myapp_views.FriendViewset)
friends.register(
    r"borrowings",
    myapp_views.BorrowedViewset,
    basename="friend-borrow",
    parents_query_lookups=["to_who"],
)
router.register(r"belongings", myapp_views.BelongingViewset)
router.register(r"borrowings", myapp_views.BorrowedViewset)
