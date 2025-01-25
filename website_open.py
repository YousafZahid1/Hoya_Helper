import webbrowser

def website_opener(domain):
    try:
        domain = domain.lower().replace(" ", "")
        url = f'https://www.{domain}.com'
        
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False