from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import Bag, Item
from .app import db
from .forms import BagForm, ItemForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    bags = Bag.query.all()
    return render_template('index.html', bags=bags)

@main.route('/create_bag', methods=['GET', 'POST'])
def create_bag():
    form = BagForm()
    if form.validate_on_submit():
        bag = Bag(name=form.name.data)
        db.session.add(bag)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_bag.html', form=form)

@main.route('/create_item/<int:bag_id>', methods=['GET', 'POST'])
def create_item(bag_id):
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, packed=False, bag_id=bag_id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('main.view_bag', bag_id=bag_id))
    return render_template('create_item.html', form=form, bag_id=bag_id)

@main.route('/view_bag/<int:bag_id>')
def view_bag(bag_id):
    bag = Bag.query.get_or_404(bag_id)
    return render_template('view_bag.html', bag=bag)

@main.route('/toggle_item/<int:item_id>')
def toggle_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.packed = not item.packed
    db.session.commit()
    return redirect(url_for('main.view_bag', bag_id=item.bag_id))

@main.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('main.view_bag', bag_id=item.bag_id))

@main.route('/delete_bag/<int:bag_id>')
def delete_bag(bag_id):
    bag = Bag.query.get_or_404(bag_id)
    items = Item.query.filter_by(bag_id=bag_id).all()
    for item in items:
        db.session.delete(item)
    db.session.delete(bag)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/save_order', methods=['POST'])
def save_order():
    order = request.json.get('order', [])
    for index, bag_id in enumerate(order):
        bag = Bag.query.get(bag_id)
        if bag:
            bag.order = index
    db.session.commit()
    return jsonify({'status': 'success'})

@main.route('/')
def index():
    bags = Bag.query.order_by(Bag.order).all()
    return render_template('index.html', bags=bags)
