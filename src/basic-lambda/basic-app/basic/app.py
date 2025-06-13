import json
import debugpy

# 5678 is the default Python debug port
debugpy.listen(("0.0.0.0", 5678))
print("⏱ Waiting for debugger attach on port 5678…")
debugpy.wait_for_client()
print("⏱ Debugger was attached")

def lambda_handler(event, context):

    first_name = event['first_name']
    last_name = event['last_name']
    message = event['message']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{message} {first_name} {last_name}",
        }),
    }
