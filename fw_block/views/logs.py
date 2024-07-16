from datetime import datetime
from typing import Any
from django.utils.timezone import make_aware
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView

from fw_block.models import BlockedLogs
from fw_block.models.blocked_logs import Actions


class LogView(PermissionRequiredMixin, ListView):

    permission_required = "fw_block.view_blockedlogs"
    paginate_by = 100
    model = BlockedLogs
    template_name = "pages/logs.html"

    def get_queryset(self) -> QuerySet[Any]:

        q = self.request.GET.get("q") or ""

        avaible_actions = {
            "block": Actions.block,
            "unblock": Actions.unblock,
            "any": "any",
        }

        action = avaible_actions.get(self.request.GET.get("action"))

        if not self.request.GET.get("date-range"):

            return BlockedLogs.objects.none()

        date_range = self.request.GET.get("date-range").split(" a ")

        start_date = date_range[0]
        end_date = date_range[1]

        start_date = make_aware(datetime.fromisoformat(start_date))
        end_date = make_aware(datetime.fromisoformat(end_date))

        result = (
            BlockedLogs.objects.filter(user__username__icontains=q)
            | BlockedLogs.objects.filter(ip__ip__icontains=q)
            | BlockedLogs.objects.filter(firewall__name__icontains=q)
        ).filter(datetime__range=(start_date, end_date))

        if action != "any":
            result = result.filter(action=action)

        return result
