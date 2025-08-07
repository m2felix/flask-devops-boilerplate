#!/bin/bash

echo "🧪 Running basic test..."

RESPONSE=$(curl -s http://localhost:5000)
if [[ "$RESPONSE" == *"Hello"* ]]; then
  echo "✅ Test passed!"
else
  echo "❌ Test failed."
  exit 1
fi

