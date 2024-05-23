def __getattr__(name):
    match name:
        case "Asset" | "AssetAPI":
            from Asset import AssetManagement as AssetAPI
            return AssetAPI
        case "Config" | "ConfigAPI":
            from Config import ConfigManagement as ConfigAPI
            return ConfigAPI
        case "Event" | "EventAPI":
            from Event import EventManagement as EventAPI
            return EventAPI
        case "Graphic" | "GraphicAPI":
            from Graphic import GraphicManagement as GraphicAPI
            return GraphicAPI
        case "Thread" | "ThreadAPI":
            from Thread import ThreadManagement as ThreadAPI
            return ThreadAPI
        case "Global" | "GlobalAPI":
            import Global as GlobalAPI
            return GlobalAPI
