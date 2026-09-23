import copy
from urllib.parse import urlsplit

from . import utils
from .exceptions.BiliVideoIdException import BiliVideoIdException
from .exceptions.NetWorkException import NetWorkException
from .utils.bvid import check_bvid
from .utils.fnval import FNVAL_PRESET
from .utils.passport import BiliPassport

API = utils.get_api(('bangumi',))


def get_bangumi_info(media_id: int):
    api = copy.deepcopy(API['info'])
    url = urlsplit(api['url'])
    params = api['params']
    params['media_id'] = media_id

    get = utils.network.get_data(
        scheme=url.scheme,
        host=url.netloc,
        method=api['method'],
        path=url.path,
        query=params
    )
    if get['code'] != 0:
        raise NetWorkException('Error al obtener la información de la serie:\n{0};\n{1};\n{2}'.format(
            get['code'],
            api['return']['code'].get(str(get['code']), 'Error desconocido'),
            get['message']
        ))
    return get['result']


def get_bangumi_detailed_info(season_id: int = None, ep_id: int = None, media_id: int = None):
    api = copy.deepcopy(API['detailed_info'])
    url = urlsplit(api['url'])
    params = api['params']
    info = None
    if media_id is not None and season_id is None and ep_id is None:
        info = get_bangumi_info(media_id)
        season_id = info['media']['season_id']
    if season_id is not None:
        params.pop('ep_id')
        params['season_id'] = season_id
    elif ep_id is not None:
        params.pop('season_id')
        params['ep_id'] = ep_id
    else:
        raise BiliVideoIdException('Debes indicar season_id o ep_id')

    get = utils.network.get_data(
        scheme=url.scheme,
        host=url.netloc,
        method=api['method'],
        path=url.path,
        query=params
    )
    if get['code'] != 0:
        raise NetWorkException('Error al obtener los detalles de la serie:\n{0};\n{1};\n{2}'.format(
            get['code'],
            api['return']['code'].get(str(get['code']), 'Error desconocido'),
            get['message']
        ))
    info = get_bangumi_info(get['result']['media_id']) if media_id is None else info
    return {'info': info, 'data': get['result']}


def get_bangumi_url(
        avid: int = None,
        bvid: str = None,
        cid: int = None,
        fnval: int = FNVAL_PRESET().default(),
        passport: BiliPassport = None
):
    api = copy.deepcopy(API["bangumi_url"])
    url = urlsplit(api["url"])
    params: dict = api["params"]
    params.pop("qn")
    params["fnval"] = fnval
    params["cid"] = cid
    params["fourk"] = 1
    if bvid is not None:
        check_bvid(bvid)
        params.pop("avid")
        params["bvid"] = bvid
    elif avid is not None:
        params.pop("bvid")
        params["avid"] = avid
    else:
        raise BiliVideoIdException("Debes indicar aid o bvid")
    header = {}
    if passport is not None:
        header["Cookie"] = passport.get_cookie()
    get: dict = utils.network.get_data(
        scheme=url.scheme,
        host=url.netloc,
        method=api["method"],
        path=url.path,
        query=params,
        header=header
    )

    if get["code"] != 0:
        raise NetWorkException("Error al obtener el enlace de la serie:\n{0};\n{1};\n{2};".format(
            get["code"],
            api["return"]["code"].get(get["code"], "Error desconocido"),
            get["message"]
        ))

    return get["result"]


def get_bangumi_url_v2(
        ep_id: int,
        ss_id: int,
        fnval: int = FNVAL_PRESET().default(),
        passport: BiliPassport = None
):
    api = copy.deepcopy(API["bangumi_url_v2"])
    url = urlsplit(api["url"])
    params = api["params"]
    if passport is None:
        params.pop("csrf")
    else:
        params["csrf"] = passport.get_data()["bili_jct"]
    body: dict = api["body"]
    # body.pop("exp_info")
    # body.pop("video_param")
    body["player_param"]["fnval"] = fnval
    body["video_index"]["ogv_episode_id"] = ep_id
    body["video_index"]["ogv_season_id"] = ss_id
    header = {}
    if passport is not None:
        header["Cookie"] = passport.get_cookie()
    get: dict = utils.network.get_data(
        scheme=url.scheme,
        host=url.netloc,
        method=api["method"],
        path=url.path,
        query=params,
        header=header,
        data=body,
        data_type=api["data_type"]
    )

    if get["code"] != 0:
        raise NetWorkException("Error al obtener el enlace:\n{0};\n{1};\n{2};".format(
            get["code"],
            api["return"]["code"].get(get["code"], "Error desconocido"),
            get["message"]
        ))

    return get["data"]
