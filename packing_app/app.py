from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BagForm, ItemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///packing.db'
db = SQLAlchemy(app)

from models import Bag, Item

@app.route('/')
def index():
    bags = Bag.query.all()
    return render_template('index.html', bags=bags)

@app.route('/create_bag', methods=['GET', 'POST'])
def create_bag():
    form = BagForm()
    if form.validate_on_submit():
        bag = Bag(name=form.name.data)
        db.session.add(bag)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_bag.html', form=form)

@app.route('/create_item/<int:bag_id>', methods=['GET', 'POST'])
def create_item(bag_id):
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, packed=False, bag_id=bag_id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('view_bag', bag_id=bag_id))
    return render_template('create_item.html', form=form, bag_id=bag_id)

@app.route('/view_bag/<int:bag_id>')
def view_bag(bag_id):
    bag = Bag.query.get_or_404(bag_id)
    return render_template('view_bag.html', bag=bag)

@app.route('/toggle_item/<int:item_id>')
def toggle_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.packed = not item.packed
    db.session.commit()
    return redirect(url_for('view_bag', bag_id=item.bag_id))

@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('view_bag', bag_id=item.bag_id))

@app.route('/delete_bag/<int:bag_id>')
def delete_bag(bag_id):
    bag = Bag.query.get_or_404(bag_id)
    db.session.delete(bag)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
