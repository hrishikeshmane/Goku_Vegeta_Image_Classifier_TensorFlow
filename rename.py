import os

def main(): 
    path = 'C:/Users/ihrishi/Desktop/files/tensorflow-for-poets-2/train_dataset/Vegeta'
    #path='C:/Users/ihrishi/Desktop/files/tensorflow-for-poets-2/train_dataset/png'
    files = os.listdir(path)


    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, 'V'+str(index)+'.jpg'))
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 