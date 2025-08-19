import json

result = {
    "success": True,
    "exit_code": 0,
    "stack": [{"type": "num", "num": "0x6c465e2e4742515ed304d4f2c5ff19b9491867476de5cabbcc17d95a2bc8a496"}],
    "decoded": {
        "public_key": "48974116953345856140181965550413085949156742768025957073441247959872919086230"
    }
}

print(json.dumps(result, indent=4))
