from aiohttp.web import Application # noqa
from .product import product_fields
from aiohttp import web  # noqa
from .data_service import get_data
from json.decoder import JSONDecodeError


async def profiling_route(_):
    from aiohttp import web # noqa
    from .data_service import get_data
    import time
    from asyncio import sleep
    times = []
    for i in range(10):
        t1 = time.time()
        res = await get_data()
        t2 = time.time()
        print("Overall", len(res), t2-t1)
        times.append(t2-t1)
        await sleep(0.5)
    print(sum(times)/10, "Mean time")
    return web.Response(text=str(dict(res._asdict()))) # noqa


async def main_processing(request):
    # Getting request params as json
    try:
        request_data = await request.json()
        try:
            if request_data['sort_key'] in product_fields:
                sort_key = request_data['sort_key']
            else:
                raise KeyError
        except KeyError:
            sort_key = "cost"

        try:
            if request_data['asc'].lower() in ["true", "false"]:
                ascending = request_data['asc'].lower() == "true"
            else:
                raise KeyError
        except KeyError:
            ascending = False
        except ValueError:
            ascending = False

    except JSONDecodeError:
        ascending = False
        sort_key = "cost"

    res = await get_data()
    res_dict = list(map(lambda x: dict(x._asdict()), res)) # noqa
    res_sorted = sorted(res_dict, key=lambda x: x[sort_key], reverse=ascending)
    data = {
        "products":  res_sorted
    }
    return web.json_response(data) # noqa


def setup_routes(app: Application):
    # app.router.add_get('/profiling_route', profiling_route)
    app.router.add_post('/parse_data', main_processing)
