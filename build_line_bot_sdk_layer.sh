mkdir python

cd python

pip install --target . line-bot-sdk 

cd ..

zip -r line-bot-sdk.zip ./python

rm -rf ./python

echo "Created line-bot-sdk.zip"
