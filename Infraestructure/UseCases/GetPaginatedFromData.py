"""
FelipedelosH
2026
"""
from Application.UseCases.IGetPaginatedFromData import IGetPaginatedFromData
from Domain.Entities.Response import Response
from Domain.Entities.Paginator import Paginator


class GetPaginatedFromData(IGetPaginatedFromData):
    def __init__(self):
        pass

    def execute(self, response: dict, page: int, page_size: int) -> Response:
        try:
            if not isinstance(response, dict):
                return Response.responsePaginated(False, {}, 0, None)

            if not response.get("success"):
                return Response.responsePaginated(False, {}, 0, None)

            data = response.get("data")

            if not data:
                return Response.responsePaginated(False, {}, 0, None)

            if page <= 0:
                page = 1

            if page_size <= 0:
                page_size = 8

            paged_data, total = self._paginate_data(data, page, page_size)

            paginator = Paginator(
                total=total,
                page=page,
                page_size=page_size
            )

            qty = len(paged_data) if hasattr(paged_data, "__len__") else 0

            return Response.responsePaginated(
                True,
                paged_data,
                qty,
                paginator.to_dict()
            )
        except:
            return Response.responsePaginated(False, {}, 0, None)

    def _paginate_data(self, data, page: int, page_size: int):
        start = (page - 1) * page_size
        end = start + page_size

        if isinstance(data, dict):
            items = list(data.items())
            total = len(items)
            paged_data = dict(items[start:end])
            return paged_data, total

        if isinstance(data, list):
            total = len(data)
            paged_data = data[start:end]
            return paged_data, total

        return {}, 0
