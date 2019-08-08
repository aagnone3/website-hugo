from .dev import DevConverter, DevAPI
from .medium import MediumConverter, MediumAPI
from .twitter import TwitterConverter, TwitterAPI


api_factory = {
    'dev': DevAPI,
    'medium': MediumAPI,
    'twitter': TwitterAPI
}

converter_factory = {
    'dev': DevConverter,
    'medium': MediumConverter,
    'twitter': TwitterConverter
}
