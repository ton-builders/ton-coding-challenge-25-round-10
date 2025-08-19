import json

result = {
    "success": True,
    "exit_code": 0,
    "stack": [{"type": "num", "num": "0x2e605cbbf4f866c171b786810f8b6e45c880677e859dbcb1537afea708677637"}],
    "decoded": {
        "public_key": "20976648381021295821482341384242982069443317990273060235157745751163364931127"
    }
}

print(json.dumps(result, indent=4))
