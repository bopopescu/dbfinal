from fe import conf
from fe.access import seller, auth


# 注册新的卖家
def register_new_seller(user_id, password) -> seller.Seller:
    a = auth.Auth(conf.URL)
    code = a.register(user_id, password)
    assert code == 200
    s = seller.Seller(conf.URL, user_id, password)
    return s
