import pandas as pd

'''
Loading comma separated files into pandas dataframes
'''
class load_data(self):
    def __init__(self):
        
    def columns(self, columns):
        self.columns = columns 
    
    
    
def df_train():
    '''
    Load and modifying training set
    '''
    df = pd.read_csv('data/train.csv')
    df.set_index('PassengerId',inplace = True)
    
    # Remove Name
    #df = df[['Survived', 'Pclass','Sex',
    #         'Age', 'SibSp', 'Parch',
    #         'Ticket','Fare', 'Cabin', 'Embarked']]
    
    # Modify Embarked
    emb_dict = {'S':0, 'C':1, 'Q':2} 
    df.replace({"Embarked": emb_dict},inplace=True)
    return df

def df_test():
    '''
    Load test set
    '''
    df = pd.read_csv('data/test.csv')
    df.set_index('PassengerId',inplace = True)
    return df

def df_gender_submission():
    '''
    Example of submission file
    '''
    df = pd.read_csv('data/gender_submission.csv')
    df.set_index('PassengerId',inplace = True)
    return df
