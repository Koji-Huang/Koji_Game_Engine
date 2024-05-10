class Script:
    flags: dict
    compile_source: any
    run_result: dict[str: [...]]
    source: str
    record_back: bool

    def __init__(self):
        """
        Script Object
        """
        pass

    def write(self, string):
        """
        Write in word to Script
        """
        pass

    def check(self):
        """
        Check the script is available.
        """
        pass

    def run(self):
        """
        Run The Script.
        """
        pass

    def result(self):
        """

        """
        pass

    pass


"""
    Asset Config Environment Be like:
        txt:
            name:
            path:
            sub:
            
            environment: ....
            
            @@@
            ... ( Write Code here)
            @@@


        ini:
            [asset]:
                ...
            
            [script_name]:
                environment = ...
                code = @@@
                ...
                @@@

        json:
            json format cannot record code. It can only used as control machine
            
            "__asset__" = {
                ...
            },
            
            "ScriptName" = file: str = ...
            
"""
