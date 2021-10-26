class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production Configuration child class

    Args:
         Config:The parent configuration class with general configuration setttings

    '''
    pass    
class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    DEBUG = True