from flask import Flask, jsonify, request
import boto3

app = Flask(__name__)

# Initialize DynamoDB Local client
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Create a DynamoDB table by giving your table the name you want with your requirements
table = dynamodb.create_table(
    TableName='YourTablename',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'  # Number data type for id
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName='MyTable')

# Sample route for getting all items from DynamoDB
@app.route('/items', methods=['GET'])
def get_items():
    items = table.scan()['Items']
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
