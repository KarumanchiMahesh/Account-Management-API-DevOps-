import subprocess

def update_amount_status(id, amount):

    proc=subprocess.run('bash app.sh %s %d'%(id, amount), shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.strip().decode('ascii')
    if(output == '-1'):
        return dict({'balance':-1,'status':404})
    else:
        return dict({'balance': int(output),'status':200})

def get_account_balance(account_id):
    proc=subprocess.run('bash app.sh %s'%(account_id), shell=True, stdout=subprocess.PIPE)
    output = proc.stdout.strip().decode('ascii')
    if(output == '-1'):
        return dict({'balance':-1,'status':404})
    else:
        return dict({'balance': int(output),'status':200})