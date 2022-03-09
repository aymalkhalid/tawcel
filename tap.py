import http.client

conn = http.client.HTTPSConnection("api.tap.company")

payload = "{\"amount\":1,\"currency\":\"KWD\",\"customer\":{\"first_name\":\"test\",\"middle_name\":\"\",\"last_name\":\"test\",\"phone\":{\"country_code\":\"92\",\"number\":\"3361901499\"},\"email\":\"testcgara@test.com\"},\"items\":[{\"name\":{\"en\":\"test\"},\"description\":{\"en\":\"test\"},\"image\":\"\",\"currency\":\"KWD\",\"amount\":1,\"quantity\":\"1\",\"discount\":{\"type\":\"P\",\"value\":0}}],\"tax\":[{\"description\":\"test\",\"name\":\"VAT\",\"rate\":{\"type\":\"F\",\"value\":1}}],\"shipping\":{\"amount\":1,\"currency\":\"KWD\",\"description\":{\"en\":\"test\"},\"address\":{\"recipient_name\":\"test\",\"line1\":\"sdfghjk\",\"line2\":\"oiuytr\",\"district\":\"hawally\",\"city\":\"hawally\",\"state\":\"hw\",\"zip_code\":\"30003\",\"po_box\":\"200021\",\"country\":\"kuwait\"}},\"metadata\":{\"udf1\":\"\",\"udf2\":\"\"},\"reference\":{\"invoice\":\"\",\"order\":\"\"}}"

headers = {
    'authorization': "Bearer sk_test_XKokBfNWv6FIYuTMg5sLPjhJ",
    'content-type': "application/json"
    }

conn.request("POST", "/v2/orders", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))