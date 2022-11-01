
import boto3

# run it to see how many more objects need to be classified
# sometimes we get down into 12 or so and... oh... as i'm typing this i wonder if we're being throttled by textract
# anyways, if it hangs, you may want to delete the remaining rows that don't have a class assigned to it to get the function to complete
dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table(f'DatasetCSVTable_20221101021618_logix-docsplitter-training_')

scan_kwargs = {
    'Select': 'COUNT',
    'FilterExpression': 'attribute_not_exists(#cls)',
    'ExpressionAttributeNames': {'#cls': 'class'}
}

done = False
start_key = None
rows_not_filled = 0
while not done:
    if start_key:
        scan_kwargs['ExclusiveStartKey'] = start_key
    response = table.scan(**scan_kwargs)
    rows_not_filled += response['Count']
    start_key = response.get('LastEvaluatedKey', None)
    done = start_key is None

if rows_not_filled == 0:
    print(f'dun')
else:
    print(f'not dun {rows_not_filled}')