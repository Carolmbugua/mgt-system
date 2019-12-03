from flask import Flask,render_template #help yo service html file to the user
import pygal

    #module import flask file
app = Flask(__name__)
#instanciating
# url#uri uniform resource identifor
@app.route('/')#its a path need to be raped on
def hello_world():
    y = 1000
    return render_template('index.html', x=y)



@app.route('/pies')
def piec():
    ratios = [('Gentlemen', 5),('Ladies', 9)]
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add(ratios[0][0],ratios[0][1])
    pie_chart.add(ratios[1][0],ratios[1][1])
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    pie_data = pie_chart.render_data_uri()

    data = [
    {'month':'January','total': 22},
    {'month':'February','total': 27},{'month':'March','total': 23},{'month':'April','total': 20},
    {'month':'May','total': 12}]

    s = [d['month'] for d in data]
    # for key, value in data.key()]

    t = [x['total'] for x in data]
    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = s

    graph.add('total', t)

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
    x = 'Techcamp'
    return render_template('ginger.html', x=x)