# from urllib.request import proxy_bypass_macosx_sysconf

from flask import Flask,render_template,request,redirect,url_for,flash#help yo service html file to the user
import pygal
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from config.Config import Develpoment


    #module import flask file
app = Flask(__name__)
app.config.from_object(Develpoment)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:#0724246005@127.0.0.1:5432/sales_demo'
# app.config['SECRET_KEY']='LearningPyT'
# app.config['DEBUG']=True
db = SQLAlchemy(app)

from models.inventories import Inventories
from models.sales import Sales
@app.before_first_request
def create_tables():
    db.create_all()


#instanciating
# url#uri uniform resource identifor
@app.route('/')#its a path need to be raped on
def hello_world():
    x = 'Mbugua'
    records = Inventories.fetch_all_records()

    return render_template('index.html',records=records, x=x)

@app.route('/add_inventory', methods=['POST','GET'])
def add_inventories():
    if request.method =='POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['BP']
        selling_price = request.form['SP']
        stock = request.form['stock']

        # print(name)
        # print(type)
        # print(buying_price)
        # print(selling_price)
        # print(stock)

        record =Inventories( name=name, buying_price=buying_price, selling_price=selling_price, type=type, stock=stock)
        record.add_records()
        #return "name"
    return redirect(url_for('hello_world'))

@app.route('/test/<num1>/<num2>')
def test(num1,num2):

   print(int(num1)+int(num2))
   return 'YES'


@app.route('/salepro/<int:id>', methods=['POST','GET'])
def makeSales(id):
    #print(id)
    record = Inventories.fetch_one_records(id)

    if record:
        if request.method == 'POST':
            quantity = request.form['quantity']
            newStock = record.stock - int(quantity)

            record.stock = newStock
            db.session.commit()
            sales = Sales(inv_id=id, quantity=quantity)
            sales.add_records()
            flash('You successfully made a sale', 'success')
            # print(quantity)
            # print(newStock)

    return redirect(url_for('hello_world'))

@app.route('/viewsales/<int:id>')
def viewSales(id):
    product = Inventories.fetch_one_records(id)
    # sales = product.sales
    return render_template('sales.html', product=product)

@app.route('/delete/<int:id>')
def delete(id):
    records = Inventories.fetch_one_records(id)
    print(records.item_id)
    print(records.name)
    db.session.delete(records)
    db.session.commit()
    flash('You have successfully delete the inventory', 'danger')
    return redirect(url_for('hello_world'))

    return 'mojo'

@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
    record = Inventories.fetch_one_records(id)

    if request.method =='POST':
        record.name = request.form['name']
        record.type = request.form['type']
        record.buying_price = request.form['BP']
        record.selling_price = request.form['SP']
        record.stock = request.form['stock']

        db.session.commit()

        return redirect(url_for('hello_world'))
    return  render_template('edit.html', record=record)







import psycopg2


@app.route('/pies')
def piec():

    conn = psycopg2.connect("dbname='sales_demo' user='postgres' host='localhost' password='#0724246005' ")

    cur1 = conn.cursor()

    cur1.execute("""select type,count(type) as type1 from inventories group by type;""")

    records = cur1.fetchall()
    #print(type(records))

    for each in records:
        print(each)

    ratios = [('Product', 5),('Services', 9)]
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add(records[0][0],records[0][1])
    pie_chart.add(records[1][0],records[1][1])
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    pie_data = pie_chart.render_data_uri()

    data = [
        {'month': 'January', 'total': 22},
        {'month': 'February', 'total': 27},
        {'month': 'March', 'total': 23},
        {'month': 'April', 'total': 20},
        {'month': 'May', 'total': 12},
        {'month': 'June', 'total': 32},
        {'month': 'July', 'total': 42},
        {'month': 'August', 'total': 72},
        {'month': 'September', 'total': 52},
        {'month': 'October', 'total': 42},
        {'month': 'November', 'total': 92},
        {'month': 'December', 'total': 102}
    ]
    s = [d['month'] for d in data]
    # # for key, value in data.key()]

    t = [x['total'] for x in data]


    cur = conn.cursor()
    cur.execute("""select sum(i.buying_price*s.quantity) as subtotal, EXTRACT(month from s.created_at) from sales as s join inventories as i
    on i.item_id = s.item_id group by extract(month from s.created_at) order by extract(month from s.created_at)""")

    rows = cur.fetchall()
    # print(type(rows))
    months = []
    total_sales = []
    for each in rows:
        months.append(each[1])
        total_sales.append(each[0])
    print(months)
    print(total_sales)

    graph = pygal.Line()
    graph.title = 'Total products over months.'
    graph.x_labels = months

    graph.add('TS', total_sales)

    # graph.add('Java', [15, 45, 76, 80, 91, 95])
    # graph.add('C++', [5, 51, 54, 102, 150, 201])
    # graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()
    return render_template("dashboard.html", graph_data=graph_data, pie_data=pie_data)



    # return render_template('dashboard.html', pie_data=pie_data)


# @app.route('/pie')
# def piechart():
#     return render_template('dashboard.html')
    # pie_chart = pygal.Pie()
    # pie_chart.title = 'Browser usage in February 2012 (in %)'
    # pie_chart.add('IE', 19.5)
    # pie_chart.add('Firefox', 36.6)
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    # pie_data = piechart.render_data_uri()

    # return render_template('dashboard.html')

@app.route('/about')
def index_page():

    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run()
#a chart is a diagramatical representation of your data
#pygal - its an external python module that helps us draw charts in variety of sytle

@app.route('/ginger')
def ginger_page():
    x = 'Online Library'
    return render_template('ginger.html', x=x)