import DataType.SystemComponent as SystemComponent


ID_Register = SystemComponent.IDRegisterObject()


def register_global_environment():
    global ID_Register, AssetManager, Registry

    # ID System
    from Thread import ThreadPackage as __ThreadFile
    _get, _recycle, _reset = ID_Register.customized('Thread', 'ThreadSystem')
    __ThreadFile._thread_id_get = _get
    __ThreadFile._thread_id_recycle = _recycle

    from Event import BasicEvent as __EventFile
    from Event import Management as __EventManager
    _get, _recycle, _reset = ID_Register.customized('Event', 'EventSystem')
    __EventFile._event_id_get = _get
    __EventFile._event_id_recycle = _recycle
    __EventManager._event_id_get = _get
    __EventManager._event_id_recycle = _recycle

    _get, _recycle, _reset = ID_Register.customized('Inspector', 'EventSystem')
    __EventFile._inspector_id_get = _get
    __EventFile._inspector_id_recycle = _recycle
    __EventManager._inspector_id_get = _get
    __EventManager._inspector_id_recycle = _recycle

    # Asset Type
    # from .Asset import AssetManagement
    # AssetManager.load_system_asset_type()
