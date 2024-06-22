import boto3


def connect_table(tablename):
    """ Create a DynamoDB session and connect to table """
    
    session = boto3.Session()
    dynamodb = session.resource('dynamodb')
    return dynamodb.Table(tablename)


def get_all_items(tablename):
    """ Get all items from DynamoDB table """
    
    table = connect_table(tablename)
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    return data


def save_item(tablename, item):
    """ Save item to DynamoDB table """
    
    table = connect_table(tablename)
    return table.put_item(Item=item)


def update_item(tablename, primarykey_name, primarykey_value, sortkey_name, sortkey_value, attribute_name, attribute_value):
    """ Update item with a given primary key in DynamoDB table """

    table = connect_table(tablename)
    return table.update_item(
        Key={
            primarykey_name: primarykey_value,
            sortkey_name: sortkey_value
        },
        UpdateExpression='SET #attrName = :attrValue',
        ExpressionAttributeNames={
            '#attrName': attribute_name
        },
        ExpressionAttributeValues={
            ':attrValue': attribute_value
        },
        ReturnValues='UPDATED_NEW'
    )


if __name__ == '__main__':
    
    print(get_all_items('Employees'))