import os
from flask import Flask, request, redirect
import requests

app =Flask(__name__)

@app.route("/test",methods=['POST'])
def test_reply():
    webhook_type=request.args.get('webhook_type')
    if webhook_type == "muscat_delivery_1" and payment_type == "online":
        from_location=request.args.get('from_location')
        payment_type=request.args.get('payment_type')
        drop_off_location_1=request.args.get('drop_off_location_1')
        order_in_muscat=request.args.get('order_in_muscat')
        phone_number_1_to_sent_package_to=request.args.get('phone_number_1_to_sent_package_to')
        response = {"data":{"type":"text","text":"Order is " +" "+ order_in_muscat + " " }}
        return response
    elif webhook_type == "muscat_delivery_2":
        from_location=request.args.get('from_location')
        payment_type=request.args.get('payment_type')
        drop_off_location_1=request.args.get('drop_off_location_1')
        drop_off_location_2=request.args.get('drop_off_location_2')
        order_in_muscat=request.args.get('order_in_muscat')
        phone_number_1_to_sent_package_to=request.args.get('phone_number_1_to_sent_package_to')
        phone_number_2_to_sent_package_to=request.args.get('phone_number_2_to_sent_package_to')
        response = {"data":{"type":"text","text":"Order is " +" "+ order_in_muscat + " " }}
        return response
    elif webhook_type == "muscat_delivery_3":
        from_location=request.args.get('from_location')
        payment_type=request.args.get('payment_type')
        drop_off_location_1=request.args.get('drop_off_location_1')
        drop_off_location_2=request.args.get('drop_off_location_2')
        drop_off_location_3=request.args.get('drop_off_location_3')
        order_in_muscat=request.args.get('order_in_muscat')
        phone_number_1_to_sent_package_to=request.args.get('phone_number_1_to_sent_package_to')
        phone_number_2_to_sent_package_to=request.args.get('phone_number_2_to_sent_package_to')
        phone_number_3_to_sent_package_to=request.args.get('phone_number_3_to_sent_package_to')
        response = {"data":{"type":"text","text":"Order is " +" "+ order_in_muscat + " " }}
        return response
    elif webhook_type == "muscat_delivery_4":
        from_location=request.args.get('from_location')
        payment_type=request.args.get('payment_type')
        drop_off_location_1=request.args.get('drop_off_location_1')
        order_in_muscat=request.args.get('order_in_muscat')
        phone_number_1_to_sent_package_to=request.args.get('phone_number_1_to_sent_package_to')
        phone_number_2_to_sent_package_to=request.args.get('phone_number_2_to_sent_package_to')
        phone_number_3_to_sent_package_to=request.args.get('phone_number_3_to_sent_package_to')
        phone_number_4_to_sent_package_to=request.args.get('phone_number_4_to_sent_package_to')        
        response = {"data":{"type":"text","text":"Order is " +" "+ order_in_muscat + " " }}
        return response
    elif webhook_type == "muscat_delivery_5":
        from_location=request.args.get('from_location')
        payment_type=request.args.get('payment_type')
        drop_off_location_1=request.args.get('drop_off_location_1')
        order_in_muscat=request.args.get('order_in_muscat')
        phone_number_1_to_sent_package_to=request.args.get('phone_number_1_to_sent_package_to')
        phone_number_2_to_sent_package_to=request.args.get('phone_number_2_to_sent_package_to')
        phone_number_3_to_sent_package_to=request.args.get('phone_number_3_to_sent_package_to')
        phone_number_4_to_sent_package_to=request.args.get('phone_number_4_to_sent_package_to')   
        phone_number_5_to_sent_package_to=request.args.get('phone_number_5_to_sent_package_to')     
        response = {"data":{"type":"text","text":"Order is " +" "+ order_in_muscat + " " }}
        return response
            
if __name__ == "__main__":
    app.run(port=5000,debug=True)