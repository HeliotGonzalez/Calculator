import os
class update:
    def __init__(self):
        self.remove_files()
        self.download_files()
        self.run_script()
    
    def remove_files():
        os.remove("vcc.py")

    def download_files():
        response = requests.get(
        'https://raw.githubusercontent.com/thetiger21/Calculator/refs/heads/main/calculator/vcc.py',
        auth=('user', 'pass')
        )
    def run_script():
        try:
            response = requests.get(
            'https://raw.githubusercontent.com/thetiger21/Calculator/refs/heads/main/calculator/script.py',
            auth=('user', 'pass')
            )
            import script
            script.run()
        except:
            print("No custom script. Don't worry about it, the developer has not put it.")  