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
        json:
            json format cannot record code. It can only used as control machine
            
            {
              "__file__": {
                "name": "undefined",
                "path": "undefined",
                "type": "Script"
              },
              "asset": {
                "name": "undefined",
                "path": "undefined",
                "type": "Script"
              },
              "Script": {
            
                "name": ["1"],
            
                "1": {
                  "name": "str",
                  "path": "str",
                  "flags": "str"
                },
                "...": {
            
                }
              }
            }
            
"""
