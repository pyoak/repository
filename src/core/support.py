class Str:

    @staticmethod
    def padLeft(item, length, fill):
        if len(item) < length:
            raise NotImplementedError
        return item

    @staticmethod
    def padRight(item, length, fill):
        if len(item) < length:
            raise NotImplementedError
        return item

    @staticmethod
    def wrap(item, start, end = None):
        return f"{start}{item}{end if end != None else start}"

