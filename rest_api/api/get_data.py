import os

def makeFile(data, filename):
    if filename in os.listdir(os.path.join(os.path.dirname(__file__), '../')):
        with open(filename,'a') as fd:
            if filename == 'transaction_data.csv':
                fd.write(','.join([str(data['timestamp']), data['method'], data['url'], str(data['status_code']), str(data['latency'])])+'\n')
            if filename == 'usage_data.csv':
                fd.write(','.join([str(data['cpu']), str(data['ram'])])+'\n')

    else:
        with open(filename, 'a') as fd:
            if filename == 'transaction_data.csv':
                fd.write('timestamp,method,url,status_code,latency\n')
                fd.write(','.join([str(data['timestamp']), data['method'], data['url'], str(data['status_code']), str(data['latency'])])+'\n')
            if filename == 'usage_data.csv':
                fd.write('cpu(%),ram(bytes)\n')
                fd.write(','.join([str(data['cpu']), str(data['ram'])])+'\n')