import webview

def open_browser(url):
    webview.create_window("Scalt Records for Desktop 1.0.0", url,)

if __name__ == '__main__':
    urls = [
        "https://sites.google.com/view/scalt-records",
    ]
    
    for url in urls:
        open_browser(url)
        
    webview.start()



