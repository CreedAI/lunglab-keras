from datetime import datetime


class Config:

    def __init__(self, **kwargs):
        self._parse(kwargs)
        self.today = datetime.today()

        # self.path = os.path.join(WEIGHTS_PATH, self.BASE,
        #                          self.today.strftime("%y%m%d%H%M%S"))

    def _parse(self, setting):
        user_dict = self._user_dict
        for k, v in setting.items():
            if k not in user_dict:
                raise ValueError('Invalid Option: "--%s"' % k)
            src_value = getattr(self, k)
            setattr(self, k, type(src_value)(v))
            print("Setting `%s`: %s->%s" % (k, src_value, getattr(self, k)))

    @property
    def _user_dict(self):
        return {k: getattr(self, k) for k in dir(self)
                if not k.startswith('_')}


if __name__ == '__main__':

    import fire

    class UserConfig(Config):
        sth = "ddd"

    def main(**kwargs):
        cfg = UserConfig(**kwargs)
        print(cfg._user_dict)
        print(cfg.sth)
        print(type(cfg.sth))

    # double(3)
    # fire.Fire(cfg)
    # fire.Fire(Calculator)

    fire.Fire(main)
