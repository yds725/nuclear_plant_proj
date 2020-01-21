import pandas as pd
import numpy as np

def add_id_column(df, file_id):
    
    id_dataframe = pd.DataFrame({'id' : [file_id for i in range(df.shape[0])]})

    df = pd.concat([id_dataframe, df], axis=1)
    
    return df

def data_loader(path, train, nrows, **kwargs):
    
    '''
    Parameters:
    
    path: [str] train용 또는 test용 csv 파일들이 저장되어 있는 폴더 
    train: [boolean] train용 파일들 불러올 시 True, 아니면 False
    nrows: [int] csv 파일에서 불러올 상위 n개의 row 
    lookup_table: [pd.DataFrame] train_label.csv 파일을 저장한 변수 
    event_time: [int] 상태_B 발생 시간 
    normal: [int] 상태_A의 라벨
    
    Return:
    
    data: train 또는 test data
    '''
    
    
    # 1. 해당 파일 경로에서 확장자 제외한 파일 이름만 가지고 오기 
    file_id = int(path.split('/')[-1].split('.')[0])
    
    # 2. train일 경우
    if train : 
        
        # 2-1 label 정보 저장
        lookup_table = kwargs['lookup_table']

        file_label = int(lookup_table[lookup_table['id'] == file_id]['label'])
        
        # 2-2 파일 읽기 
        data = pd.read_csv(path, nrows = nrows)
        
        # 2-3 id컬럼 추가 
        data = add_id_column(data, file_id)
        
        # 2-3 label컬럼 추가 
        event_time = kwargs['event_time']

        data['label'] = np.concatenate((np.repeat(kwargs['normal'], event_time), np.repeat(file_label, data.shape[0]-event_time)))

    # 3. test일 경우 
    else : 
        
        # 3-1 파일 읽기
        data = pd.read_csv(path, nrows = nrows)
        
        # 3-2 id컬럼 추가 
        data = add_id_column(data, file_id)
        
    return data

