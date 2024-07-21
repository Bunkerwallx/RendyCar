# src/grafica.py

# src/generar_grafica.py

import pandas as pd

def generar_html(data):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);

            function drawChart() {
                var data = google.visualization.arrayToDataTable([
                    ['Fecha', 'Rendimiento'],
    """

    for _, row in data.iterrows():
        html += f"['{row['fecha']}', {row['rendimiento']}],\n"

    html += """
                ]);

                var options = {
                    title: 'Rendimiento de Combustible',
                    curveType: 'function',
                    legend: { position: 'bottom' }
                };

                var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
                chart.draw(data, options);
            }
        </script>
    </head>
    <body>
        <div id="curve_chart" style="width: 900px; height: 500px"></div>
    </body>
    </html>
    """

    with open('index.html', 'w') as file:
        file.write(html)

def main():
    datos = pd.read_csv('data/datos_rendimiento.csv')
    generar_html(datos)
    print("Gráfica generada y guardada en 'index.html'")

if __name__ == "__main__":
    main()
