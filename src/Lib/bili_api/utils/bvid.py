from ..exceptions.BiliVideoIdException import BiliVideoIdException


def check_bvid(bvid: str) -> None:
    if len(bvid) != 12:
        raise BiliVideoIdException('Formato de bvid incorrecto: debe tener 12 caracteres')
    if bvid[:2].upper() != 'BV':
        raise BiliVideoIdException('Formato de bvid incorrecto: debe empezar con BV')
