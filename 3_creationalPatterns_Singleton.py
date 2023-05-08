'''

    Design Pattern 3: Creational Pattern - Singleton.

'''

class ApplicationState:

    instance = None

    def __init__(self):
        self.isLoggedIn = False
    
    @staticmethod
    def getAppState():
        # Create an instance if there's no instance. 
        # This make sure there's only one instance no matter how many variables refer to this class.
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return  ApplicationState.instance

if __name__ == '__main__':
    appState_1 = ApplicationState.getAppState()
    print(appState_1.isLoggedIn)    # False

    appState_2 = ApplicationState.getAppState()
    print(appState_2.isLoggedIn)    # False

    appState_1.isLoggedIn = True
    print(appState_1.isLoggedIn)    # True
    print(appState_2.isLoggedIn)    # True
    
    '''

        'appState_1.isLoggedIn' and 'appState_2.isLoggedIn' will be 'True' if one of them is set as 'True'.
        This means there is only "one" instance that appState_1 and appState_2 refer to.

    '''