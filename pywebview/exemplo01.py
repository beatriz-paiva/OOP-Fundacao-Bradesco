import webview

class Api:
   
    def sayHelloTo(self, name):
        response = {'message': 'Hello {0}!'.format(name)}
        return response



if __name__ == '__main__':
    


    webview.create_window('Survey Form', r'C:\Documentos\GitHub\OOP-Fundacao-Bradesco\pywebview\view\index.html', js_api = Api())
    webview.start()