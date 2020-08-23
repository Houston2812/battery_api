from api import app, db
from flask import render_template, url_for, request, jsonify    
from api.models import Laptop


@app.route('/', methods = ["GET"])
def home():
    return render_template("home.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")


@app.route('/api/v1/resources/laptops/all', methods = ["GET"])
def api_all():
    return jsonify({'Laptops': list(map(lambda lap: lap.get_dict(), Laptop.query.all()))})


@app.route('/api/v1/resources/laptops', methods = ["GET"])
def api_filter():
    
    query_params = request.args

    device_name = query_params.get('device_name')
    
    laptop = Laptop.query.filter_by(device_name = device_name).first_or_404()   

    if laptop is not None:
        print(laptop.get_dict())
        return jsonify(laptop.get_dict())
    else:
        return page_not_found(404)


@app.route('/api/v1/resources/laptops', methods = ["POST"])
def api_register():
    if request.is_json:
        content = request.get_json()
        device_name = content['device_name']

        new_device = Laptop(device_name = device_name)
        db.session.add(new_device)
        db.session.commit()

        return  jsonify({'result': True}), 201
    else:
        return  jsonify({'result': False})


@app.route('/api/v1/resources/laptops', methods = ["PUT"])
def api_update():
    if request.is_json:
        print(request.get_json())
            
        content = request.get_json()
        device_name = content['device_name']
        power = content['power']
        percentage = content['percentage']
            
        device = Laptop.query.filter_by(device_name = device_name).first_or_404()
        device.power = power
        device.percentage = percentage
        db.session.commit()

        return  jsonify({
            'result': True,
            'status': device.status
            })
    else:
        return  jsonify({
            'result': False,
            'status': device.status
            })

        
@app.route('/api/v1/resources/laptops/<device_name>', methods = ["DELETE"])
def api_delete(device_name):
    device = Laptop.query.filter_by(device_name = device_name).first_or_404()
    db.session.delete(device)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/api/v1/resources/laptops/status', methods = ['POST'])
def stop_continue():
    if request.is_json:
        print(request.get_json())
        content = request.get_json()
        device_name = content['device_name']
        status = content['status']
        device = Laptop.query.filter_by(device_name = device_name).first_or_404()
        if status == "0":
            device.status = False
            db.session.commit()
        elif status == "1":
            device.status = True
            db.session.commit()
    return jsonify({'result': True}), 202


        
    