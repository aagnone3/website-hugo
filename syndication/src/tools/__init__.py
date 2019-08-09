from .dev import DevConverter, DevAPI
from .medium import MediumConverter, MediumAPI
from .twitter import TwitterConverter, TwitterAPI


api_factory = {
    'dev': (DevAPI, DevConverter),
    'medium': (MediumAPI, MediumConverter),
    'twitter': (TwitterAPI, TwitterConverter)
}
