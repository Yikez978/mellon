from zope import interface

class IFlaskApplication(interface.Interface):
    """Marker for Flask application singleton"""

class IFlaskRestApiApplication(interface.Interface):
    """Marker for Flask Rest api singleton"""

class IFlaskRestApiPreprocessors(interface.Interface):
    """Marker for Flask Rest api preprocessor definition singleton"""

class IFlaskRestApiPostprocessors(interface.Interface):
    """Marker for Flask Rest api postprocessor definition singleton"""