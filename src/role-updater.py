import boto3
import json
import os
import urllib3
from distutils.version import StrictVersion

templateurl='https://s3-us-west-2.amazonaws.com/cloudconformity/CloudConformity.template'
cfresource=boto3.resource('cloudformation')
stackname=os.environ.get('ccstackname')
stack=cfresource.Stack(stackname)
stackparams=[
    {
        'ParameterKey': 'AccountId',
        'UsePreviousValue': True
    },
    {
        'ParameterKey': 'ExternalId',
        'UsePreviousValue': True
    }
]

def get_conformity_template_verion():
    http=urllib3.PoolManager()
    template=http.request('GET', templateurl)
    templatejson=json.loads(template.data.decode('utf-8'))['Outputs']['Version']
    for key, value in templatejson.items():
        print('The latest CloudConformity template version is: {}'.format(value))
        return(value)

def get_conformity_stack_version():
    stackoutputs=stack.outputs
    for o in stackoutputs:
        if o['OutputKey'] == 'Version':
            print('The CloudConformity stack version is: {}'.format(o['OutputValue']))
            return(o['OutputValue'])

def main(event, context):
    templateversion=get_conformity_template_verion()
    stackversion=get_conformity_stack_version()
    if StrictVersion(templateversion) > StrictVersion(stackversion):
        stack.update(TemplateURL=templateurl,UsePreviousTemplate=False,Parameters=stackparams,Capabilities=['CAPABILITY_NAMED_IAM'])
        print('The CloudConformity stack is out of date, updating the stack to: {}'.format(templateversion))
        return('The CloudConformity stack is out of date, updating the stack to: {}'.format(templateversion))
    else:
        print('The CloudConformity stack is already up to date, version: {}'.format(stackversion))
        return('The CloudConformity stack is already up to date, version: {}'.format(stackversion))

if __name__ == "__main__":
    main(event=None, context=None)