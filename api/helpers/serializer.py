import jsonpickle


class Serializer:

    @staticmethod
    def serialize(object):
        return jsonpickle.encode(object, unpicklable=False)
