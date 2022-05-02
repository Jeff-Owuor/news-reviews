class News_source:
    '''
    News class to define New Objects
    '''

    def __init__(self,source,content):
        self.source = source
        self.content = content
        
        
class News_article:
    def __init__(self,description,image,date_created):
        self.description = description
        self.image = image
        self.date_created = date_created