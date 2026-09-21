import os

def create_folder(path):
    isExist = os.path.exists(path) 
    if not isExist:
        os.makedirs(path)


# Write a function to convert time
def sec_to_min_and_sec(sec):
    if sec>=0:
        output_min = round(sec//60)
        output_sec = round(sec%60)
        return str(output_min) + ' min ' + str(output_sec) +' sec'
    else:
        sec = -sec
        output_min = round(sec//60)
        output_sec = round(sec%60)
        return '-' + str(output_min) + ' min ' + str(output_sec) +' sec'