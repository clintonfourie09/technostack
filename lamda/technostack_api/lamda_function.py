def lambda_handler(event, context):
        try:
            category = event['queryStringParameters']['category']
            response = {
                'statusCode': 200,
                'body': f'Received category: {category}'
            }
            return response
        except Exception as e:
            error_response = {
                'statusCode': 400,
                'body': f'Error: {str(e)}'
            }
            return error_response