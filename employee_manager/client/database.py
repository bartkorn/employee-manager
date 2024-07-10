import boto3
from typing import Any, Dict


def connect_table(table_name: str) -> Any:
    """ Create a DynamoDB session and connect to table """
    
    session = boto3.Session()
    dynamodb = session.resource('dynamodb')
    return dynamodb.Table(table_name)


def get_all_items(table_name: str) -> Any:
    """ Get all items from DynamoDB table """
    
    table = connect_table(table_name)
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    return data


def get_item(table_name: str, primary_key_name: str, primary_key_value: any, sort_key_name: str, sort_key_value: any) -> any:
    """ Get item with a given primary key in DynamoDB table """

    table = connect_table(table_name)
    return table.get_item(Key={
        primary_key_name: primary_key_value,
        sort_key_name: sort_key_value
    })


def save_item(table_name: str, item: Dict) -> Any:
    """ Save item to DynamoDB table """
    
    table = connect_table(table_name)
    return table.put_item(Item=item)


def update_item(table_name: str, primary_key_name: str, primary_key_value: any, sort_key_name: str, sort_key_value: any, attribute_name: str, attribute_value: any) -> Any:
    """ Update item with a given primary key in DynamoDB table """

    table = connect_table(table_name)
    return table.update_item(
        Key={
            primary_key_name: primary_key_value,
            sort_key_name: sort_key_value
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


def delete_item(table_name: str, primary_key_name: str, primary_key_value: any, sort_key_name: str, sort_key_value: any) -> any:
    """ Delete item with a given primary key from DynamoDB table """

    table = connect_table(table_name)
    return table.delete_item(Key={
        primary_key_name: primary_key_value,
        sort_key_name: sort_key_value
    })


if __name__ == '__main__':
    
    print(get_all_items('Employees'))