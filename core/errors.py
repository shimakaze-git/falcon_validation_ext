# coding: utf-8

import falcon


class HTTPError(falcon.HTTPError):
    """
    HTTPError that stores a dictionary of validation error messages.
    バリデーションエラーメッセージの辞書を格納するHTTPErrorクラス
    """
    
    def __init__(self, status, errors=None, *args, **kwargs):
        self.errors = errors
        super(HTTPError, self).__init__(status, *args, **kwargs)

    def to_dict(self, *args, **kwargs):
        """
        Override `falcon.HTTPError` to include error messages in responses.

        レスポンス内にエラーメッセージに格納するために`falcon.HTTPError`をオーバーライドしてください。
        """
        ret = super(HTTPError, self).to_dict(*args, **kwargs)

        if self.errors is not None:
            ret['errors'] = self.errors

        return ret